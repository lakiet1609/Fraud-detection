import os
import yaml
import json
from pathlib import Path
from FraudDetection import logger
import pickle


def read_yaml(path: Path):
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path} loaded successfully')
            return content
    except Exception as e:
        raise e


def create_directories(path_dir):
    os.makedirs(path_dir, exist_ok=True)


def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")


def load_json(path: Path):
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded succesfully from: {path}")
    return content


def save_object(file_path, obj):
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, "wb") as file_obj:
        pickle.dump(obj, file_obj)


def load_object(file_path):
    with open(file_path, "rb") as file_obj:
        return pickle.load(file_obj)


