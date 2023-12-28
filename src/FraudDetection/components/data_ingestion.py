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

    def initiate_data_ingestion(self):
        logger.info('Entered the data ingestion method or component')
        try:
            df = pd.read_csv(self.root_dir)
            logger.info('Read the dataset as dataframe')

            # Choosing subsample for the dataset
            df = df.sample(frac=1)
            fraud_df = df.loc[df['Class'] == 1]
            non_fraud_df = df.loc[df['Class'] == 0][:5000]
            new_df = pd.concat([fraud_df, non_fraud_df])
            new_df = new_df.sample(frac=1, random_state=42)

            train_set, test_set = train_test_split(new_df, test_size=0.25, stratify=new_df['Class'], random_state=42)
            logger.info(r'Split 25% for the train and test set completed !')

            train_set.to_csv(self.train_path, index=False, header=True)
            test_set.to_csv(self.test_path, index=False, header=True)

            logger.info('Data ingestion is completed !')
            
        except Exception as e:
            raise e