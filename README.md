### SEA Kindergarten

SEA Kindergarten is a kindergarten of robots, a physical environment for robots to continually learn by living a life in it along with other robots.

#### Robots

1. A few Open Ants (from Openmind, Gymnasium style and physical).
2. A robot dog, Unitree Go2 or similar.
3. A couple of SolPals (Super Sunflower) or Soundflowers, possibly implemented with budget 4-6 DOF robotic arms.
4. Etc.
5. Caretaker robot: a mobile manipulator that does not need to learn but put the kindergarten back in order at night, including resuscitating dead ants.

#### Environment

1. Openness: open to humans and robots to go in and out.
2. A "live-in" environment for robots to get all their needs for survival and learning met.
3. Telemetry: robots are remotely monitored, and may be remotely controlled but
no learning from remote control.

#### Research

1. Alberta Plan: learning algorithms and especially the OaK architecture
2. Continual Learning for Continual Living, with auto-curriculum.
3. Sensorimotor abstraction architecture

#### Phase 1 (digital twin + EMA + evaluation)

- **Physical layout**: [docs/LAYOUT.md](docs/LAYOUT.md) — reference dimensions, diagram, build notes.
- **Simulation**: [sim/](sim/) — MuJoCo scene (crib, play pen, play yard, charging zone, sound flower); [sim/kindergarten_ema.xml](sim/kindergarten_ema.xml) includes EMA (ant).
- **Environment**: [env/kindergarten_ema.py](env/kindergarten_ema.py) — life model (battery drain, charging), observation, reward.
- **Evaluation**: [docs/EVALUATION.md](docs/EVALUATION.md) — metrics and protocol; [eval/run_eval.py](eval/run_eval.py) — run with fixed seeds, output JSON.
- **Alberta Plan**: [docs/ALBERTA_PLAN.md](docs/ALBERTA_PLAN.md) — how the kindergarten supports the vision.

Run (with venv): `pip install -r requirements.txt` then `python env/run_ema.py` or `python eval/run_eval.py --out results.json`.
