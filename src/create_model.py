# Standard Library Imports
from pathlib import Path
from os import environ

# Third-Party Imports
from dotenv import load_dotenv
from roboflow import Roboflow
from ultralytics import YOLO

# Local Imports


class ModelMaker():
    def __init__(self,):
        # Load environment from .env
        env_location = "./.env"
        if not load_dotenv(env_location):
            print(f"[ModelMaker.__init__()] Could not load {env_location}")

    def run(self,):
        # Download dataset if necessary
        dataset_path = Path("datasets")
        # If datasets_path does not exist or it is empty...
        if not dataset_path.exists() or not dataset_path.iterdir():
            dataset_path = self._download_dataset()
        
        return self._prepare_model()

    def _download_dataset(self,):
        rf = Roboflow(api_key=environ["ROBOFLOW_API_KEY"])
        project = rf.workspace("teststage").project("electronic-components-odddk")
        version = project.version(2)
        dataset = version.download(model_format="yolo26", location="./datasets")
        return dataset.location

    def _prepare_model(self, dataset_path: str):
        model = YOLO("yolo26n-cls.yaml")
        model.train(data=self._download_dataset(),                                                       epochs=3)
        model.val()
        return model