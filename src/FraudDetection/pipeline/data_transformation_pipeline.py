from FraudDetection.components.data_transformation import DataTransformation
from FraudDetection.config.configuration import ConfigurationManager
from FraudDetection import logger

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
        #STAGE 2
        logger.info(f">>>>>> {STAGE_2} started <<<<<<")
        transformation = DataTransformationPipeline()
        train_arr, test_arr = transformation.transform_data()
        logger.info(f">>>>>> {STAGE_2} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e