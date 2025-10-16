import numpy as np

class PolygonCoverageEnv:
    """Minimal stub of the environment used by examples/tests.

    This is a lightweight placeholder. Replace with the full implementation.
    """

    def __init__(self, vertices=None, grid_size=64, max_steps=1000):
        self.vertices = vertices or [(0,0),(1,0),(1,1),(0,1)]
        self.grid_size = grid_size
        self.max_steps = max_steps
        self.step_count = 0

    def reset(self):
        self.step_count = 0
        obs = np.zeros((self.grid_size, self.grid_size), dtype=np.float32)
        return obs

    def step(self, action):
        self.step_count += 1
        obs = np.zeros((self.grid_size, self.grid_size), dtype=np.float32)
        reward = 0.0
        done = self.step_count >= self.max_steps
        info = {}
        return obs, reward, done, info
