from FraudDetection.config.configuration import ConfigurationManager
from FraudDetection.components.data_ingestion import DataIngestion
from FraudDetection.components.data_transformation import DataTransformation
from FraudDetection.components.model_training import ModerTraining
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


STAGE_3 = 'Model training stage'

class ModelTraingPipeline:
    def __init__(self):
        pass

    def training_data(self):
        config = ConfigurationManager().get_model_training_config()
        data_training = ModerTraining(config=config)
        data_training.initiate_model_training()


if __name__ == '__main__':
    try:
        #STAGE 1
        logger.info(f">>>>>> {STAGE_1} started <<<<<<")
        ingestion = DataIngestionPipeline()
        ingestion.ingest_data()
        logger.info(f">>>>>> {STAGE_1} completed <<<<<<")

        #STAGE 2
        logger.info(f">>>>>> {STAGE_2} started <<<<<<")
        transformation = DataTransformationPipeline()
        train_arr, test_arr = transformation.transform_data()
        logger.info(f">>>>>> {STAGE_2} completed <<<<<<")

        # STAGE 3
        logger.info(f">>>>>> {STAGE_3} started <<<<<<")
        training = ModelTraingPipeline()
        training.training_data()
        logger.info(f">>>>>> {STAGE_3} completed <<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e