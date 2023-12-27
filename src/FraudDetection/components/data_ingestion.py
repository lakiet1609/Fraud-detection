import pandas as pd
from sklearn.model_selection import train_test_split
from FraudDetection import logger
from FraudDetection.entity.config_entity import DataIngestionCongfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionCongfig):
        self.root_dir = config.root_dir
        self.train_path = config.train_path
        self.test_path = config.test_path
        self.validation_path = config.validation_path

    def initiate_data_ingestion(self):
        logger.info('Entered the data ingestion method or component')
        try:
            df = pd.read_csv(self.root_dir)
            logger.info('Read the dataset as dataframe')

            #Split the data into 90% for train and test 10% for validate
            dataset, validate_set = train_test_split(df, test_size=0.2, stratify=df['Class'], random_state=42)
            logger.info(r'Split 20% for the validation set completed !')

            validate_set.to_csv(self.validation_path, index=False, header=True)

            #Split the dataset into train set and test set
            train_set, test_set = train_test_split(dataset, test_size=0.25, stratify=dataset['Class'], random_state=42)
            
            train_set.to_csv(self.train_path, index=False, header=True)
            test_set.to_csv(self.test_path, index=False, header=True)

            logger.info('Data ingestion is completed !')
            
        except Exception as e:
            raise e