# 🏨 Assignment 2: Machine Learning & Predictive Modeling (Hotel Booking Demand)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Tools-Jupyter_Notebook-orange.svg)](https://jupyter.org/)
[![Colab](https://img.shields.io/badge/Platform-Google_Colab-F9AB00.svg)](https://colab.research.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 📑 Table of Contents
- [Project Overview](#-project-overview)
- [Key Components](#-key-components)
- [Technologies & Libraries](#-technologies--libraries)
- [Highlight Insights](#-highlight-insights)
- [How to Run](#-how-to-run)
- [Project Structure](#-project-structure)
- [Author](#-author)

---

## 🚀 Project Overview
This repository contains the second phase of the Hotel Booking Demand project. Building upon the exploratory data analysis and feature engineering from Assignment 1, this assignment focuses on deploying a comprehensive suite of Machine Learning algorithms. 

The objective is to solve three distinct business problems: predicting room prices (Regression), forecasting future pricing trends (Time-Series), anticipating customer cancellations (Binary Classification), and segmenting audiences (Multiclass Classification).

**Dataset Source:** [Kaggle - Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

---

## 🧩 Key Components

### 1. Regression & Time-Series Forecasting
* **Price Prediction (ADR):** Evaluated 10 different regression models including Linear, Ridge, LASSO, SVR, and Distance-Weighted KNN to predict the Average Daily Rate.
* **Advanced Error Analysis:** Utilized business-centric metrics (MAE, MedAE) alongside robust statistical metrics (Huber Loss, MSLE) to evaluate model performance against extreme pricing outliers.
* **Temporal Forecasting:** Engineered chronological datasets to forecast future weekly prices using ARIMA, Seasonal ARIMA (SARIMA), and Hidden Markov Models (HMM).

### 2. Binary Classification
* **Cancellation Prediction:** Trained and cross-validated Logistic Regression, Kernel SVM, Decision Trees, and Naive Bayes to predict booking cancellations.
* **Hyperparameter Tuning:** Utilized K-Fold Cross-Validation to optimize tree depth and nearest-neighbor constraints.
* **Information Theory Metrics:** Evaluated models using advanced metrics ideal for imbalanced datasets, including PR-AUC, Cross-Entropy (Log Loss), and Jensen-Shannon Divergence.
* **Visual Error Analysis:** Generated interactive ROC/PR curves and Confusion Matrix heatmaps to analyze the business cost of False Negatives.

### 3. Multiclass & Boosting Ensembles
* **Customer Segmentation:** Deployed state-of-the-art boosting algorithms to categorize bookings into 4 distinct Customer Types (Transient, Group, Contract, etc.).
* **Advanced Ensembles:** Implemented XGBoost, LightGBM, and CatBoost, alongside meta-learners like Stacking and Hard/Soft Voting Classifiers.
* **Imbalance Handling:** Evaluated models strictly using Macro F1-Scores and Cohen's Kappa to ensure minority classes (like "Group" bookings) were not statistically ignored by the models.

---

## 🛠 Technologies & Libraries

| Category | Tools/Libraries |
| :--- | :--- |
| **Language** | Python |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Standard Machine Learning** | Scikit-Learn (`LinearSVC`, `DecisionTrees`, `StackingClassifier`, etc.) |
| **Advanced Boosting** | XGBoost, LightGBM, CatBoost |
| **Time-Series & Stats** | Statsmodels (`SARIMAX`), `hmmlearn`, SciPy |

---

## 💡 Highlight Insights
1. **The Curse of Dimensionality:** Highly sparse, One-Hot Encoded data heavily handicapped standard linear models and Kernel SVMs (due to $O(n^2)$ memory scaling). Tree-based models and Locally Weighted KNN vastly outperformed them on this specific dataset.
2. **The Business Cost of Accuracy:** While Random Forests achieved the highest raw accuracy for cancellations, Decision Trees proved better for actual deployment by minimizing False Negatives (missing a cancellation), which is the most expensive error in the hospitality industry.
3. **LightGBM's Imbalance Mastery:** In the multiclass task, LightGBM dominated the traditional linear models and standard ensembles, yielding the highest Macro F1-Score while training in seconds, proving the power of histogram-based gradient boosting on imbalanced data.
4. **Time-Series Realities:** SARIMA forecasting captured the highly cyclical summer-spikes of the hotel industry perfectly, whereas the Hidden Markov Model (HMM) demonstrated how probabilistic transitions naturally settle into a smooth, steady-state average over long horizons.

---

## 💻 How to Run

You can view and execute this project directly in your browser using Google Colab.

1. **Open in Colab:** [Click here to open the notebook](https://colab.research.google.com/drive/1SHNlmlxz6dQZUkF5BYb0-X9ODVRbObVp?usp=sharing)
3. **Download the Data:** Download `hotel_bookings.csv` from Kaggle and upload it to the Colab session storage.
4. **Execute:** Run the notebook sequentially from Part 1 to Part 3. 

---

## 📁 Project Structure
```text
├── README.md                  <- Top-level README for developers using this project.
├── hotel_booking_ml.ipynb     <- Main Jupyter Notebook containing Regression, Classification, and Boosting pipelines.
└── hotel_bookings.csv         <- Raw dataset (Ensure this is uploaded before running the notebook)
