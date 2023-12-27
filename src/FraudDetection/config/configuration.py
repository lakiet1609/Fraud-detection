from FraudDetection.constants import *
import os
from pathlib import Path
from FraudDetection.utils.common import read_yaml, create_directories
from FraudDetection.entity.config_entity import DataIngestionCongfig, DataTransformationConfig


class ConfigurationManager:
    def __init__(self, 
                 config_path=CONFIG_FILE_PATH):
    
        self.config = read_yaml(config_path)
    
    def get_data_ingestion_config(self) -> DataIngestionCongfig:
        config = self.config['data_ingestion']
        
        data_ingestion_config = DataIngestionCongfig(
            root_dir=config['root_dir'],
            train_path=config['train_path'],
            test_path=config['test_path'],
            validation_path=config['validation_path']
        )
        
        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config['data_transformation']
        create_directories(config['root_dir'])
        
        data_ingestion_config = DataTransformationConfig(
            train_path= config['train_path'],
            test_path=config['test_path'],
            train_arr=config['train_arr'],
            test_arr=config['test_arr']
        )
        
        return data_ingestion_config