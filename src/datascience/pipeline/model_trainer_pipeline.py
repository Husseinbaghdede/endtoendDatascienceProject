from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger


STAGE_NAME= "Model trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        trainer_config = config.get_model_trainer_config()
        trainer = ModelTrainer(config=trainer_config)
        trainer.train()