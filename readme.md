---
droneSweep — Polygon Coverage Path Planning
---

<!-- Badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![PyPI - Status](https://img.shields.io/badge/status-experimental-orange)](#)
[![Made with PyTorch](https://img.shields.io/badge/pytorch-%3E%3D2.0.0-red)](https://pytorch.org/)

# droneSweep

Lightweight reinforcement learning framework for polygon coverage path planning with obstacle avoidance.

Summary

- Trains PPO agents to cover polygonal areas efficiently while avoiding obstacles.
- Includes environment, training scripts, and evaluation/visualization helpers.
- Works with CPU, CUDA-enabled NVIDIA GPUs, and Apple Silicon (MPS).

Table of Contents

- [Highlights](#highlights)
- [Quick links](#quick-links)
- [Requirements](#requirements)
- [Install](#install)
- [Quick start](#quick-start)
- [Project layout](#project-layout)
- [Core ideas](#core-ideas)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

Highlights

- Multi-objective reward (coverage, time, collisions)
- Handles irregular polygons and dynamic obstacles
- Training, evaluation and visualization scripts included

Quick links

- Code: `src/`
- Notebooks: `ShapeOptimzation.ipynb` (and others in `notebooks/`)
- Models & logs: `data/models/`, `logs/tensorboard/`

Requirements

- Python 3.8+
- Recommended: GPU with CUDA (for faster training) or Apple Silicon (MPS)
- Dependencies are listed in `requirements.txt`

Install

1. Clone the repo:

```bash
git clone <your-repo-url>
cd droneSweep
```

2. Create and activate a virtualenv (macOS / Linux):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Quick start

1) Train with default settings:

```bash
source venv/bin/activate
python scripts/train.py
```

2) Monitor with TensorBoard:

```bash
tensorboard --logdir=./logs/tensorboard/ --port=6006
```

3) Generate dataset:

```bash
python scripts/generate_dataset.py --num_samples 10000 --output data/processed/
```

4) Evaluate a model:

```bash
python scripts/evaluate.py --model data/models/polygon_coverage_ppo.zip
```

Project layout (important files)

- `src/` — core code (environment, models, utils)
- `scripts/` — training, evaluation and visualization helpers
- `data/` — models and processed datasets
- `notebooks/` — exploratory and training notebooks
- `logs/` — tensorboard logs

Architecture (visual)

![Architecture placeholder](assets/architecture.png)

Core ideas

- The agent observes its pose plus dense coverage and obstacle maps (e.g., 64×64).
- The actor outputs continuous forward and angular velocities via a Gaussian policy.
- Rewards balance coverage gain, time penalty, collision and boundary penalties, and a return bonus.

Configuration

- Edit `configs/default.yaml` for environment and training hyperparameters.

Troubleshooting (common)

- ModuleNotFoundError: install requirements with `pip install -r requirements.txt`.
- CUDA OOM: reduce batch size / `n_steps` or run on CPU.
- Shapely build issues on Windows: prefer installing via conda.

Contributing

- Fork → branch → PR. Please run tests (`pytest`) and format code (`black`) before submitting.

License

- MIT — see `LICENSE`.

Happy training!
