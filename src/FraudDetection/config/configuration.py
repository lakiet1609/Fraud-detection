from FraudDetection.constants import *
import os
from pathlib import Path
from FraudDetection.utils.common import read_yaml, create_directories
from FraudDetection.entity.config_entity import DataIngestionCongfig


class ConfigurationManager:
    def __init__(self, 
                 config_path=CONFIG_FILE_PATH):
    
        self.config = read_yaml(config_path)
        create_directories(self.config['artifacts_root'])
    
    def get_data_ingestion_config(self) -> DataIngestionCongfig:
        config = self.config['data_ingestion']
        
        data_ingestion_config = DataIngestionCongfig(
            root_dir=config['root_dir'],
            train_path=config['train_path'],
            test_path=config['test_path'],
            validation_path=config['validation_path']
        )
        
        return data_ingestion_config