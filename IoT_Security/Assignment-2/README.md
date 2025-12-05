🛡️ Malware Classification Project

	Name: Lakshminath Reddy Alamuru
	SUID: 367982169
	Goal: Classify Windows PE files as malicious or benign using supervised machine learning models.

📌 Overview

	This project builds a complete machine learning pipeline to detect malware using structured PE (Portable Executable) file metadata. Multiple models—Random Forest, Linear SVM, Neural Network, KNN, and XGBoost—are evaluated under both default and tuned configurations.

	The objective is to compare model performance and identify the most robust classifier.

📂 Dataset

	The dataset used is MalwareData.csv, a structured PE header dataset widely used for academic malware analysis.
	Rows: ~140,000 samples
	Classes: legitimate (0 = malicious, 1 = benign)
	Features: PE header metadata (imports, size, entropy, timestamps, etc.)

🏗️ Project Steps
1. Environment Setup

	Imported required modules:
	pandas, numpy, matplotlib, sklearn, xgboost, and others.

	import pandas as pd
	import numpy as np
	import matplotlib.pyplot as plt
	from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
	from sklearn.preprocessing import StandardScaler
	from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, ConfusionMatrixDisplay
	from sklearn.ensemble import RandomForestClassifier
	from sklearn.svm import LinearSVC
	from sklearn.neural_network import MLPClassifier
	from sklearn.decomposition import PCA
	from sklearn.neighbors import KNeighborsClassifier
	from xgboost import XGBClassifier

2. Load Dataset from MalwareData.csv (with seperator |)

3. Data Cleaning & Feature Engineering

	Removed non-informative features (e.g., Name, md5, version fields).
	Converted all values to numeric and replaced invalid values.
	Applied StandardScaler normalization.
	Performed PCA dimensionality reduction retaining 80% explained variance.

4. Train–Test Split

	Performed an 80–20 split with stratification.
	train_test_split(..., test_size=0.2, stratify=y)

5. Model Training (Default Settings)

	Trained the following models:

	Model	Included
	Random Forest	✔️
	Linear SVM	✔️
	Neural Network (MLP)	✔️
	KNN	✔️
	XGBoost	✔️

	For each: Performed 5-fold cross-validation. Evaluated on test set using accuracy, precision, recall, F1-score, ROC-AUC. Displayed confusion matrix

6. Hyperparameter Tuning

	Used GridSearchCV to safely tune parameters.
	Key grids included:

	Random Forest → n_estimators, max_depth
	KNN → k values & weights
	Neural Network → layer sizes, learning rate
	XGBoost → depth, estimators, learning rate
	SVM → C parameter
	Produced tuned models for comparison.

7. Summary Tables

	Two summary tables were generated:
	Default Model Performance
	Tuned Model Performance
	Metrics reported:
	Accuracy, Precision, Recall, F1-score, ROC-AUC

8. Comparison Plots

	Plotted side-by-side bars comparing:
	Accuracy, F1-score, ROC-AUC
	for default vs. tuned models.

📊 Summary of Results
	Overall Performance

	All models achieved very high accuracy (97–99%), but differences exist:

	✔️ Best Models
     Random Forest and XGBoost
     Accuracy & ROC-AUC ≈ 0.999
	 Excellent recall → best for malware detection

	✔️ Improved Models

	KNN improved from 98.7% → 99.0% after tuning
	Competed with Random Forest

⚠️ Weaker Models

	Linear SVM struggled with nonlinear patterns
	Lower recall (≈93%)
	🤖 Neural Network
	Performed well but did not surpass ensemble models

⚠️ Limitations

	Dataset is imbalanced (70% benign / 30% malicious).
	→ Models may appear better than they generalize.

	Risk of overfitting due to high accuracy across all models.
	Hyperparameter search was limited; wider search may yield better results.
	All testing was done on the same dataset; external validation needed.

🚀 Possible Improvements

	Use SMOTE or class weights to handle imbalance.
	Expand hyperparameter search (Bayesian Optimization).
	Test on unseen malware samples or VirusShare datasets.
	Try Deep Learning on raw binaries (CNN/Byte-Embedding models).


📝 Conclusion

	This project demonstrates a complete malware classification workflow using classical ML.
	Tree-based models—Random Forest and XGBoost—showed the best robustness and generalization, achieving near-perfect metrics.
	With improved validation and broader hyperparameter tuning, this pipeline can be production-ready for advanced malware detection research
	