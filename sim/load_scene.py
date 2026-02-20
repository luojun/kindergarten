#!/usr/bin/env python3
"""Load and optionally render the kindergarten MuJoCo scene (no robot)."""
import os
import mujoco

_ASSET_DIR = os.path.dirname(os.path.abspath(__file__))


def load_kindergarten_model():
    path = os.path.join(_ASSET_DIR, "kindergarten.xml")
    return mujoco.MjModel.from_xml_path(path)


def main():
    model = load_kindergarten_model()
    data = mujoco.MjData(model)
    print("Kindergarten model loaded.")
    print("  Bodies:", [model.id2name(i, "body") for i in range(model.nbody)])
    print("  Sites: charging_zone, flower_anchor")
    # Optional: render with mujoco.viewer if available (mujoco 3.x)
    try:
        mujoco.viewer.launch_passive(model, data)
    except Exception:
        print("  (Launch viewer with: python -c 'import sim.load_scene as L; import mujoco; m=L.load_kindergarten_model(); d=mujoco.MjData(m); mujoco.viewer.launch_passive(m,d)' )")


if __name__ == "__main__":
    main()
