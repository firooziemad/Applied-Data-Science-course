# 🏨 Assignment 1 (based on Hotel Booking Demand Dataset)

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
This repository contains the final submission for my data analysis project. The goal of this assignment is to demonstrate a complete data processing pipeline—from raw, messy data to mathematically sound, machine-learning-ready features. 

The dataset analyzes booking records for a City Hotel and a Resort Hotel, containing details such as booking lead time, length of stay, price (Average Daily Rate), and cancellation status.

**Dataset Source:** [Kaggle - Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

---

## 🧩 Key Components

### 1. Exploratory Data Analysis & Data Cleaning
* **Imputation:** Handled organic missing values across categorical and numerical features.
* **Anomaly Detection:** Filtered out invalid data (e.g., bookings with 0 guests) and removed extreme pricing outliers using the IQR statistical method.
* **Preprocessing:** Applied Categorical Encoding and One-Hot Encoding to prepare data for machine learning algorithms, alongside MinMax and Standard Scaling.

### 2. Advanced Data Visualization
Developed a suite of visualizations to uncover hidden trends, ensuring readability and accurate scaling:
* 🥧 **Composition:** Pie charts and Stacked Bar charts mapping market segments.
* 📈 **Trends:** Multi-line charts mapping price seasonality.
* 🫧 **Multivariate:** Bubble charts mapping lead time, price, and stay duration simultaneously.
* 📊 **Uncertainty:** Bar charts featuring asymmetric error bars (Zero-Capped Variance).
* 🖱️ **Interactive:** Integrated **Plotly** for granular scatter analysis and **Bokeh** for a highly interactive, mute-able time-series analysis of weekly price fluctuations.

### 3. Feature Engineering & PCA
* **Feature Creation:** Engineered complex features including `Price_Per_Person`, `Total_Nights`, and aggregated `ADR_to_Segment_Ratio`.
* **Transformations:** Executed datetime extractions and applied mathematical transformations (e.g., Square Root of Lead Time) to stabilize variance.
* **Mutual Information:** Utilized `mutual_info_classif` to mathematically prove the predictive power of the newly engineered features against the target variable (`is_canceled`).
* **Dimensionality Reduction:** Applied Principal Component Analysis (PCA) to compress 35 features down to 21 components while strictly retaining 90% of the statistical variance.

---

## 🛠 Technologies & Libraries

| Category | Tools/Libraries |
| :--- | :--- |
| **Language** | Python |
| **Data Manipulation** | Pandas, NumPy |
| **Static Visualization** | Matplotlib, Seaborn |
| **Interactive Visualization** | Plotly, Bokeh |
| **Machine Learning / Preprocessing** | Scikit-Learn (`StandardScaler`, `PCA`, `SelectKBest`, `mutual_info_classif`) |

---

## 💡 Highlight Insights
1. **The Off-Peak Premium:** While Resort hotels experience massive price surges during mid-summer (Week 33), City Hotels actually command a higher Average Daily Rate for the vast majority of the off-peak year.
2. **Cancellation Anomalies:** "Non Refund" deposits exhibit a disproportionately high cancellation rate, indicating systemic behavior (likely travel agent block-booking adjustments) rather than individual guest behavior.
3. **The Value of Feature Engineering:** Statistical analysis proved that manually engineered features (like comparing a guest's price to their specific market segment's average) were significantly more predictive of cancellations than the raw baseline data.

---

## 💻 How to Run

You can view and execute this project directly in your browser using Google Colab.

1. **Open in Colab:** [Click here to open the notebook](https://colab.research.google.com/drive/1b2NnHOm52CeE68JkQC225A5vP9ZD1suW?usp=sharing)
2. **Download the Data:** Download `hotel_bookings.csv` from Kaggle.
3. **Execute:** Run the first cell to upload the CSV, then execute the notebook sequentially. 

---

## 📁 Project Structure
```text
├── README.md                    <- The top-level README for developers using this project.
├── hotel_booking_analysis.ipynb <- Main Jupyter Notebook containing all code, outputs, and markdown.
└── hotel_bookings.csv           <- Raw dataset (Ensure this is uploaded before running the notebook)
```

---

## 👨‍💻 Author

**[Emad Firoozi / firooziemad]**
* Sharif University of Technology, Spring 2026 / Applied Data Science
* Date: 5/2/2026
