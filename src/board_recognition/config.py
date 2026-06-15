"""Central config: paths and training/dataset parameters.

Add new settings here rather than scattering literals across modules.
"""

from dataclasses import dataclass, field
from pathlib import Path

# Project root = two levels up from src/board_recognition/config.py
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASETS_DIR = PROJECT_ROOT / "datasets"
RUNS_DIR = PROJECT_ROOT / "runs"
ENV_FILE = PROJECT_ROOT / ".env"


@dataclass(frozen=True)
class RoboflowConfig:
    workspace: str = "teststage"
    project: str = "electronic-components-odddk"
    version: int = 2
    model_format: str = "yolo26"
    api_key_env: str = "ROBOFLOW_API_KEY"


@dataclass(frozen=True)
class TrainConfig:
    model: str = "yolo26n-cls.yaml"
    epochs: int = 3


@dataclass(frozen=True)
class Config:
    datasets_dir: Path = DATASETS_DIR
    runs_dir: Path = RUNS_DIR
    env_file: Path = ENV_FILE
    roboflow: RoboflowConfig = field(default_factory=RoboflowConfig)
    train: TrainConfig = field(default_factory=TrainConfig)


CONFIG = Config()
