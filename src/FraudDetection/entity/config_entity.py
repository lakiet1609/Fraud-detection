from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionCongfig:
    root_dir: Path
    train_path: Path
    test_path: Path
    validation_path: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    train_path: Path
    test_path: Path
    train_arr: Path
    test_arr: Path
