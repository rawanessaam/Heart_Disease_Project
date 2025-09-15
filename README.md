<h1 style="text-align:center; color:#e63946;">❤️ Heart Disease Prediction App</h1>

<h2>📌 Overview</h2>
<p>
This project is a <b>Machine Learning web application</b> built with <b>Streamlit</b> that predicts whether a patient is at risk of heart disease.  
We applied both <b>supervised</b> and <b>unsupervised learning</b>:
</p>
<ul>
  <li><b>Supervised models</b> → Logistic Regression, Decision Tree, Random Forest, SVM</li>
  <li><b>Unsupervised models</b> → K-Means Clustering, Hierarchical Clustering</li>
</ul>
<p>
After tuning and evaluation, <b>Logistic Regression</b> was selected as the best-performing model and deployed with Streamlit.
</p>

<h2>🚀 Features</h2>
<ul>
  <li>✅ Predict heart disease risk from patient details (Logistic Regression model)</li>
  <li>✅ Probability score for risk level</li>
  <li>✅ Interactive data visualizations (age distribution, cholesterol levels, correlations, etc.)</li>
  <li>✅ Explore clustering insights (unsupervised learning)</li>
  <li>✅ Simple web interface built with <b>Streamlit</b></li>
</ul>

<h2>🧠 Machine Learning Workflow</h2>
<ol>
  <li><b>Data Preprocessing</b>: Encoding categorical features, scaling numeric features, feature selection</li>
  <li><b>Supervised Learning</b>: Logistic Regression, Decision Tree, Random Forest, SVM → tuned with GridSearchCV & RandomizedSearchCV → Best model: Logistic Regression</li>
  <li><b>Unsupervised Learning</b>: K-Means (elbow method), Hierarchical clustering (dendrogram), compared clusters with labels</li>
  <li><b>Deployment</b>: Full pipeline (preprocessing + model) saved as <code>Best_Pipeline.pkl</code>, deployed with Streamlit</li>
</ol>

<h2>📊 Dataset</h2>
<p>
Dataset: <b>Heart Disease UCI Dataset</b><br>
<b>Features:</b> age, cholesterol, blood pressure, max heart rate, chest pain type, exercise-induced angina, number of major vessels, etc.<br>
<b>Target:</b>
<ul>
  <li>0 → No heart disease</li>
  <li>1 → Heart disease</li>
</ul>
</p>

<h2>🖥️ How to Run Locally</h2>
<pre>
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction

pip install -r requirements.txt

streamlit run app.py
</pre>

<h2>📂 Project Structure</h2>
<pre>
heart-disease-prediction/
│── app.py                 # Streamlit app
│── Best_Pipeline.pkl      # Trained ML pipeline (Logistic Regression)
│── heart.csv              # Dataset
│── notebooks/             # Jupyter notebooks (EDA, supervised, unsupervised)
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
</pre>

<h2>📸 Screenshots</h2>
<p><i>Add some screenshots of your app interface and visualizations here.</i></p>

<h2>🔮 Future Improvements</h2>
<ul>
  <li>Add <b>bulk CSV upload</b> for multiple patients</li>
  <li>Add <b>clustering visualization</b> page in the app (K-Means groups)</li>
  <li>Deploy on <b>Streamlit Cloud / Hugging Face Spaces</b></li>
  <li>Try <b>advanced ML models</b> (XGBoost, Neural Nets)</li>
</ul>

<h2>👩‍💻 Authors</h2>
<p>
<b>Rawan Essam</b><br>
AI & Machine Learning Enthusiast | Competitive Programmer<br>
🔗 <a href="https://linkedin.com/in/your-profile">LinkedIn</a> | 
<a href="https://github.com/your-username">GitHub</a>
</p>

<p>
<b>Mohammed Saied</b><br>
Machine Learning Developer | Data Science Enthusiast<br>
🔗 <a href="https://linkedin.com/in/mohammed-profile">LinkedIn</a> | 
<a href="https://github.com/mohammed-username">GitHub</a>
</p>
