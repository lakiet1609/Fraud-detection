import numpy as np 
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import  RobustScaler
from FraudDetection import logger
from imblearn.combine import SMOTEENN
from FraudDetection.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.train_path = config.train_path
        self.test_path = config.test_path
        self.train_arr = config.train_arr
        self.test_arr = config.test_arr
    
    def initiate_data_transformation(self):
        try:
            train_df = pd.read_csv(self.train_path)
            test_df = pd.read_csv(self.test_path)
            logger.info("Read train and test data completed")

            #Rescale the Amount and Time feature in the dataset
            rob_scaler = RobustScaler()
            train_df['scaled_amount'] = rob_scaler.fit_transform(train_df['Amount'].values.reshape(-1,1))
            train_df['scaled_time'] = rob_scaler.fit_transform(train_df['Time'].values.reshape(-1,1))
            scaled_amount = train_df['scaled_amount']
            scaled_time = train_df['scaled_time']
            train_df.drop(['scaled_amount', 'scaled_time'], axis=1, inplace=True)
            train_df.insert(0, 'scaled_amount', scaled_amount)
            train_df.insert(1, 'scaled_time', scaled_time)
            train_df = train_df.sample(frac=1)
            logger.info('Rescale the time and amount columns')

            #Remove outliers (Highest negative correlated with Class)
            target_column = 'Class'
            negative_corr_column = ['V14', 'V12', 'V10']
            for col in negative_corr_column:
                quantile_25 = train_df[col].loc[train_df[target_column] == 1].quantile(0.25)
                quantile_75 = train_df[col].loc[train_df[target_column] == 1].quantile(0.75)
                iqr = quantile_75 - quantile_25
                lower_limit = quantile_25 - iqr*1.5
                upper_limit = quantile_75 + iqr*1.5
                new_train_df = train_df.drop(train_df[(train_df[col] > upper_limit) | (train_df[col] < lower_limit)].index)
                train_df = new_train_df
            logger.info('Remove outliers for the feature having highest correlation with the target')

            input_feature_train_df= train_df.drop(columns=[target_column],axis=1)
            target_feature_train_df= train_df[target_column]

            # Random Over Sampling the dataset because of its imbalance
            smt = SMOTEENN()
            X_train_sampling, y_train_sampling = smt.fit_resample(input_feature_train_df, target_feature_train_df)
            logger.info('Random Over Sampling the dataset')

            input_feature_test_df=test_df.drop(columns=[target_column],axis=1)
            target_feature_test_df=test_df[target_column]

            train_arr = np.c_[X_train_sampling, np.array(y_train_sampling)]
            test_arr = np.c_[input_feature_test_df, np.array(target_feature_test_df)]

            np.save(self.train_arr, train_arr)
            np.save(self.test_arr, test_arr)
            logger.info('Save preprocessed train and test set')
            
            return train_arr, test_arr

        except Exception as e:
            raise e
        
        