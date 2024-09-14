import os
import sys
from dataclasses import dataclass
from sklearn.neighbors import NearestNeighbors

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_abstracts_model_file_path: str=os.path.join("artifacts", "abstracts_model.pkl")
    trained_titles_model_file_path: str=os.path.join("artifacts", "titles_model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self, tfidf_weights_abs, tfidf_weights_title):
        '''
        Function that initiates the Model training
        '''
        try:
            # Create the k-NN model using k=10
            nn_abs = NearestNeighbors(n_neighbors=10, algorithm='auto')
            nn_title = NearestNeighbors(n_neighbors=10, algorithm='auto')
            logging.info("Created k-NN models for both Abstract and Title similarity")

            # Fit the models to the TF-IDF weights matrix
            nn_fitted_abs = nn_abs.fit(tfidf_weights_abs)
            nn_fitted_title = nn_title.fit(tfidf_weights_title)
            logging.info("Trained the models for both Abstract and Title similarity")

            save_object(
                file_path=self.model_trainer_config.trained_abstracts_model_file_path,
                obj=nn_fitted_abs
            )
            logging.info("Saved the Abstracts model")

            save_object(
                file_path=self.model_trainer_config.trained_titles_model_file_path,
                obj=nn_fitted_title
            )
            logging.info("Saved the Titles model")


        except Exception as e:
            raise CustomException(e, sys)