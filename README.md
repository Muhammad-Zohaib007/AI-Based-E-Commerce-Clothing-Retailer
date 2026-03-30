# 👕 Fashion Forward: CNN-Based Garment Classification

**Simple Deep Learning Prototype for Clothing Image Classification**  
Built with PyTorch, FashionMNIST, and CNN fundamentals

---

## 📌 Overview

This project demonstrates how a Convolutional Neural Network (CNN) can be used to classify clothing images.

It is built as a prototype for automated garment categorization, inspired by real-world e-commerce use cases such as product tagging and inventory organization.

---

## 🎯 Problem Statement

Manually categorizing clothing images is time-consuming and inconsistent.

This project shows how deep learning can automate this process by classifying images into predefined categories, forming a foundation for:

- Product categorization  
- Improved search filtering  
- Inventory organization  

---

## 🧠 Dataset

This project uses the FashionMNIST dataset.

| Feature      | Value |
|-------------|------|
| Image Type   | Grayscale |
| Image Size   | 28 × 28 |
| Classes      | 10 |
| Examples     | Shirt, Shoe, Bag, Dress |

---

## 🏗️ Model Architecture
The project utilizes a custom `MultiClassImageClassifier` designed for efficient image processing:

* **Convolutional Layer**: 1 input channel to 16 output channels with a $3 \times 3$ kernel.
* **Activation**: ReLU for non-linearity.
* **Pooling**: MaxPool2d ($2 \times 2$) for spatial dimension reduction.
* **Classifier**: Fully connected linear layer mapped to the specific number of garment classes.



[Image of Convolutional Neural Network architecture]



### 🔍 Layer Purpose

- **Conv2D**: Extracts visual features like edges and textures  
- **ReLU**: Adds non-linearity to learn complex patterns  
- **MaxPooling**: Reduces image size while keeping important features  
- **Fully Connected Layer**: Produces final class predictions  

---

## 🚀 Features

- Custom CNN built with PyTorch  
- Efficient data loading using DataLoader  
- Evaluation using TorchMetrics  
- Per-class performance analysis  

---

## ⚙️ How It Works

1. Load FashionMNIST dataset  
2. Convert images into tensors  
3. Train CNN using CrossEntropyLoss  
4. Optimize using Adam optimizer  
5. Evaluate using accuracy, precision, and recall  

---

## 📊 Evaluation

The model is evaluated using:

- **Accuracy**: Overall correctness  
- **Precision (per class)**: How many predicted items are correct  
- **Recall (per class)**: How many actual items are correctly identified  

---

## 🛠️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/fashion-forward.git
cd fashion-forward
