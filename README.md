# 🚔 AI Crime Analytics & Prediction System Using Machine Learning

## 📌 Project Overview

This project implements a Machine Learning-based Crime Analytics and Prediction System using regression techniques.  
The primary objective is to analyze historical Indian IPC crime data and predict total cognizable crimes based on geographical and temporal inputs.
The system processes structured state-wise and district-wise crime records to identify trends and generate predictive insights. A regression-based machine learning model was trained using encoded categorical features to simulate real-world crime forecasting scenarios.
---

## 🎥 Live Project Demonstration

A complete walkthrough of the AI Crime Analytics Dashboard is available below:

▶ **Watch Demo Video:**  
[Click here to watch the demo](demo-video.mp4)

### The demonstration includes:

- 📊 Data visualization dashboard  
- 📈 Crime trend analysis  
- 🤖 Model training process  
- 🔮 Real-time prediction workflow  
- 🏗️ System architecture explanation  


### 🔹 Key Components

- 📊 Crime Trend Analysis Dashboard  
- 🔮 Crime Count Prediction using Random Forest Regression  

### 🔹 Model Evaluation Metric

- R² Score (Coefficient of Determination)

The project demonstrates a complete end-to-end machine learning workflow including:

- Data preprocessing  
- Feature encoding  
- Model training  
- Model evaluation  
- Data visualization  
- Interactive deployment using Streamlit  

---

## 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit-based dashboard (`app/app.py`) that allows users to:

- View Crime Trend Over Years  
- Analyze Top 10 Crime States  
- View Key Performance Metrics (Total Crimes, Average Crimes, Highest Crime State)  
- Generate Real-Time Crime Predictions  

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sagargore067-commits/crime-prediction-ml.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd crime-prediction-ml
```

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train the Model

```bash
python main.py
```

### 5️⃣ Run the Streamlit Application

```bash
python -m streamlit run app/app.py
```

---

## 🎯 Problem Statement

Crime data is generated in large volumes across different states and districts in India.  

Manual analysis of such large datasets is inefficient and does not provide predictive insights.  

Law enforcement agencies and policymakers require:

- Accurate trend analysis  
- Identification of high-risk regions  
- Predictive crime estimation  

This project applies Machine Learning techniques to analyze historical crime data and generate predictive insights for improved decision-making.

---

## 📊 Dataset Details

The dataset contains structured IPC crime records with the following features:

- States/UTs  
- District  
- Year  
- Total Cognizable IPC Crimes (Target Variable)  

The dataset represents official state-wise and district-wise crime statistics.

---

## ⚙️ Technologies Used

- Python  
- Pandas  
- Matplotlib  
- Scikit-learn  
- Streamlit  
- Joblib  

---

## 🧠 Machine Learning Model

### Random Forest Regression

An ensemble-based regression algorithm that:

- Handles non-linear relationships  
- Performs well with encoded categorical variables  
- Provides stable and reliable predictions  
- Reduces overfitting compared to single decision trees  

---

## 📈 Model Evaluation

Evaluation Metric Used:

- **R² Score (Coefficient of Determination)**  

The R² score measures how effectively the model explains variance in the target variable.

---

## 📊 Result Visualization

The dashboard includes:

- 📈 Line graph for Crime Trend Over Years  
- 🏆 Bar chart for Top 10 Crime States  
- 📊 KPI summary metrics  
- 🔮 Real-time crime prediction module  

---

## 🖥️ System Functionality

Users can:

- Select State  
- Select District  
- Select Year  
- Generate predicted total IPC crime count  

The trained Random Forest model produces real-time predictions instantly.

---

## 📌 Conclusion

The project successfully demonstrates:

- Data preprocessing and encoding  
- Machine learning model training  
- Model evaluation using regression metrics  
- Deployment of an interactive analytics dashboard  

It highlights how Machine Learning can be leveraged for crime data analysis and predictive modeling.

---

## 🔮 Future Improvements

- Integrate multi-year dataset (2001–2020)  
- Incorporate socio-economic and population features  
- Implement advanced models such as XGBoost  
- Add interactive India heatmap visualization  
- Deploy the dashboard on a cloud platform  
- Integrate real-time crime reporting systems  

---

## 👨‍💻 Author

**Sagar Gore**  
AI & Machine Learning Enthusiast
