import os
import sys
import re
import pandas as pd
import nltk
nltk.download('punkt')

from dataclasses import dataclass
from sklearn.feature_extraction.text import TfidfVectorizer

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    tfidf_weights_abs_file_path: str = os.path.join('artifacts', 'tfidf_abstract_weights.pkl')
    tfidf_weights_title_file_path: str = os.path.join('artifacts', 'tfidf_title_weights.pkl')
    tfidf_features_abs_file_path: str = os.path.join('artifacts', 'tfidf_abstract_features.pkl')
    tfidf_features_title_file_path: str = os.path.join('artifacts', 'tfidf_title_features.pkl')
    preprocessed_data_path: str=os.path.join('artifacts', "preprocessed_data.csv")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
            

    def clean_text(self, text):
        '''
        Function that cleans text by removing '\x0c' and '\n' characters as well as all non-alpha characters 
        and finally converts everything to lower case
        '''
        stop_words = ['\x0c', '\n']
        for i in stop_words:
            text.replace(i, ' ')
        clean_text = re.sub('[^a-zA-Z]+', ' ', text)
        return clean_text.lower()
  

    def tokenize_and_stem(self, text):
        '''
        Function that takes text, tokenizes it and returns list of stemmed tokens
        '''
        tokens = nltk.tokenize.word_tokenize(text)
        stemmer = nltk.stem.snowball.SnowballStemmer("english")
        return [i for i in [stemmer.stem(t) for t in tokens] if len(i) > 2]
    
        
    def initiate_data_transformation(self, research_data):
        '''
        Function that initiates the data transformation
        '''
        try:
            research_data = pd.read_csv(research_data)

            logging.info("Reading Researched data completed")

            #Remove duplicate data
            research_data.drop_duplicates(keep='first', inplace=True)
            logging.info("Removed duplicate data")

            # Create a column for cleaned Abstract and cleaned Title
            research_data['clean_abstract'] = research_data['abstracts'].apply(self.clean_text)
            research_data['clean_title'] = research_data['titles'].apply(self.clean_text)
            logging.info("Cleaned Abstracts and Titles")

            research_data.to_csv(self.data_transformation_config.preprocessed_data_path, index=False, header=True)
            logging.info("Saved the preprocessed data")

            # Create vectorizer for Abstracts, max_df is set to 0.5, we only want
            # to include terms that appear in less than 50% of the documents (i.e. rare terms)
            # we are selecting maximum 200,000 abstract features
            abstract_tfidf_vectorizer = TfidfVectorizer(max_df=0.5, min_df=1, max_features=200000, 
                                                        stop_words='english', use_idf=True, tokenizer=self.tokenize_and_stem)

            # Create vectorizer for Title, max_df is set to 0.5, we only want
            # to include terms that appear in less than 50% of the documents (i.e. rare terms)
            # we are selecting maximum 100,000 title features
            title_tfidf_vectorizer = TfidfVectorizer(max_df=0.5, min_df=1, max_features=100000,
                                                     stop_words='english', use_idf=True, tokenizer=self.tokenize_and_stem)


            # Compute TF-IDF weights for Abstracts and Title
            tfidf_weights_abs = abstract_tfidf_vectorizer.fit_transform(research_data['clean_abstract'])
            tfidf_weights_title = title_tfidf_vectorizer.fit_transform(research_data['clean_title'])
            logging.info("Computed TF-IDF weights for Abstracts and Titles")

            # Get feature names for Abstract and Title models
            tfidf_features_abs = abstract_tfidf_vectorizer.get_feature_names_out()
            tfidf_features_title = title_tfidf_vectorizer.get_feature_names_out()
            logging.info("Extracted feature names for Abstract and Title models")

            save_object(
                file_path=self.data_transformation_config.tfidf_weights_abs_file_path,
                obj=tfidf_weights_abs
            )
            logging.info("Saved TF-IDF weights computed using Abstracts")

            save_object(
                file_path=self.data_transformation_config.tfidf_weights_title_file_path,
                obj=tfidf_weights_title
            )
            logging.info("Saved TF-IDF weights computed using Titles")

            save_object(
                file_path=self.data_transformation_config.tfidf_features_abs_file_path,
                obj=tfidf_features_abs
            )
            logging.info("Saved feature names extracted from Abstracts")

            save_object(
                file_path=self.data_transformation_config.tfidf_features_title_file_path,
                obj=tfidf_features_title
            )
            logging.info("Saved feature names extracted from Titles")

            return (
                tfidf_weights_abs,
                tfidf_weights_title
            )
        except Exception as e:
            raise CustomException(e, sys)