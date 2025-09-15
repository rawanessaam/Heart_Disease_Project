
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# Load Model & Dataset
# ===============================
pipeline = joblib.load("Best_Pipeline.pkl")
df = pd.read_csv("heart.csv")

# ===============================
# Sidebar Navigation
# ===============================
st.sidebar.title("🔎 Options")
page = st.sidebar.radio("Go to:", ["Prediction", "Data Visualization"])

# ===============================
# Prediction Page
# ===============================
if page == "Prediction":
    st.title("❤️ Heart Disease Prediction App")
    st.write("Enter patient details and get prediction:")

    # --- Inputs ---
    age = st.number_input("Age", 20, 100, 50)
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 200, 120)
    chol = st.number_input("Cholesterol (chol)", 100, 600, 200)
    thalach = st.number_input("Max Heart Rate (thalach)", 70, 220, 150)
    oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.5, 1.0, step=0.1)

    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
    slope = st.selectbox("Slope", [1, 2, 3])
    thal = st.selectbox("Thalassemia (thal)", [1, 2, 3])
    ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3])
    exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])

    # --- Convert to DataFrame ---
    input_data = pd.DataFrame([{
        "age": age, "trestbps": trestbps, "chol": chol, "thalach": thalach,
        "oldpeak": oldpeak, "cp": cp, "restecg": restecg, "slope": slope,
        "thal": thal, "ca": ca, "exang": exang
    }])

    # --- Predict ---
    if st.button("Predict"):
        pred = pipeline.predict(input_data)[0]
        proba = pipeline.predict_proba(input_data)[0][1]
        if pred == 1:
            st.error(f"⚠️ High risk of heart disease (Probability: {proba:.2f})")
        else:
            st.success(f"✅ Low risk of heart disease (Probability: {proba:.2f})")

# ===============================
# Visualization Page
# ===============================
elif page == "Data Visualization":
    st.title("📊 Heart Disease Data Exploration")
    st.write("Explore trends and patterns in the dataset.")

    # --- Age distribution ---
    st.subheader("Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["age"], bins=20, kde=True, color="skyblue", ax=ax)
    st.pyplot(fig)

    # --- Cholesterol vs Target ---
    st.subheader("Cholesterol by Target (0 = No disease, 1 = Disease)")
    fig, ax = plt.subplots()
    sns.boxplot(x="target", y="chol", data=df, palette="Set2", ax=ax)
    st.pyplot(fig)

    # --- Max heart rate vs Target ---
    st.subheader("Max Heart Rate by Target")
    fig, ax = plt.subplots()
    sns.violinplot(x="target", y="thalach", data=df, palette="muted", ax=ax)
    st.pyplot(fig)

    # --- Correlation heatmap ---
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # --- Pie chart of Chest Pain Types ---
    st.subheader("Chest Pain Type Distribution")
    cp_counts = df["cp"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(cp_counts, labels=cp_counts.index, autopct="%1.1f%%", startangle=90)
    st.pyplot(fig)
