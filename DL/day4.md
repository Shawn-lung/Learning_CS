# 📘 Day 4 – Deep Learning Fundamentals (Day 1 in DL)

**Date:** Sept 9, 2025  

---

## ✅ Key Learnings

### Neuron
- A neuron is the basic unit of a neural network.  
- It performs a **weighted sum of inputs**, adds a **bias**, and applies an **activation function**.  
- Formula:  
  \
  y = f(w_1x_1 + w_2x_2 + \dots + w_nx_n + b)
  \
- Intuition: each input contributes differently (scaled by weights), and the activation decides how strongly the neuron “fires.”

### Dense Layer
- A **Dense layer** (Fully Connected layer) is simply a collection of neurons.  
- Each input connects to **every neuron** in the layer.  
- Mathematically:  
  \
  y = W \cdot x + b
  \
  where \(W\) is the weight matrix and \(b\) is the bias vector.  
- Usually followed by an activation function (ReLU, sigmoid, softmax).  
- Dense layers are often used near the end of models for prediction.

### TensorFlow Perspective
- In Keras, a Dense layer is created with:  
  ```python
  from tensorflow.keras import layers
  dense = layers.Dense(units=4, input_shape=(3,))
  ```
  - `units=4` → number of neurons (outputs).  
  - `input_shape=(3,)` → input has 3 features.  
- TensorFlow manages the weight matrix (3×4) and bias vector (length 4).

---

## ❓ Questions I Asked Today
1. *What is a neuron in deep learning?*  
   → It’s a unit that performs weighted sum + bias + activation.  

2. *How does a Dense layer relate to neurons?*  
   → It’s just many neurons grouped together, which mathematically equals matrix multiplication + bias.  

---

## 🧪 Mini Test & Answers

**Q1. What are the three key components of a single neuron?**  
👉 Weights, bias, and activation function.  

**Q2. Suppose we have inputs \([1, 2]\), weights \([0.5, 0.25]\), and bias \(1\), with activation = identity (no nonlinearity). What is the neuron’s output?**  
👉 \(0.5 	imes 1 + 0.25 	imes 2 + 1 = 0.5 + 0.5 + 1 = 2.0\).  

**Q3. Why is a Dense layer also called a Fully Connected layer?**  
👉 Because every input is connected to every neuron in the layer.  

---

## 📝 Reflection
- I now understand the step-by-step function of a neuron: weighted sum → bias → activation.  
- A Dense layer is simply many neurons at once, so the math naturally becomes matrix multiplication + bias.  
- This builds confidence: even very complex deep learning models are just combinations of these basic units.  
