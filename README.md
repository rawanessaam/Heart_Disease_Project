#❤️ Heart Disease Prediction App
<h2>📌 Overview</h2>

This project is a Machine Learning web application built with Streamlit that predicts whether a patient is at risk of heart disease.

We applied both supervised and unsupervised learning:

Supervised models → Logistic Regression, Decision Tree, Random Forest, SVM

Unsupervised models → K-Means Clustering, Hierarchical Clustering

After tuning and evaluation, Logistic Regression was selected as the best-performing model and deployed with Streamlit.

🚀 Features

✅ Predict heart disease risk from patient details (Logistic Regression model)
✅ Probability score for risk level
✅ Interactive data visualizations (age distribution, cholesterol levels, correlations, etc.)
✅ Explore clustering insights (unsupervised learning)
✅ Simple web interface built with Streamlit

🧠 Machine Learning Workflow

Data Preprocessing

Encoding categorical features

Standardizing numerical features

Feature selection

Supervised Learning

Models: Logistic Regression, Decision Tree, Random Forest, SVM

Hyperparameter tuning: GridSearchCV & RandomizedSearchCV

Best Model → Logistic Regression

Unsupervised Learning

K-Means Clustering (elbow method for K)

Hierarchical Clustering (dendrogram analysis)

Compared clusters with true labels

Deployment

Full pipeline (preprocessing + model) saved as Best_Pipeline.pkl

Interactive app built with Streamlit

📊 Dataset

Dataset: Heart Disease UCI Dataset

Features:

Age, cholesterol, blood pressure, max heart rate, chest pain type, exercise-induced angina, number of major vessels, etc.

Target:

0 → No heart disease

1 → Heart disease

🖥️ How to Run Locally
1. Clone the repo
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction

2. Install requirements
pip install -r requirements.txt

3. Run the app
streamlit run app.py

📂 Project Structure
heart-disease-prediction/
│── app.py                 # Streamlit app
│── Best_Pipeline.pkl      # Trained ML pipeline (Logistic Regression)
│── heart.csv              # Dataset
│── notebooks/             # Jupyter notebooks (EDA, supervised, unsupervised)
│── requirements.txt       # Dependencies
│── README.md              # Project documentation

📸 Screenshots

Add some screenshots of your app interface and visualizations here.

🔮 Future Improvements

Add bulk CSV upload for multiple patients

Add clustering visualization page in the app (show K-Means groups)

Deploy on Streamlit Cloud / Hugging Face Spaces

Try advanced ML models (XGBoost, Neural Nets)

👩‍💻 Author

Rawan Essam
📌 AI & Machine Learning Enthusiast | Competitive Programmer
🔗 LinkedIn
 | GitHub
