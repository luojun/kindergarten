# SEA Kindergarten simulation (MuJoCo digital twin)

- [ ] To be reviewed by a human!

This directory contains the MuJoCo scene and agents for the kindergarten digital twin.

## Scene

- **kindergarten.xml**: Reference layout matching [docs/LAYOUT.md](../docs/LAYOUT.md):
  - Play yard 5 m (E–W) × 8 m (N–S); play pen 2 m × 1.5 m at +36 cm; crib 0.6 m × 0.8 m at +18 cm inside pen
  - Two charging pads (10×10 cm) in crib with sites `charging_zone_1`, `charging_zone_2`
  - Fence around pen (gaps for north and east gates), ramp on crib east, terrace step(s)
  - Sound flower in yard (stationary base + rotating head, hinge + motor)
- **kindergarten_ema.xml**: Same scene + EMA (ant); used by `env/kindergarten_ema.py`

## Usage

Requires `mujoco` (and optionally `dm_control` for the ant). From repo root:

```bash
pip install mujoco
python sim/load_scene.py
```

## Life model and agents

- Charging is implemented in Python: when the agent (e.g. EMA) is within the charging zone, battery increases.
- See `env/` for the gym-like environment that composes the scene with EMA and life logic.
