# Board Recognition

Train a YOLO classifier on electronic-component images.

## REQUIREMENTS
* Python>=3.14
* uv package manager>=0.11.16
* CMake>=4.0.0

## USAGE
```bash
uv sync
uv run board-recognition train --clean
```

## ARCHITECTURE

```mermaid
flowchart TD
    CLI["cli.py<br/>argparse · train --clean"]
    Model["model.py<br/>ModelMaker"]
    Dataset["dataset.py<br/>ensure_dataset / download_dataset"]
    Config["config.py<br/>CONFIG · dataclasses"]

    Roboflow(["Roboflow API"])
    YOLO(["Ultralytics YOLO"])
    Env([".env<br/>ROBOFLOW_API_KEY"])
    Runs(["runs/ output"])

    CLI -->|train| Model
    CLI -->|--clean| Runs
    Model --> Dataset
    Model -->|train/val| YOLO
    Dataset -->|download if missing| Roboflow
    Model -->|load_dotenv| Env

    Config -.-> CLI
    Config -.-> Model
    Config -.-> Dataset
```

### Module roles
| Module | Role |
|--------|------|
| `config.py` | Central paths + Roboflow/Train params (frozen dataclasses, `CONFIG`) |
| `dataset.py` | Download from Roboflow; skip if dataset already present |
| `model.py` | `ModelMaker` — ensure dataset, train, validate |
| `cli.py` | Entry point `board-recognition train [--clean]` |
