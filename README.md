# 🚔 AI Crime Analytics & Prediction System  
### Machine Learning-Based Crime Forecasting Dashboard

---

## 📌 Project Overview

The **AI Crime Analytics & Prediction System** is a Machine Learning-based application designed to analyze historical Indian IPC crime data and generate predictive insights.

The system processes structured state-wise and district-wise crime records to:

- Identify long-term crime trends  
- Highlight high-crime regions  
- Predict total cognizable IPC crimes  
- Provide interactive visual analytics  

A regression-based machine learning model was trained using encoded categorical features to simulate real-world crime forecasting scenarios.

This project demonstrates a complete end-to-end ML workflow including:

- Data preprocessing  
- Feature encoding  
- Model training  
- Model evaluation  
- Interactive dashboard deployment  
---

## 🎬 Live Project Demonstration

<p align="center">
  <a href="https://youtu.be/tid0rBbhpek" target="_blank">
    <img src="https://img.youtube.com/vi/tid0rBbhpek/maxresdefault.jpg" 
         alt="AI Crime Analytics Dashboard Demo" 
         width="800">
  </a>
</p>

<p align="center">
  ▶ <strong>Click the image above to watch the complete project demonstration.</strong>
</p>

---

### 📌 The Demonstration Covers:

- 📊 Interactive Streamlit-based crime analytics dashboard  
- 📈 Crime trend visualization across years  
- 🏆 Top 10 high-crime states analysis  
- 🤖 Machine learning model training (Random Forest Regression)  
- 🔮 Real-time crime prediction based on state, district & year  
- 🏗️ System architecture and workflow explanation  

---

### 🎥 Direct Video Link

👉 https://youtu.be/tid0rBbhpek


---

## 🎯 Problem Statement

Crime data is generated in large volumes across different states and districts in India.  

Manual analysis of such large datasets is inefficient and does not provide predictive insights.

Law enforcement agencies and policymakers require:

- Trend analysis  
- Identification of high-risk regions  
- Predictive crime estimation  

This project applies Machine Learning to analyze historical crime data and generate actionable predictive insights.

---

## 📊 Dataset Details

The dataset contains structured IPC crime records with the following features:

- `States/UTs`
- `District`
- `Year`
- `Total Cognizable IPC Crimes` (Target Variable)

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

An ensemble-based regression model selected because it:

- Handles non-linear relationships  
- Performs well with encoded categorical variables  
- Provides stable and accurate predictions  
- Reduces overfitting compared to individual decision trees  

---

## 📈 Model Evaluation

Evaluation metric used:

- **R² Score (Coefficient of Determination)**  

The R² score measures how effectively the model explains variance in the target variable.

---

## 📊 Dashboard Features

The interactive dashboard provides:

- 📈 Crime Trend Over Years (Line Chart)  
- 🏆 Top 10 Crime States (Bar Chart)  
- 📊 KPI Summary Metrics  
  - Total Crimes  
  - Average Crimes  
  - Highest Crime State  
- 🔮 Real-Time Crime Prediction Module  

---

## 🖥️ System Functionality

Users can:

1. Select State  
2. Select District  
3. Select Year  
4. Generate predicted total IPC crime count  

The trained Random Forest model instantly produces real-time predictions.

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sagargore067-commits/crime-prediction-ml.git
```

### 2️⃣ Navigate to Project Directory

```bash
cd crime-prediction-ml
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train the Model

```bash
python main.py
```

### 5️⃣ Launch the Dashboard

```bash
python -m streamlit run app/app.py
```

---

## 📂 Project Structure

```
crime-prediction-ml/
│
├── app/                # Streamlit dashboard
├── src/                # Model training & preprocessing
├── data/               # Crime dataset
├── notebooks/          # Exploratory data analysis
├── models/             # Trained model files
├── README.md
├── requirements.txt
└── main.py
```

---

## 📌 Conclusion

This project successfully demonstrates:

- Data preprocessing and encoding  
- Machine learning model training  
- Model evaluation  
- Deployment of an interactive analytics dashboard  

It highlights how Machine Learning can be leveraged to extract insights from crime datasets and assist in predictive decision-making.

---

## 🔮 Future Enhancements

- Integrate multi-year dataset (2001–2020)  
- Add socio-economic and population-based features  
- Implement advanced models such as XGBoost  
- Add interactive India heatmap visualization  
- Deploy dashboard on cloud platform  
- Integrate real-time crime data APIs  

---

## 👨‍💻 Author

**Sagar Gore**  
AI & Machine Learning Enthusiast  
