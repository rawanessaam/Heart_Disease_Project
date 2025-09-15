<h1 style="text-align:center; color:#d62828;">❤️ Heart Disease Prediction App</h1>

<h2>📌 Overview</h2>
<p>
This project is a <b>machine learning web app</b> that predicts whether a person is at risk of heart disease.  
We started with the UCI Heart Disease dataset, performed <b>data cleaning, feature selection, PCA, supervised and unsupervised modeling</b>,  
and finally deployed our best model using <b>Streamlit + Ngrok</b>.  
</p>

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

<h2>🔧 What We Did</h2>

<h3>1. Data Preprocessing & Cleaning</h3>
<p>
We loaded the dataset into Pandas, handled missing values, encoded categorical features using One-Hot Encoding,  
and standardized numerical features with StandardScaler.  
We also explored the dataset visually with histograms, boxplots, and correlation heatmaps.  
<b>Result:</b> a clean, ready-to-use dataset.
</p>

<h3>2. Dimensionality Reduction (PCA)</h3>
<p>
To simplify the dataset and reduce noise, we applied <b>Principal Component Analysis (PCA)</b>.  
We checked how much variance each component explained and chose the number of components that gave a good balance.  
<b>Result:</b> PCA-transformed dataset + variance visualization.
</p>

<h3>3. Feature Selection</h3>
<p>
We didn’t just rely on PCA — we also wanted to know which features mattered most.  
Using <b>Random Forest feature importance</b>, <b>Recursive Feature Elimination (RFE)</b>, and <b>Chi-Square tests</b>,  
we ranked features and picked the most important ones for modeling.  
<b>Result:</b> smaller dataset with only the strongest predictors.
</p>

<h3>4. Supervised Learning</h3>
<p>
We trained several classification models:
<ul>
  <li>Logistic Regression</li>
  <li>Decision Tree</li>
  <li>Random Forest</li>
  <li>Support Vector Machine (SVM)</li>
</ul>
We compared them using accuracy, precision, recall, F1-score, and ROC-AUC.  
<b>Best performer:</b> Logistic Regression after tuning.
</p>

<h3>5. Unsupervised Learning</h3>
<p>
We also explored clustering to see how patients group together.  
Using <b>K-Means (with the elbow method)</b> and <b>Hierarchical Clustering (dendrograms)</b>,  
we found clusters and compared them with the actual disease labels.  
<b>Result:</b> interesting insights about natural patient groupings.
</p>

<h3>6. Hyperparameter Tuning</h3>
<p>
We optimized our models with <b>GridSearchCV</b> and <b>RandomizedSearchCV</b>.  
This step fine-tuned parameters like regularization (C) in Logistic Regression and depth in Decision Trees.  
<b>Result:</b> Logistic Regression tuned to the best performance.
</p>

<h3>7. Model Export</h3>
<p>
We bundled preprocessing + model into one <b>scikit-learn pipeline</b> and saved it as <code>Best_Pipeline.pkl</code>.  
This ensures reproducibility and makes deployment easier.  
</p>

<h3>8. Streamlit Web App</h3>
<p>
We built a simple UI where users can:
<ul>
  <li>Enter health details (age, cholesterol, chest pain type, etc.)</li>
  <li>Get a prediction + probability of having heart disease</li>
  <li>Explore visualizations (age distribution, cholesterol vs. target, heatmaps, etc.)</li>
</ul>
<b>Result:</b> a user-friendly heart disease prediction app.
</p>

<h3>9. Deployment with Ngrok</h3>
<p>
Since we worked in Google Colab, we used <b>Ngrok</b> to expose the Streamlit app publicly.  
This allowed anyone to access the app via a shareable link.  
<b>Result:</b> live demo link of the model in action.
</p>

<h2>👩‍💻 Authors</h2>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px;">

  

  <div style="flex: 0 1 250px; text-align:center; border:1px solid #ddd; padding:15px; border-radius:10px;">
    <h3 style="color:#457b9d;">Mohammed Saied</h3>
    <p>AI & Machine Learning Enthusiast</p>
    <p>
      🔗 <a href="www.linkedin.com/in/mohammed-sai3ed">LinkedIn</a> | 
      <a href="https://github.com/Mohammed-Sai3ed">GitHub</a>
    </p>
  </div>
<div style="flex: 0 1 250px; text-align:center; border:1px solid #ddd; padding:15px; border-radius:10px;">
    <h3 style="color:#457b9d;">Rawan Essam</h3>
    <p>AI & Machine Learning Enthusiast</p>
    <p>
      🔗 <a href="www.linkedin.com/in/rawanessammm">LinkedIn</a> | 
      <a href="https://github.com/rawanessaam">GitHub</a>
    </p>
  </div>
</div>


</div>
