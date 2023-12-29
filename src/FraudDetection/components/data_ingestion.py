import pandas as pd
from sklearn.model_selection import train_test_split
from FraudDetection import logger
from FraudDetection.entity.config_entity import DataIngestionCongfig
from pathlib import Path
import gdown
import os
import zipfile

class DataIngestion:
    def __init__(self, config: DataIngestionCongfig):
        self.source_url = config.source_url
        self.local_data_file = config.local_data_file
        self.unzip_dir = config.unzip_dir
        self.data_path = config.data_path
        self.train_path = config.train_path
        self.test_path = config.test_path
    
    def download_file(self)-> str:
        try: 
            dataset_url = self.source_url
            zip_download_dir = self.local_data_file
            os.makedirs("artifacts/data", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        unzip_path = self.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info('Extracted zip file completed')

    def initiate_data_ingestion(self):
        logger.info('Entered the data ingestion method or component')
        try:
            df = pd.read_csv(self.data_path)
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