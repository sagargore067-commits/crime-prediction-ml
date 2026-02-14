import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI Crime Analytics Dashboard",
    page_icon="🚔",
    layout="wide"
)

# =============================
# Load Data & Model
# =============================
df = pd.read_csv("data/crime_data.csv")
model = joblib.load("models/trained_model.pkl")
le_state, le_district = joblib.load("models/label_encoders.pkl")

# =============================
# Sidebar
# =============================
st.sidebar.title("🔍 Controls")

state = st.sidebar.selectbox("Select State", le_state.classes_)
district = st.sidebar.selectbox("Select District", le_district.classes_)

min_year = int(df["Year"].min())
max_year = int(df["Year"].max())

if min_year == max_year:
    year = min_year
else:
    year = st.sidebar.slider("Select Year", min_year, max_year, min_year)

predict_button = st.sidebar.button("🚀 Predict Crime")

# =============================
# Title Section
# =============================
st.title("🚔 AI Crime Analytics Dashboard")
st.markdown("### Data-Driven Crime Trend & Prediction System")

# =============================
# KPI Metrics
# =============================
total_crimes = df["Total Cognizable IPC crimes"].sum()
avg_crimes = df["Total Cognizable IPC crimes"].mean()
max_state = df.groupby("States/UTs")["Total Cognizable IPC crimes"].sum().idxmax()

col1, col2, col3 = st.columns(3)

col1.metric("📊 Total Crimes", f"{int(total_crimes):,}")
col2.metric("📈 Average Crimes", f"{int(avg_crimes):,}")
col3.metric("🔥 Highest Crime State", max_state)

st.divider()

# =============================
# Graph Section
# =============================
col_left, col_right = st.columns(2)

# Crime Trend Graph
with col_left:
    st.subheader("📈 Crime Trend Over Years")

    yearly = df.groupby("Year")["Total Cognizable IPC crimes"].sum().sort_index()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(yearly.index, yearly.values, marker='o', linewidth=2)
    ax.set_title("Total IPC Crimes Over Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Crimes")
    ax.ticklabel_format(style='plain', axis='y')
    ax.grid(True, linestyle='--', alpha=0.6)

    st.pyplot(fig)

# Top States Graph
with col_right:
    st.subheader("🏆 Top 10 Crime States")

    top_states = (
        df.groupby("States/UTs")["Total Cognizable IPC crimes"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    top_states.plot(kind="bar", ax=ax2)
    ax2.set_xlabel("States")
    ax2.set_ylabel("Total Crimes")
    ax2.ticklabel_format(style='plain', axis='y')
    ax2.grid(axis="y", linestyle='--', alpha=0.6)

    st.pyplot(fig2)

st.divider()

# =============================
# Prediction Section
# =============================
st.subheader("🔮 Crime Prediction Result")

if predict_button:

    state_encoded = le_state.transform([state])[0]
    district_encoded = le_district.transform([district])[0]

    input_data = pd.DataFrame(
        [[state_encoded, district_encoded, year]],
        columns=["States/UTs", "District", "Year"]
    )

    prediction = model.predict(input_data)

    st.success(f"""
    ### 📌 Prediction Summary
    - **State:** {state}
    - **District:** {district}
    - **Year:** {year}
    - **Predicted Total IPC Crimes:** **{int(prediction[0]):,}**
    """)
