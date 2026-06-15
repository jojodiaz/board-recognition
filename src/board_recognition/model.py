"""Model training/validation wrapper around Ultralytics YOLO."""

from pathlib import Path

from dotenv import load_dotenv
from ultralytics import YOLO

from board_recognition.config import CONFIG, TrainConfig
from board_recognition.dataset import ensure_dataset


class ModelMaker:
    def __init__(self, train_cfg: TrainConfig = CONFIG.train):
        self.train_cfg = train_cfg
        if not load_dotenv(CONFIG.env_file):
            print(f"[ModelMaker] Could not load {CONFIG.env_file}")

    def run(self) -> YOLO:
        """Ensure dataset is present, then train and validate the model."""
        dataset_path = ensure_dataset()
        return self._prepare_model(dataset_path)

    def _prepare_model(self, dataset_path: Path) -> YOLO:
        model = YOLO(self.train_cfg.model)
        model.train(data=str(dataset_path), epochs=self.train_cfg.epochs)
        model.val()
        return model
