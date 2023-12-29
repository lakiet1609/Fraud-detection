from FraudDetection.config.configuration import ConfigurationManager
from FraudDetection.components.model_training import ModerTraining
from FraudDetection import logger

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
        # STAGE 3
        logger.info(f">>>>>> {STAGE_3} started <<<<<<")
        training = ModelTraingPipeline()
        training.training_data()
        logger.info(f">>>>>> {STAGE_3} completed <<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e