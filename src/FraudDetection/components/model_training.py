from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from FraudDetection import logger
from FraudDetection.entity.config_entity import ModelTrainingConfig
from FraudDetection.utils.common import save_object, save_json
import numpy as np
import matplotlib.pyplot as plt
import os


class ModerTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.train_arr = config.train_arr
        self.test_arr = config.test_arr
        self.train_result = config.train_result
        self.test_result = config.test_result
        self.model_path = config.model_path
    
    def initiate_model_training(self):
        try:
            train_arr = np.load(self.train_arr)
            test_arr = np.load(self.test_arr)
            logger.info('Loading train and test set')

            X_train,y_train,X_test,y_test= (train_arr[:,:-1], train_arr[:,-1], test_arr[:,:-1], test_arr[:,-1])
            logger.info("Split training and test input data")

            #Model selection
            models = {
                "Random Forest": RandomForestClassifier(),
                "MLP": MLPClassifier(max_iter=1000),
                "AdaBoost": AdaBoostClassifier(),
                "XGBClassifier": XGBClassifier(),
            }

            logger.info('Model selection')

            #Hyperparameter selection
            params={
                "Random Forest":{
                    'n_estimators': [100, 200, 400],
                    'criterion': ['gini', 'entropy'],
                    'max_features': ['sqrt', 'log2'],
                },
                "MLP":{
                    'hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
                    'activation': ['tanh', 'relu'],
                    'solver': ['sgd', 'adam'],
                    'alpha': [0.0001, 0.05],
                    'learning_rate': ['constant','adaptive'],
                },
                "XGBClassifier":{
                    'learning_rate': [0.1, 0.01, 0.001],
                    'min_child_weight': [1, 5, 10],
                    'gamma': [0.5, 1, 1.5, 2, 5],
                },
                "AdaBoost":{
                    'learning_rate':[0.1, 0.01, 0.001],
                    'n_estimators': [50, 100, 200]
                }
            }

            logger.info('Hyperparameter tuning')

            #Cross validation
            cv = StratifiedKFold(n_splits=5, random_state=None, shuffle=False)

            #Evaluation
            report = {}
            test_result = {model: '' for model in models}
            train_result = {model: '' for model in models}
            
            for i in range(len(list(models))):
                model = list(models.values())[i]
                param= params[list(models.keys())[i]]
                gs = GridSearchCV(model, param, cv=cv, n_jobs=-1, scoring='f1_macro')
                gs.fit(X_train,y_train)

                model.set_params(**gs.best_params_)
                model.fit(X_train,y_train)

                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)

                cm = confusion_matrix(y_test, y_test_pred)
                disp = ConfusionMatrixDisplay(confusion_matrix=cm)
                disp.plot()
                plt.savefig(os.path.join('artifacts', 'results', f'{list(models.keys())[i]}.png'))
                
                train_report = classification_report(y_train, y_train_pred)
                train_result[list(models.keys())[i]] = train_report
                
                test_report = classification_report(y_test, y_test_pred)
                test_result[list(models.keys())[i]] = test_report

                test_score = f1_score(y_test, y_test_pred)
                report[list(models.keys())[i]] = test_score

            save_json(self.train_result, train_result)
            save_json(self.test_result, test_result)
            
            logger.info('Classification report for train set and test set')
            
            ## To get best model score from dict
            best_model_score = max(sorted(report.values()))
            print(best_model_score)

            ## To get best model name from dict
            best_model_name = list(report.keys())[list(report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score<0.8:
                print("No best model found")
            
            logger.info(f"Best found model on testing dataset")

            save_object(self.model_path, best_model)

            logger.info(f"Saving best found model on testing dataset")

        except Exception as e:
            raise e