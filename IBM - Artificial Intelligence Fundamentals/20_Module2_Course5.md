# Fairness in AI: Key Concepts and Challenges

## What is Fairness in AI?
**Fairness** in AI refers to the equitable treatment of individuals/groups by algorithms, ensuring decisions are **unbiased** and **free from discrimination** based on protected attributes. It aims to prevent systemic advantages/disadvantages for specific populations.

---

## Protected Attributes
**Protected attributes** are characteristics legally or ethically safeguarded from being used to discriminate. Common examples include:

| Attribute         | Examples                          |
|--------------------|-----------------------------------|
| **Demographic**    | Race, gender, age, religion       |
| **Socioeconomic**  | Income, education, nationality    |
| **Physical**       | Disability, pregnancy status      |
| **Legal**          | Citizenship, criminal record*     |

> **Note**: Some attributes (e.g., criminal history) may be context-dependent.  
> **Ethical AI Practice**: Avoid using protected attributes **directly** or **indirectly** (via proxies).

---

## Privileged vs. Unprivileged Groups
| Group Type         | Definition                          | Examples                          |
|---------------------|--------------------------------------|-----------------------------------|
| **Privileged**      | Historically advantaged groups      | Men in tech leadership roles      |
| **Unprivileged**    | Systemically marginalized groups    | Women in STEM fields              |

### Case Study: Loan Approval Algorithms  
- **Privileged**: High-income applicants (approved at 70% rate)  
- **Unprivileged**: Low-income applicants (approved at 30% rate)  
- **Bias Source**: Training data reflecting historical inequities.

---

## AI Bias: Types and Sources
**AI bias** occurs when systems produce **skewed outcomes** favoring/disfavoring specific groups.

### Types of Bias
1. **Data Bias**  
   - **Cause**: Unrepresentative/incomplete training data.  
   - **Example**: Facial recognition trained mostly on lighter-skinned faces.  

2. **Algorithmic Bias**  
   - **Cause**: Flawed model design amplifying data biases.  
   - **Example**: Resume screening tools penalizing "women-only" colleges.  

3. **Measurement Bias**  
   - **Cause**: Misaligned success metrics (e.g., prioritizing accuracy over fairness).  

4. **Deployment Bias**  
   - **Cause**: Using models in contexts they weren’t designed for.  

---

## Achieving Fairness: Methods and Metrics
### Common Fairness Metrics
| Metric               | Formula/Description                  | Use Case                          |
|----------------------|---------------------------------------|-----------------------------------|
| **Demographic Parity**| Equal approval rates across groups   | Hiring algorithms                 |
| **Equal Opportunity**| Equal true positive rates             | Credit scoring                    |
| **Disparate Impact** | Ratio of outcomes (threshold: ≥0.8)  | Legal compliance (U.S. EEOC)      |

### Mitigation Strategies
- **Pre-processing**: Balance datasets (e.g., oversampling underrepresented groups).  
- **In-processing**: Use fairness-aware algorithms (e.g., adversarial debiasing).  
- **Post-processing**: Adjust decision thresholds per group.  

---

## Challenges in AI Fairness
1. **Tradeoffs**: Fairness vs. accuracy (e.g., lowering false positives for one group may raise them for another).  
2. **Context Dependency**: Fairness criteria vary by culture/application (e.g., healthcare vs. criminal justice).  
3. **Proxy Variables**: Hidden correlations (e.g., ZIP code as a proxy for race).  

---

> **Example**: Amazon’s discontinued hiring tool discriminated against women due to biased historical data.  
> **Solution**: Regular **bias audits** and **diverse team input** during model development.

---

## Conclusion
Fairness in AI requires intentional design to address **protected attributes**, **group disparities**, and **bias sources**. While no one-size-fits-all solution exists, combining technical methods (e.g., fairness metrics) with ethical governance can reduce harm and build trust in AI systems.
