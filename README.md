# Fashion Forward: AI-Driven Garment Classification

Fashion Forward is an AI-powered e-commerce initiative aimed at revolutionizing product categorization. By leveraging deep learning, this project automates the sorting of new clothing listings into distinct categories (e.g., shirts, trousers, shoes), optimizing the customer search experience and streamlining inventory management.

## 📌 Project Overview
As e-commerce scales, manual categorization becomes a bottleneck. This project implements a **Convolutional Neural Network (CNN)** built with **PyTorch** to classify garment images accurately. 

### Key Objectives:
* Automate product categorization for faster listing.
* Enhance user experience through accurate search filters.
* Improve inventory logistics via automated sorting.

---

## 🏗️ Model Architecture
The project utilizes a custom `MultiClassImageClassifier` designed for efficient image processing:

* **Convolutional Layer**: 1 input channel to 16 output channels with a $3 \times 3$ kernel.
* **Activation**: ReLU for non-linearity.
* **Pooling**: MaxPool2d ($2 \times 2$) for spatial dimension reduction.
* **Classifier**: Fully connected linear layer mapped to the specific number of garment classes.



[Image of Convolutional Neural Network architecture]


---

## 🚀 Features
- **Deep Learning Framework**: Built using `PyTorch`.
- **Advanced Metrics**: Evaluation performed using `torchmetrics` for Accuracy, Precision, and Recall (per-class analysis).
- **Scalable Pipeline**: Includes DataLoaders for efficient batch processing.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/fashion-forward.git](https://github.com/YOUR_USERNAME/fashion-forward.git)
   cd fashion-forward
