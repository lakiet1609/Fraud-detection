import numpy as np 
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import  StandardScaler
from FraudDetection import logger
from FraudDetection.utils.common import save_object
from imblearn.combine import SMOTEENN
from FraudDetection.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.train_path = config.train_path
        self.test_path = config.test_path
        self.train_arr = config.train_arr
        self.test_arr = config.test_arr
        self.preprocessor_path = config.preprocessor_path
    
    def get_data_transformer_object(self):
        try:
            preprocessor = Pipeline(steps=[("scaler",StandardScaler())])
            return preprocessor
        except Exception as e:
            raise e
        
    def initiate_data_transformation(self):
        try:
            train_df = pd.read_csv(self.train_path)
            test_df = pd.read_csv(self.test_path)
            logger.info("Read train and test data completed")

            #Remove duplicates records
            train_df = train_df.drop_duplicates()
            logger.info('Remove duplicated records')

            #Rescale the Amount and Time feature in the dataset
            preprocessor = self.get_data_transformer_object()
            
            train_df['Time'] = preprocessor.fit_transform(train_df['Amount'].values.reshape(-1,1))
            train_df['Amount'] = preprocessor.fit_transform(train_df['Time'].values.reshape(-1,1))

            test_df['Time'] = preprocessor.transform(test_df['Amount'].values.reshape(-1,1))
            test_df['Amount'] = preprocessor.transform(test_df['Time'].values.reshape(-1,1))

            logger.info('Rescale the time and amount columns for train and test set')
            
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
            
            logger.info('Remove outliers for the feature having highest negative correlation with the target')

            input_feature_train_df= train_df.drop(columns=[target_column],axis=1)
            target_feature_train_df= train_df[target_column]

            # Random Over Sampling the dataset because of its imbalance
            smoteenn = SMOTEENN()
            X_train_sampling, y_train_sampling = smoteenn.fit_resample(input_feature_train_df, target_feature_train_df)
            
            logger.info('Over Sampler using SMOTEENN')

            input_feature_test_df=test_df.drop(columns=[target_column],axis=1)
            target_feature_test_df=test_df[target_column]

            train_arr = np.c_[X_train_sampling, np.array(y_train_sampling)]
            test_arr = np.c_[input_feature_test_df, np.array(target_feature_test_df)]
 
            np.save(self.train_arr, train_arr)
            np.save(self.test_arr, test_arr)
            logger.info('Save preprocessed train and test set')

            save_object(self.preprocessor_path, preprocessor)
            logger.info('Save preprocessor')
    
            return train_arr, test_arr

        except Exception as e:
            raise e
        
        