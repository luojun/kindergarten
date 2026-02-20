# SEA Kindergarten simulation (MuJoCo digital twin)

- [ ] To be reviewed by a human!

This directory contains the MuJoCo scene and agents for the kindergarten digital twin.

## Scene

- **kindergarten.xml**: Reference layout matching [docs/LAYOUT.md](../docs/LAYOUT.md):
  - Play yard (3×3 m ground plane)
  - Crib (0.6×0.6 m) with charging pad and `charging_zone` site
  - Play pen (1.2×1.2 m) at 8 cm height
  - Sound flower (stationary base + rotating head, hinge + motor)
- **kindergarten_ema.xml**: Same scene + EMA (ant) + sound flower; used by `env/kindergarten_ema.py`

## Usage

Requires `mujoco` (and optionally `dm_control` for the ant). From repo root:

```bash
pip install mujoco
python sim/load_scene.py
```

## Life model and agents

- Charging is implemented in Python: when the agent (e.g. EMA) is within the charging zone, battery increases.
- See `env/` for the gym-like environment that composes the scene with EMA and life logic.
