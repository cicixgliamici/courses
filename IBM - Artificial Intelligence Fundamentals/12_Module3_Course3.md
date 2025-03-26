# Introduction to Neural Networks

Neural networks (NNs) are computational models inspired by the biological neural networks in the human brain. They enable machines to learn patterns from data through trial and error, mimicking the brain's ability to adapt and refine connections. This module explores how neural networks form the foundation of deep learning, their biological inspiration, and their role in modern AI systems.

---

## Biological Inspiration: From Neurons to Artificial Networks

### Biological Basis

1. **Human Brain Analogy**:  
   - **Neurons**: Biological neurons transmit electrochemical signals via synapses.  
   - **Plasticity**: The brain strengthens or weakens connections based on experience (neuroplasticity).

2. **Artificial Neurons**:  
   - **Perceptrons**: Simplified computational models inspired by biological neurons.  
   - **Activation**: Simulate "firing" using mathematical functions (e.g., sigmoid, ReLU).

![Biological vs. Artificial Neuron](https://miro.medium.com/v2/resize:fit:720/format:webp/1*DfMR4ajCBUj8YokW4yf5Ow.png)  

---

## Structure and Information Flow in Neural Networks

### The Perceptron: Basic Building Block

A perceptron processes inputs to produce an output through three stages:

1. **Input Layer**: Receives data (e.g., pixel values, sensor data).  
2. **Weights and Summation**:  
   - Each input is multiplied by a weight (\(w_i\)).  
   - Results are summed with a bias term (\(b\)):  
     \[
     z = \sum_{i=1}^n (w_i \cdot x_i) + b
     \]  
3. **Activation Function**:  
   - Determines if the neuron "fires":  
     \[
     y = \sigma(z)
     \]

---

## Perceptron Implementation in PyTorch

    # Simplified Perceptron Example in PyTorch
    import torch
    import torch.nn as nn

    class Perceptron(nn.Module):
        def __init__(self, input_dim):
            super().__init__()
            self.linear = nn.Linear(input_dim, 1)
            self.activation = nn.Sigmoid()

        def forward(self, x):
            return self.activation(self.linear(x))

---

## The Learning Process

### Key Concepts

- **Loss Function**: Quantifies prediction error (e.g., MSE, cross-entropy).  
- **Optimization**:  
  - **Gradient Descent**: Iteratively adjusts weights to minimize loss.  
  - **Backpropagation**: Propagates errors backward to update weights.  
- **Epochs**: Multiple passes over the dataset to refine accuracy.  

---

## Deep Learning Ecosystem Components

| Component           | Role                              | Examples                           |
|---------------------|-----------------------------------|-----------------------------------|
| **Frameworks**      | Simplify model building           | TensorFlow, PyTorch               |
| **Pretrained Models**| Enable transfer learning         | ResNet, BERT                      |
| **Hardware**        | Accelerate training               | GPUs, TPUs                        |

---

## References

- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.  
- PyTorch Documentation. (2023). [https://pytorch.org/docs](https://pytorch.org/docs)
