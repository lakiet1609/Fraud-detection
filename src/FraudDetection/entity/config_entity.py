from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionCongfig:
    root_dir: Path
    train_path: Path
    test_path: Path
    validation_path: Path
