"""Dataset generator placeholder."""

import os
import sys
import json

# Ensure repo root is on sys.path so `from src...` imports work when running the script directly
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.environment.polygon_env import PolygonCoverageEnv


def main():
    env = PolygonCoverageEnv()
    obs = env.reset()
    sample = {'obs_shape': getattr(obs, 'shape', None)}
    print(json.dumps(sample))


if __name__ == "__main__":
    main()
