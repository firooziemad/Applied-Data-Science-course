# 🏢 Assignment 3: Applied Deep Learning & Neural Architectures

---

## 📑 Table of Contents

* [Project Overview](https://www.google.com/search?q=%23-project-overview)
* [Key Components](https://www.google.com/search?q=%23-key-components)
* [Technologies & Libraries](https://www.google.com/search?q=%23-technologies--libraries)
* [Highlight Insights](https://www.google.com/search?q=%23-highlight-insights)
* [How to Run](https://www.google.com/search?q=%23-how-to-run)
* [Project Structure](https://www.google.com/search?q=%23-project-structure)
* [Author](https://www.google.com/search?q=%23-author)

---

## 🚀 Project Overview

This repository contains a comprehensive exploration of modern Deep Learning architectures using **PyTorch**. The project transitions from foundational neural networks to advanced sequence and spatial modeling, demonstrating how different network topologies solve distinct data problems.

The objective is to master four core deep learning paradigms across three unique datasets: predicting employee attrition and income via Multilayer Perceptrons (MLPs), classifying natural scenes using Convolutional Neural Networks (CNNs), forecasting weather time-series data with Recurrent Neural Networks (RNNs), and implementing self-attention mechanisms via Transformers.

**Dataset Sources:**

1. IBM HR Analytics Employee Attrition & Performance
2. Intel Image Classification (Natural Scenes)
3. Daily Climate Time Series Data (Delhi)

---

## 🧩 Key Components

### 1. Multilayer Perceptrons (MLP) & Network Tuning

* **Classification & Regression:** Built custom MLPs to predict binary employee attrition and continuous monthly income.
* **Hyperparameter Optimization:** Conducted systematic experiments on optimizers (SGD, Adam), learning rate scheduling (`ReduceLROnPlateau`), and batch size variations to navigate the loss landscape.
* **Regularization & Stability:** Implemented Early Stopping, Dropout, L1/L2 Weight Decay, Gradient Clipping, and Batch Normalization to combat severe overfitting observed in deep, unregularized networks.

### 2. Convolutional Neural Networks (CNN) & Computer Vision

* **Spatial Feature Extraction:** Designed scratch-built CNNs to classify 150x150 RGB images into 6 natural scene categories.
* **Architectural Experiments:** Evaluated the computational and predictive impacts of varying kernel sizes, strides, pooling mechanisms, and network depth.
* **Data Augmentation & Transfer Learning:** Mitigated spatial overfitting using random flips, rotations, and color jitter. Deployed a pre-trained **ResNet-18** backbone as a feature extractor, vastly outperforming custom architectures.

### 3. Recurrent Neural Networks (RNN) & Sequence Modeling

* **Time-Series Forecasting:** Formatted daily climate data into 3D sliding-window tensors to predict future mean temperatures.
* **Architecture Showdown:** Trained and compared Vanilla RNN, LSTM, and GRU models to evaluate memory capacity and gradient flow over short sequences.
* **Advanced RNN Configurations:** Tested bidirectional processing, inter-layer dropout, and varied hidden states/depths to optimize sequence representations.

### 4. Transformers & Attention Mechanisms

* **Parallel Sequence Processing:** Implemented a custom `TimeSeriesTransformer` using PyTorch's native `TransformerEncoder` to bypass the sequential bottlenecks of RNNs.
* **Attention vs. Recurrence:** Integrated Positional Encoding and Multi-Head Attention to map global temporal context ($O(1)$ dependency path), comparing its convergence stability and computational footprint directly against the LSTM baseline.

---

## 🛠 Technologies & Libraries

| Category | Tools/Libraries |
| --- | --- |
| **Language** | Python |
| **Deep Learning Framework** | PyTorch (`torch`, `torch.nn`, `torch.optim`) |
| **Computer Vision** | TorchVision (`datasets`, `transforms`, `models`) |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly (`graph_objects`, `subplots`) |
| **Preprocessing & Metrics** | Scikit-Learn (`StandardScaler`, `accuracy_score`, `f1_score`, `confusion_matrix`, etc.) |

---

## 💡 Highlight Insights

1. **The Cost of Capacity:** Across both MLPs and CNNs, arbitrarily increasing network depth and width without corresponding regularization (like Dropout or Batch Norm) immediately resulted in catastrophic memorization and divergent validation loss.
2. **Transfer Learning Dominance:** In the image classification task, transferring ImageNet weights via a frozen ResNet-18 backbone bypassed the need for massive local compute, instantly jumping to an 85%+ accuracy in Epoch 1 by leveraging pre-learned universal textures.
3. **RNN Resiliency on Short Sequences:** While LSTMs and GRUs are essential for long-term dependencies, Vanilla RNNs proved highly competitive—and computationally lighter—when restricted to short 7-day forecasting windows where the vanishing gradient problem is negligible.
4. **Transformer Attention Dynamics:** The Transformer encoder successfully mapped temporal relationships in parallel, but early training exhibited micro-oscillations in validation loss because it lacks the built-in chronological inductive bias of LSTMs and must learn the concept of "time" entirely from positional sine waves.

---

## 💻 How to Run

You can view and execute this project directly in your browser using Google Colab or locally via Jupyter.

1. **Open the Environment:** Launch the Jupyter Notebook locally or open it in Google Colab. Ensure hardware acceleration (GPU/CUDA) is enabled.
2. **Download the Data:** Ensure the following files/directories are placed in the same working directory as the notebook:
* `WA_Fn-UseC_-HR-Employee-Attrition.csv`
* `seg_train/` and `seg_test/` (Intel Image folders)
* `DailyDelhiClimateTrain.csv` and `DailyDelhiClimateTest.csv`


3. **Execute:** Run the notebook sequentially from Part 0 through Part 4. The modular training loops will automatically manage GPU memory (`torch.cuda.empty_cache()`) between experiments.

---

## 📁 Project Structure

```text
├── README.md                               <- Top-level README for this assignment.
├── Assignment_3_Deep_Learning.ipynb        <- Main Jupyter Notebook containing all DL pipelines.
├── WA_Fn-UseC_-HR-Employee-Attrition.csv   <- Raw HR dataset.
├── DailyDelhiClimateTrain.csv              <- Training split for time-series.
├── DailyDelhiClimateTest.csv               <- Testing split for time-series.
└── seg_train/ & seg_test/                  <- Extracted image directories for CNN training.

```

---

## 👤 Author

**Emad Firoozi**
Course: Applied Data Science
