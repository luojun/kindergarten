# SEA Kindergarten: Reference Physical Layout

Indoor, workshop-cum-playground environment open to foot traffic. Play yard with raised play pen; one crib inside the play pen. Auto-curriculum: crib → play pen → play yard. Robot caretaker (wheeled mobile manipulator) can be sent around the yard and into the play pen to return ants to the charging pad.

## Diagram (top view, N = +y, E = +x)

```
    N (+y)
    ^
    |   PLAY YARD 5 m (E-W) x 8 m (N-S)
    |   +--------------------------------------------------+
    |   |                    [sound flower]                |
    |   |  +------------------+  north gate (to ramp)       |
    |   |  |   PLAY PEN       |  (middle of north side)     |
    |   |  |  2m (E-W) x 1.5m |  fence 1m from pen floor   |
    |   |  |  floor +36cm     |                             |
    |   |  |  +----------+    |  east gate (near S corner)  |
    |   |  |  |  CRIB    |    |                             |
    |   |  |  | 0.6x0.8m | ramp (E side)                    |
    |   |  |  | floor    | 2 steps (N,W,S) 9cm/18cm        |
    |   |  |  | +18cm    | [pad1] [pad2]                    |
    |   |  |  +----------+                                  |
    |   |  |  terrace: 2 steps down to yard (18cm rise,     |
    |   |  +--|-----------+  30cm run each)                  |
    |   |     ingress/egress                                |
    +---+---------------------------------------------------+
        origin (0,0)  ---> E (+x)
```

## Dimensions

### Play yard
| Item | Size | Notes |
|------|------|--------|
| **Play yard** | 5 m (E–W) × 8 m (N–S) | Main floor (z = 0). Open to foot traffic. |

### Play pen
| Item | Size | Notes |
|------|------|--------|
| **Play pen** | 150 cm (N–S) × 200 cm (E–W) | Whole area raised **36 cm** above play yard floor. |
| **Fence** | 1 m high from play pen floor | Surrounds play pen; gates are openings. |
| **Terrace** | 2 steps down to yard | Each step: **18 cm** rise, **30 cm** run. |
| **North gate** | Middle of north side | Double-swinging, 80 cm wide × 80 cm tall, sill 10 cm above pen floor. Opens to ramp. |
| **East gate** | Near south corner, east side | Same: 80 cm × 80 cm, 10 cm sill. Push open from inside or outside. |

### Crib (inside play pen)
| Item | Size | Notes |
|------|------|--------|
| **Crib floor** | 60 cm (E–W) × 80 cm (N–S) | **18 cm below** play pen floor (+18 cm above play yard). Flat. |
| **Charging pads** | Two, each 10 cm × 10 cm | Non-symmetrically placed on crib floor. |
| **East side** | Ramp | Down from play pen floor to crib floor; **36 cm** run. |
| **N, W, S sides** | Two steps down from pen | Each step: **9 cm** rise, **18 cm** run. |

### Robot caretaker
- Wheeled mobile manipulator; can be sent around the yard and into the play pen (through the north gate) to place ants that have run out of battery back on a charging pad.

## Zones summary

- **Crib**: Two wireless charging pads; first stage of auto-curriculum; ramp (east) and steps (N, W, S) to play pen.
- **Play pen**: Raised, fenced, two gates; terrace steps down to play yard.
- **Play yard**: Main level; open to humans and robots; sound flower, caretaker, future BYOR.

## Materials and safety (build notes)

- **Floor**: Smooth, low-friction; no loose cables in traffic.
- **Steps / ramp**: Rounded edges; dimensions as above.
- **Charging**: Pads flush or recessed; cable routing away from walkways.
- **Fence / gates**: No sharp edges; gates open both ways.

## Telemetry

- **Power**: Battery level and charging state when on a pad.
- **Pose**: Position and orientation of each robot (and sound flower if applicable).
- **Optional**: Remote control for experiments and demos; video feeds.

This layout is the reference for the **digital twin** (MuJoCo scene) and for building the physical kindergarten.
