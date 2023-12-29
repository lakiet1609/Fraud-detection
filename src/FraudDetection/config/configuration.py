from FraudDetection.constants import *
import os
from pathlib import Path
from FraudDetection.utils.common import read_yaml, create_directories
from FraudDetection.entity.config_entity import DataIngestionCongfig, DataTransformationConfig, ModelTrainingConfig


class ConfigurationManager:
    def __init__(self, 
                 config_path=CONFIG_FILE_PATH):
    
        self.config = read_yaml(config_path)
    
    def get_data_ingestion_config(self) -> DataIngestionCongfig:
        config = self.config['data_ingestion']
        
        data_ingestion_config = DataIngestionCongfig(
            unzip_dir=config['unzip_dir'],
            train_path=config['train_path'],
            test_path=config['test_path'],
            source_url=config['source_url'],
            local_data_file=config['local_data_file'],
            data_path=config['data_path']
        )
        
        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config['data_transformation']
        create_directories(config['root_dir'])
        
        data_ingestion_config = DataTransformationConfig(
            train_path= config['train_path'],
            test_path=config['test_path'],
            train_arr=config['train_arr'],
            test_arr=config['test_arr'],
            preprocessor_path=config['preprocessor_path']
        )
        
        return data_ingestion_config
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config['model_training']
        create_directories(config['root_dir'])
        create_directories(config['result_dir'])
        
        model_training_config = ModelTrainingConfig(
            model_path= config['model_path'],
            train_arr=config['train_arr'],
            test_arr=config['test_arr'],
            train_result=config['train_result'],
            test_result=config['test_result']
        )
        
        return model_training_config