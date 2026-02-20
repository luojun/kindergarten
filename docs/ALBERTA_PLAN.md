# Alberta Plan in the Kindergarten

- [ ] To be reviewed by a human!

The SEA Kindergarten is a physical and virtual testbed for research aligned with the **Alberta Plan**: continual learning in a “big world,” with temporal uniformity and sensorimotor abstraction.

## Link: environment, life, algorithms

- **Environment**: The kindergarten (crib → play pen → play yard) is an **auto-curriculum** in space: the agent can start in the crib and progress by leaving it, climbing to the play pen, and then to the open yard. The environment is open to foot traffic (humans and robots), so the world is **bigger** than any fixed dataset—imperfect information and continual adaptation are required.

- **Life**: Battery and charging implement **continual living**. There is no episodic “game over” in the sense of a fixed task; the agent must maintain its own viability by returning to the charging zone. Reward is tied to survival and to being on the pad, supporting **temporal uniformity**: every step matters for life, not just special training phases.

- **Algorithms**: The testbed is agnostic to the learning algorithm. Suitable candidates include methods that learn step-by-step (e.g. temporal-difference learning), build state or world models, and use curiosity or empowerment for exploration. The kindergarten stresses **sensorimotor abstraction** (e.g. approaching the pad, climbing the step) and **continual learning for continual living**—and eventually for **creating** (e.g. object use, collaboration with other agents).

## What we evaluate

We evaluate whether agents can survive long horizons, discover the crib → pen → yard progression, and exhibit robust behavior under layout and traffic variations. See [EVALUATION.md](EVALUATION.md) for the protocol and metrics.
