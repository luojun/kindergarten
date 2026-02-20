# SEA Kindergarten: Reference Physical Layout

- [ ] To be reviewed by a human!

Indoor, workshop-cum-playground environment open to foot traffic. Single bounded zone with crib, play pen, and play yard for the auto-curriculum (crib → play pen → play yard).

## Diagram (top view)

```
                    ingress/egress (open)
    +----------------------------------------------------------+
    |                     OPEN FLOOR / PLAY YARD               |
    |  (main level, wheeled/legged/future flying zone)         |
    |                                                          |
    |    +-------------------+     [sound flower]              |
    |    |   PLAY PEN        |        (anchor)                 |
    |    |  (raised terrace) |                                 |
    |    |  +------------+   |                                 |
    |    |  |   CRIB     |   |   step up (~8 cm)               |
    |    |  | [charging] |   |   from crib to pen              |
    |    |  +------------+   |                                 |
    |    +-------------------+   terrace to yard (main level)  |
    |                                                          |
    +----------------------------------------------------------+
```

## Dimensions (minimal “start small” footprint)

| Zone | Size | Height / step | Notes |
|------|------|----------------|--------|
| **Crib** | 60 cm × 60 cm | Floor level | Wireless charging pad centered; low wall ~5 cm to contain ant. |
| **Step (crib → pen)** | Full crib edge | 8 cm up | Single step; climbable by EMA. |
| **Play pen** | 120 cm × 120 cm | +8 cm from floor | Terraced area; one step from crib. |
| **Play pen → play yard** | Full pen edge | 0 cm (flush) or small curb | Ramp or flush to main floor. |
| **Play yard / open floor** | 300 cm × 300 cm (min) | Main floor | Room for EMA, flower, later wheeled/flying. |
| **Sound flower anchor** | 30 cm × 30 cm | Main floor | Fixed spot; no obstacle to traffic. |

**Total minimal footprint**: ~3 m × 3 m (play yard) containing crib + play pen in one corner.

## Zones summary

- **Crib**: Wireless charging pad at bottom; first stage of auto-curriculum; contained so EMA can learn to step out.
- **Play pen**: One step up from crib; intermediate exploration; optional second charging pad for later.
- **Play yard**: Main level; open to humans and robots; shared utilities (charging, flower, future BYOR).
- **Openness**: No full enclosure; clear ingress/egress so the world stays “big” (unpredictable traffic).

## Materials and safety (build notes)

- **Floor**: Smooth, low-friction where robots run (e.g. laminate or sealed wood); no loose cables in traffic.
- **Step/terrace**: Rounded edges; height 8 cm for ant-scale step-up.
- **Charging**: Wireless pad(s) flush or recessed; cable routing under or along wall, not across walkway.
- **Crib wall**: Soft or rounded (e.g. foam strip) so no sharp edges.
- **Telemetry**: Power and pose feeds; optional remote control; mount cameras/sensors so they don’t obstruct movement.

## Telemetry

- **Power**: Battery level (and charging state when on pad).
- **Pose**: Position and orientation of each robot (and sound flower angle if applicable).
- **Optional**: Remote control for experiments and demos; video feeds for monitoring.

This layout is the reference for the **digital twin** (MuJoCo scene) and for building the minimal physical crib+pen in Phase 2.
