# Classical Machine Learning: Foundations and Key Algorithms  

---

## 1. Introduction to Classical Machine Learning  
Classical machine learning refers to traditional, non-deep-learning algorithms that solve problems through statistical inference and pattern recognition. These models are characterized by:  
- **Interpretability**: Transparent decision-making processes.  
- **Efficiency**: Lower computational demands compared to deep learning.  
- **Robustness**: Effective with small-to-medium datasets.  

This document focuses on three foundational algorithms: **decision trees**, **linear regression**, and **logistic regression**, along with their advantages and the role of the **sigmoid function**.

---

## 2. Decision Trees  

### Definition  
A **decision tree** is a hierarchical model that splits data into subsets based on feature values, leading to a final prediction (classification or regression).  

### Structure  
- **Root Node**: The top decision point (e.g., "Is age > 30?").  
- **Internal Nodes**: Subsequent decision splits.  
- **Leaf Nodes**: Terminal nodes providing final predictions.  

### Splitting Criteria  
- **Entropy**: Measures impurity (uncertainty).  
  \[
  \text{Entropy}(S) = -\sum_{i=1}^c p_i \log_2 p_i
  \]
  where \( p_i \) is the proportion of class \( i \) in set \( S \).  
- **Gini Impurity**: Probability of misclassifying a random sample.  
  \[
  \text{Gini}(S) = 1 - \sum_{i=1}^c p_i^2
  \]  
- **Information Gain**: Reduction in entropy after a split.  

### Advantages & Limitations  
| **Pros**                          | **Cons**                          |  
|-----------------------------------|-----------------------------------|  
| Interpretable (human-readable).   | Prone to overfitting.             |  
| Handles non-linear relationships. | Sensitive to small data changes.  |  
| No need for feature scaling.      | Biased toward dominant classes.   |  

### Example  
Predicting loan approval based on income, credit score, and employment status.  

---

## 3. Linear Regression  

### Definition  
**Linear regression** models the relationship between a dependent variable \( y \) and one or more independent variables \( X \) using a linear equation.  

### Mathematical Formulation  
Simple linear regression:  
\[
y = \beta_0 + \beta_1 x + \epsilon
\]  
Multiple linear regression:  
\[
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon
\]  
- \( \beta_0 \): Intercept.  
- \( \beta_1, \dots, \beta_n \): Coefficients.  
- \( \epsilon \): Error term.  

### Loss Function  
Mean Squared Error (MSE):  
\[
\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
\]  

### Optimization  
**Ordinary Least Squares (OLS)**: Minimizes MSE analytically.  
**Gradient Descent**: Iteratively adjusts coefficients using:  
\[
\beta_j := \beta_j - \alpha \frac{\partial}{\partial \beta_j} \text{MSE}
\]  
where \( \alpha \) is the learning rate.  

### Use Cases  
- Predicting house prices based on square footage and location.  
- Estimating sales from advertising spend.  

---

## 4. Logistic Regression  

### Definition  
**Logistic regression** predicts binary outcomes (e.g., 0/1) by modeling the probability \( P(y=1) \) using the logistic (sigmoid) function.  

### Sigmoid Function  
\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]  
where \( z = \beta_0 + \beta_1 x_1 + \dots + \beta_n x_n \).  

### Decision Boundary  
- If \( \sigma(z) \geq 0.5 \), predict class 1; else, predict class 0.  

### Loss Function  
Log Loss (Cross-Entropy):  
\[
\text{Loss} = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \log(\hat{p}_i) + (1 - y_i) \log(1 - \hat{p}_i) \right]
\]  

### Use Cases  
- Spam detection (spam vs. not spam).  
- Medical diagnosis (disease present/absent).  

---

## 5. Advantages of Classical Machine Learning  

1. **Interpretability**:  
   - Models like decision trees and linear regression provide clear insights into feature importance (e.g., coefficients in linear regression).  
2. **Computational Efficiency**:  
   - Train quickly on CPUs, even with limited resources (vs. GPUs for deep learning).  
3. **Robustness to Small Data**:  
   - Perform well with hundreds (not millions) of samples.  
4. **Feature Engineering Flexibility**:  
   - Domain knowledge can be directly incorporated (e.g., creating interaction terms).  
5. **Theoretical Guarantees**:  
   - Statistical properties (e.g., confidence intervals for coefficients) support reliable inference.  

### Classical vs. Deep Learning  
| **Factor**          | **Classical ML**                | **Deep Learning**               |  
|----------------------|----------------------------------|----------------------------------|  
| Data Size            | Small to medium                 | Large                            |  
| Interpretability     | High                            | Low (black-box models)           |  
| Hardware             | CPUs sufficient                 | GPUs/TPUs required               |  
| Training Time        | Minutes to hours                | Hours to weeks                  |  

---

## 6. The Sigmoid Function in Machine Learning  

### Role of the Sigmoid  
1. **Logistic Regression**:  
   - Maps linear combinations \( z \) to probabilities \( [0, 1] \).  
2. **Neural Networks**:  
   - Historically used as activation functions in hidden layers (largely replaced by ReLU).  
3. **Calibration**:  
   - Converts model outputs (e.g., SVM scores) to probabilities.  

### Properties  
- **Smooth Gradient**:  
  \[
  \frac{d}{dz} \sigma(z) = \sigma(z)(1 - \sigma(z))
  \]  
  Prevents abrupt jumps in updates during gradient descent.  
- **Interpretability**:  
  Outputs can be directly read as probabilities.  

### Limitations  
- **Vanishing Gradients**:  
  For extreme \( z \) values, gradients approach zero, slowing learning.  
- **Computational Cost**:  
  Exponential functions are slower than ReLU in deep networks.  

### Alternatives to Sigmoid  
- **ReLU**: \( f(z) = \max(0, z) \) (common in neural networks).  
- **Probit Function**: Inverse of the Gaussian CDF (used in some regression models).  

---

## 7. Case Studies  

### Case 1: Credit Scoring with Logistic Regression  
- **Task**: Predict loan default risk.  
- **Features**: Income, credit history, debt-to-income ratio.  
- **Outcome**: Probability of default \( P(\text{default}) \).  

### Case 2: Demand Forecasting with Linear Regression  
- **Task**: Estimate product demand based on price and seasonality.  
- **Model**: \( \text{Demand} = \beta_0 + \beta_1 \text{Price} + \beta_2 \text{Season} \).  

---

## 8. Conclusion  
Classical machine learning remains vital for scenarios requiring transparency, efficiency, and reliability. Decision trees excel in interpretability, linear regression in modeling linear relationships, and logistic regression in probabilistic binary classification. The sigmoid function bridges linear models and probabilistic interpretations, though its limitations have spurred alternatives in deep learning.  

---

## 9. References  
1. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.  
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning*. Springer.  
3. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.  
4. Ng, A. (2012). *Machine Learning Yearning*. DeepLearning.ai.  
