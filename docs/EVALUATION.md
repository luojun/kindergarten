# SEA Kindergarten: Evaluation Protocol

- [ ] To be reviewed by a human!

Evaluation is **continual**: no train/test split; agents run in the same environment over long horizons. Metrics are computed over time and over multiple runs with fixed seeds for reproducibility.

## Metrics

| Metric | Description |
|--------|-------------|
| **Survival rate** | Fraction of episodes that do not end in death (battery > 0 at horizon). |
| **Mean episode length** | Mean number of steps until done (death or max_steps). |
| **Charging visits** | Number of steps (or transitions) during which the agent was on the charging zone. |
| **Time to leave crib** | First step at which torso xy is outside the crib bounding box (e.g. [0, 0.6] × [0, 0.6]). |
| **Time in play yard** | Number of steps with torso in play yard (e.g. outside crib and outside play pen footprint). |
| **Crib → pen → yard** | Binary or count: whether the agent reached pen (and optionally yard) after starting in crib. |

## Protocol

1. **Seeds**: Use a fixed list of seeds (e.g. `[0, 1, ..., 9]`) for reproducibility.
2. **Horizon**: Each episode runs for at most `max_steps` (e.g. 5000).
3. **No train/test**: Same scene and env for all evaluation; no separate test environment.
4. **Reporting**: Report mean and std (or quartiles) over seeds for each metric.

## Running evaluations

From repo root (with venv activated):

```bash
python eval/run_eval.py --config eval/config.yaml --seeds 0,1,2,3,4 --out results.json
```

See `eval/config.yaml` for default env and evaluation parameters. Results are written to the specified output file and optionally printed.

## Reproducibility

- Scene: `sim/kindergarten_ema.xml` (version-controlled).
- Env parameters: `battery_drain`, `charging_rate`, `max_steps` in config.
- Seeds: fixed per run; report seeds in results.
