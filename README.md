# FRAUDULENT TRANSACTION PREDICTION

At this project, I will deploy end to end fraudulen transaction classification.

Steps including in this projects:
- Project template create
- Requirements and project set-up
- Data ingestion
- Data transformation
- Model training
- Custom prediction
- Data version controlling (DVC)
- Deployment and user app
- Dockerization and AWS CICD pipeline

1. Project Template
- Including: template.py
- Setting up all necessary files and folders

2. Requirements and project setup
- Including: requirements.txt, setup.py, logger
- Create logger files
- Set up necassary dependancies and packages

3. Data ingestion
- Including: config/config.yaml, components/data_ingestion.py, pipeline/data_ingestion_pipeline.py
- Download dataset from google drive
- Extract the downloaded zip file
- Train test split the dataset into 2 csv files

4. Data transformation
- Including: config/config.yaml, components/data_transformation.py, pipeline/data_transformation_pipeline.py
- Drop duplicates
- Rescale the Time and Amount feature using StandardScaler
- Remove outliers
- Oversampling the dataset 
- Save the results

5. Model Training
-  Including: config/config.yaml, components/model_training.py, pipeline/model_training_pipeline.py
- Load previous result
- Split to X_train,y_train,X_test,y_test
- Model selection
- Stratified cross validation
- Hyperparameter tuning
- Evaluating on training set and testing set
- Saving the evaluation
- Saving the best results and models

6. Custom prediction
- Including: pipeline/predict_pipeline.py
- Loading best model
- Loading preprocessor
- Transform for custom features
- Predict custom features by best models

7. Data version controlling (DVC)
- Including: dvc.yaml
- Write stages for 3 principal processes

8. Deployment and user app
- Including: app.py, templates/index.html, templates/home.html
- Deploy custom prediction using Flask api
- Write frontend web using HTML

![Screenshot 2023-12-29 170607](https://github.com/lakiet1609/Fraud-detection/assets/116550803/0b0c09a5-97ca-48d6-b916-beec8482bc0f)

![Screenshot 2023-12-29 170621](https://github.com/lakiet1609/Fraud-detection/assets/116550803/a05536d1-95d1-42e9-ad7a-22e6f96e8d55)

9. Dokerization and AWS CICD pipeline
- Including: Dockerfile, .github/workflows/main.yaml
- Building docker container
- Building CICD delpoyment pipeline using AWS:
    - Create IAM user
    - Create ECR repo
    - Create ECR machine
    - Install docker in EC2 Machine
    - Configure EC2 as self-hosted runner
    - Setup github secrets

![aws](https://github.com/lakiet1609/Fraud-detection/assets/116550803/e1b789f9-66f1-4734-b046-25b108a80186)

![Screenshot 2023-12-29 170346](https://github.com/lakiet1609/Fraud-detection/assets/116550803/ab6ce753-33df-4f12-aeb6-f1e91eb7c546)