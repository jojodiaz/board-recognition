import os
import shutil
import argparse
from create_model import ModelMaker

def main():
    clean_runs()
    model_maker = ModelMaker()
    model = model_maker.run()


def clean_runs():
    shutil.rmtree("./runs")    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--create")
    main()
