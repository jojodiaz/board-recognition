"""Dataset acquisition: download from Roboflow, ensure it exists locally."""

from os import environ
from pathlib import Path

from roboflow import Roboflow

from board_recognition.config import CONFIG, RoboflowConfig


def _is_empty(path: Path) -> bool:
    """True if path missing or has no entries."""
    return not path.exists() or not any(path.iterdir())


def download_dataset(
    dest: Path = CONFIG.datasets_dir,
    rf_cfg: RoboflowConfig = CONFIG.roboflow,
) -> Path:
    """Download the dataset from Roboflow into dest. Returns its location."""
    api_key = environ.get(rf_cfg.api_key_env)
    if not api_key:
        raise RuntimeError(
            f"Missing {rf_cfg.api_key_env}. Set it in {CONFIG.env_file} or the environment."
        )

    rf = Roboflow(api_key=api_key)
    project = rf.workspace(rf_cfg.workspace).project(rf_cfg.project)
    version = project.version(rf_cfg.version)
    dataset = version.download(model_format=rf_cfg.model_format, location=str(dest))
    return Path(dataset.location)


def ensure_dataset(dest: Path = CONFIG.datasets_dir) -> Path:
    """Return local dataset path, downloading it only if missing/empty."""
    if _is_empty(dest):
        return download_dataset(dest)
    return dest
