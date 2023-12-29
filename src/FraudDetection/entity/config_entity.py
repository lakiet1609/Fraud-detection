from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionCongfig:
    unzip_dir: Path
    train_path: Path
    test_path: Path
    source_url: str
    local_data_file: Path
    data_path: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    train_path: Path
    test_path: Path
    train_arr: Path
    test_arr: Path
    preprocessor_path: Path


@dataclass(frozen=True)
class ModelTrainingConfig:
    model_path: Path
    test_arr: Path
    train_arr: Path
    train_result: Path
    test_result: Path
