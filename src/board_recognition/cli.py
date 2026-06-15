"""Command-line entry point."""

import argparse
import shutil

from board_recognition.config import CONFIG
from board_recognition.model import ModelMaker


def clean_runs() -> None:
    """Remove the runs/ output directory if present."""
    shutil.rmtree(CONFIG.runs_dir, ignore_errors=True)


def train(clean: bool = False) -> None:
    if clean:
        clean_runs()
    ModelMaker().run()


def main() -> None:
    parser = argparse.ArgumentParser(prog="board-recognition")
    subparsers = parser.add_subparsers(dest="command", required=True)

    train_p = subparsers.add_parser("train", help="train and validate the model")
    train_p.add_argument(
        "-c", "--clean", action="store_true", help="delete runs/ before training"
    )
    args = parser.parse_args()

    if args.command == "train":
        train(clean=args.clean)


if __name__ == "__main__":
    main()
