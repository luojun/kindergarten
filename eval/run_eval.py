#!/usr/bin/env python3
"""
Run evaluation protocol for Kindergarten EMA env: fixed seeds, metrics, output JSON.
"""
import argparse
import json
import os
import sys

import numpy as np
import yaml

# Add repo root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from env.kindergarten_ema import KindergartenEMA


def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)


def in_zone(xy, x_range, y_range):
    return (x_range[0] <= xy[0] <= x_range[1]) and (y_range[0] <= xy[1] <= y_range[1])


def run_episode(env, seed, zones, max_steps):
    obs = env.reset(seed=seed)
    charging_visits = 0
    time_to_leave_crib = None
    steps_in_play_yard = 0
    left_crib = False
    total_reward = 0.0
    for step in range(max_steps):
        action = np.zeros(env.action_space[0])  # or use a policy
        obs, reward, done, info = env.step(action)
        total_reward += reward
        if info["on_charging_zone"]:
            charging_visits += 1
        xy = env.get_torso_xy()
        if not left_crib and not in_zone(xy, zones["crib_x"], zones["crib_y"]):
            left_crib = True
            if time_to_leave_crib is None:
                time_to_leave_crib = step
        if left_crib and not in_zone(xy, zones["pen_x"], zones["pen_y"]):
            steps_in_play_yard += 1
        if done:
            break
    return {
        "seed": seed,
        "steps": step + 1,
        "done_by_death": info["battery"] <= 0,
        "total_reward": float(total_reward),
        "charging_visits": charging_visits,
        "time_to_leave_crib": time_to_leave_crib,
        "steps_in_play_yard": steps_in_play_yard,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=os.path.join(os.path.dirname(__file__), "config.yaml"), help="Config YAML")
    ap.add_argument("--seeds", default="0,1,2,3,4", help="Comma-separated seeds")
    ap.add_argument("--out", default=None, help="Output JSON path")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    cfg = load_config(args.config)
    seeds = [int(s) for s in args.seeds.split(",")]
    env_cfg = cfg["env"]
    env = KindergartenEMA(
        model_path=env_cfg.get("model_path"),
        battery_drain=env_cfg.get("battery_drain", 0.002),
        charging_rate=env_cfg.get("charging_rate", 0.01),
        battery_cap=env_cfg.get("battery_cap", 1.0),
        charging_radius=env_cfg.get("charging_radius", 0.2),
        max_steps=env_cfg.get("max_steps", 5000),
    )
    zones = cfg.get("zones", {
        "crib_x": [0.0, 0.6], "crib_y": [0.0, 0.6],
        "pen_x": [0.0, 1.2], "pen_y": [0.0, 1.2],
    })
    max_steps = env_cfg.get("max_steps", 5000)
    results = []
    for seed in seeds:
        r = run_episode(env, seed, zones, max_steps)
        results.append(r)
        if not args.quiet:
            print("Seed", seed, "steps", r["steps"], "death", r["done_by_death"], "charging_visits", r["charging_visits"])
    # Aggregate
    survival_rate = 1.0 - np.mean([r["done_by_death"] for r in results])
    mean_steps = np.mean([r["steps"] for r in results])
    out = {
        "config": args.config,
        "seeds": seeds,
        "survival_rate": float(survival_rate),
        "mean_episode_length": float(mean_steps),
        "episodes": results,
    }
    if args.out:
        with open(args.out, "w") as f:
            json.dump(out, f, indent=2)
        if not args.quiet:
            print("Wrote", args.out)
    if not args.quiet:
        print("Survival rate:", survival_rate, "Mean steps:", mean_steps)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
