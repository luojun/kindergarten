### SEA Kindergarten

SEA Kindergarten is a kindergarten of robots, a physical environment for robots to continually learn by living a life in it along with other robots.

#### Robots

1. Ant, MuJoCo style and physical. (EMA, or Embodied MuJoCo Ant)
2. Robot dog, Unitree style and physical.
3. Sunflower or Soundflower, standing alone but rotates.

#### Environment

1. Openness: open to humans and robots to go in and out.
2. A "live-in" environment for robots to get all their needs for survival and learning met.
3. Telemetry: robots are remotely monitored, and may be remotely controlled.

#### Research

1. Sensorimotor Abstraction Architecture
2. Alberta Plan Learning Algorithms
3. Continual Learning for Continual Living -- auto-curriculum.

---

#### Phase 1 (digital twin + EMA + evaluation)

- [ ] To be reviewed by a human!

- **Physical layout**: [docs/LAYOUT.md](docs/LAYOUT.md) — reference dimensions, diagram, build notes.
- **Simulation**: [sim/](sim/) — MuJoCo scene (crib, play pen, play yard, charging zone, sound flower); [sim/kindergarten_ema.xml](sim/kindergarten_ema.xml) includes EMA (ant).
- **Environment**: [env/kindergarten_ema.py](env/kindergarten_ema.py) — life model (battery drain, charging), observation, reward.
- **Evaluation**: [docs/EVALUATION.md](docs/EVALUATION.md) — metrics and protocol; [eval/run_eval.py](eval/run_eval.py) — run with fixed seeds, output JSON.
- **Alberta Plan**: [docs/ALBERTA_PLAN.md](docs/ALBERTA_PLAN.md) — how the kindergarten supports the vision.

Run (with venv): `pip install -r requirements.txt` then `python env/run_ema.py` or `python eval/run_eval.py --out results.json`.



