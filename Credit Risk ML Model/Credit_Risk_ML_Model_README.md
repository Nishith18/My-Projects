Project Name: Credit Risk Prediction

Description: 

This project investigates the effectiveness of different machine learning models for predicting credit card defaults. Two data resampling techniques, SMOTE and SMOTEENN, are employed to address the issue of imbalanced data. Five machine learning models are evaluated: Logistic Regression, KNN, Random Forest, AdaBoost, and XGBoost.

Business Question:
To identify the most effective machine learning model for predicting credit card defaults, considering both accuracy and recall.

Methodology:

Data Preprocessing: Import and clean the credit card dataset.
Data Imbalance Handling: Apply SMOTE and SMOTEENN resampling techniques to address imbalanced data.
Model Training: Train five machine learning models (Logistic Regression, KNN, Random Forest, AdaBoost, and XGBoost) using the preprocessed data.
Model Evaluation: Evaluate each model using accuracy and recall metrics.

Key Findings:

XGBoost, when paired with SMOTE, consistently outperforms other models in overall accuracy.
In risk-averse banking contexts, AdaBoost, enhanced by SMOTEENN resampling, demonstrates superior recall and F1 scores.

Recommendations:

Implement AdaBoost with SMOTEENN resampling for accurate and effective credit card default prediction.
Continuously monitor model performance and retrain as needed.
Consider incorporating additional features for more refined risk assessment.

Technical Notes:

The project utilizes the following Python libraries:
pandas: For data manipulation and analysis
sklearn: For machine learning tasks
imbalanced-learn: For data resampling

Data Sources:

Credit card dataset from the University of Edinburgh
