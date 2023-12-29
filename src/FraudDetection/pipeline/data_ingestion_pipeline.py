from FraudDetection.config.configuration import ConfigurationManager
from FraudDetection.components.data_ingestion import DataIngestion
from FraudDetection import logger

STAGE_1 = 'Data Ingestion stage'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def ingest_data(self):
        config = ConfigurationManager().get_data_ingestion_config()
        data_ingestion = DataIngestion(config=config)
        data_ingestion.initiate_data_ingestion()

if __name__ == '__main__':
    try:
        #STAGE 1
        logger.info(f">>>>>> {STAGE_1} started <<<<<<")
        ingestion = DataIngestionPipeline()
        ingestion.ingest_data()
        logger.info(f">>>>>> {STAGE_1} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e