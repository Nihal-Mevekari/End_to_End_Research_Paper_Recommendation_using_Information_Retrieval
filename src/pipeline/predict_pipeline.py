import sys
import os
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        self.model_path: str = os.path.join("artifacts", "abstracts_model.pkl")
        self.tfidf_weights_abs_file_path: str = os.path.join('artifacts', 'tfidf_abstract_weights.pkl')
        self.tfidf_features_abs_file_path: str = os.path.join('artifacts', 'tfidf_abstract_features.pkl')
        self.preprocessed_data_path: str=os.path.join('artifacts', "preprocessed_data.csv")


    def get_top_features(self, rownum, weights, features, top_k=30):
        '''
        Function for returning the top_k features of an Abstract or Title
        '''
        #weights is a Sparse vector, hence need to convert into 2D matrix using toarray() function
        weight_vec = weights.toarray()[rownum,:]

        # weight_vec is tf-idf weight vector for particular row_num (abstract) 
        # where no. of columns = vocab size
        
        # We will sort this weight vector in decreasing order of the weights and will choose top_k weights
        top_idx = np.argsort(weight_vec)[::-1][:top_k]

        # We will return k-features which corresponds to the top_k weights
        return [features[i] for i in top_idx]


    def find_nearest_papers(self, row, kNNmodel, tfidf_weights, tfidf_features, papers):
        # Get the top_k features of an Abstract or Title
        keywords = self.get_top_features(row, tfidf_weights, tfidf_features)

        # Get the Nearest 10 neighbors (similar papers) using k-NN
        dist,idx = kNNmodel.kneighbors(tfidf_weights[row,:])

        # Suggest top most 5 similar papers
        idx = list(idx[0][1:6])

        return {'papers':papers.iloc[idx], 'keywords':keywords}

    def predict(self, query_paper_title):
        try:
            model = load_object(file_path=self.model_path)
            tfidf_weights_abs = load_object(file_path=self.tfidf_weights_abs_file_path)
            tfidf_features_abs = load_object(file_path=self.tfidf_features_abs_file_path)
            data = pd.read_csv(self.preprocessed_data_path)

            found = True
            query_paper_index = data.index[data['titles'] == query_paper_title].tolist()
            if not query_paper_index:
                found = False

            if found:
                return self.find_nearest_papers(query_paper_index[0], model, tfidf_weights_abs, tfidf_features_abs, data)
            else:
                return "Invalid search..Try again"
        
        except Exception as e:
            raise CustomException(e, sys)
