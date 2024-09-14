import os
import sys
import pandas as pd
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    raw_data_path: str=os.path.join("notebook\data", "Research_papers_data.csv")
    preprocessed_data_path: str=os.path.join('artifacts', "preprocessed_data.csv")

    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(self.ingestion_config.raw_data_path)
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.preprocessed_data_path), exist_ok=True)

            logging.info('Ingestion of the data is completed')

            return(
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    obj=DataIngestion()
    research_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    tfidf_weights_abs, tfidf_weights_title = data_transformation.initiate_data_transformation(research_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(tfidf_weights_abs, tfidf_weights_title))
    