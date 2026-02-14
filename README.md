🚔 AI Crime Analytics & Prediction System Using Machine Learning
📌 Project Overview

This project implements a Machine Learning-based Crime Analytics and Prediction System using regression techniques. The objective of the system is to analyze historical Indian IPC crime data and predict total cognizable crimes based on location and year.

The system processes structured crime records at the state and district level to identify trends and generate predictive insights. A regression-based machine learning model was trained using encoded categorical features to simulate real-world crime forecasting scenarios.

Two major components were implemented:

📊 Crime Trend Analysis Dashboard

🔮 Crime Count Prediction using Random Forest Regression

Model performance was evaluated using:

R² Score (Coefficient of Determination)

In addition to model training and evaluation, the system includes an interactive Streamlit dashboard that allows users to:

Select State

Select District

Select Year

Generate real-time crime prediction

This project demonstrates a complete end-to-end machine learning workflow including data preprocessing, feature encoding, model training, evaluation, visualization, and deployment.

🖥️ Streamlit Dashboard

This project includes an interactive Streamlit-based dashboard (app/app.py) that allows users to:

View Crime Trend Over Years

Analyze Top 10 Crime States

View Key Metrics (Total Crimes, Average Crimes, Highest Crime State)

Generate Real-Time Crime Prediction

To run the dashboard locally:

Clone the repository:

git clone https://github.com/sagargore067-commits/crime-prediction-ml.git


Navigate to the project folder:

cd crime-prediction-ml


Install required dependencies:

pip install -r requirements.txt


Train the model:

python main.py


Run the application:

python -m streamlit run app/app.py

🎯 Problem Statement

Crime data is generated in large volumes across different states and districts in India.

Manual analysis of such large datasets is inefficient and does not provide predictive insights.

Law enforcement and policy planners require:

Trend analysis

Identification of high-risk regions

Predictive crime estimation

This project uses Machine Learning to analyze historical crime data and predict total IPC crimes based on geographical and temporal inputs.

📊 Dataset Details

The dataset contains structured crime records with the following features:

States/UTs

District

Year

Total Cognizable IPC Crimes (Target Variable)

The dataset represents state-wise and district-wise IPC crime statistics.

⚙️ Technologies Used

Python

Pandas

Matplotlib

Scikit-learn

Streamlit

Joblib

🧠 Machine Learning Model
Random Forest Regression

An ensemble-based regression model that:

Handles non-linear relationships

Works well with encoded categorical variables

Provides robust and stable predictions

Reduces overfitting compared to single decision trees

📈 Model Evaluation

Evaluation metric used:

R² Score (Coefficient of Determination)

The R² score indicates how well the model explains variance in crime data.

📊 Result Visualization

The dashboard includes:

📈 Line graph showing Crime Trend Over Years

🏆 Bar chart showing Top 10 Crime States

📊 KPI cards for summary statistics

🔮 Real-time crime prediction module

🖥️ System Functionality

The system allows users to:

Select State

Select District

Select Year

Predict total IPC crimes

The trained Random Forest model generates predicted crime count instantly.

📌 Conclusion

The project successfully demonstrates:

Data preprocessing and encoding

Machine Learning model training

Model evaluation

Interactive dashboard deployment

It showcases how Machine Learning can be used to extract insights from crime datasets and provide predictive analysis.

🔮 Future Improvements

Use multi-year dataset (2001–2020)

Integrate population and socio-economic features

Implement advanced models like XGBoost

Add India interactive heatmap

Deploy dashboard on cloud platform

Add real-time crime data integration

👨‍💻 Author

Sagar Gore
AI & Machine Learning Enthusiast