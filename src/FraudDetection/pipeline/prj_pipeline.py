from FraudDetection.config.configuration import ConfigurationManager
from FraudDetection.components.data_ingestion import DataIngestion
from FraudDetection.components.data_transformation import DataTransformation
from FraudDetection import logger


STAGE_1 = 'Data Ingestion stage'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def ingest_data(self):
        config = ConfigurationManager().get_data_ingestion_config()
        data_ingestion = DataIngestion(config=config)
        data_ingestion.initiate_data_ingestion()


STAGE_2 = 'Data Transformation stage'

class DataTransformationPipeline:
    def __init__(self):
        pass

    def transform_data(self):
        config = ConfigurationManager().get_data_transformation_config()
        data_transformation = DataTransformation(config=config)
        train_arr, test_arr = data_transformation.initiate_data_transformation()
        return train_arr, test_arr


if __name__ == '__main__':
    try:
        # #STAGE 1
        # logger.info(f">>>>>> {STAGE_1} started <<<<<<")
        # ingestion = DataIngestionPipeline()
        # ingestion.ingest_data()
        # logger.info(f">>>>>> {STAGE_1} completed <<<<<<")

        #STAGE 2
        logger.info(f">>>>>> {STAGE_2} started <<<<<<")
        transformation = DataTransformationPipeline()
        train_arr, test_arr = transformation.transform_data()
        logger.info(f">>>>>> {STAGE_2} completed <<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e