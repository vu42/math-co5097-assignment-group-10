---
marp: true
style: |
  section {
    h1, h2, h3, h4, h5, h6 {
    color: black !important;}
    color: black !important;
    font-family: "Arial", sans-serif;
    font-size: 30px;
    line-height: 1.3;
  }
---
# Statistics
Hypothesis Testing
---
---
### **1. Hypothesis Testing Setup**
Hypothesis:
$$
H_0 : \text{null hypothesis}
\qquad\text{vs}\qquad
H_1 : \text{alternative hypothesis}
$$
In practice, we make a decision:

- **Reject** $H_0$, or 
- **Fail to reject** $H_0$.

---

### **2. Four Possible Outcomes (Confusion Matrix View)**

**Machine learning confusion matrix**

| Reality / Decision | Predict Positive | Predict Negative |
|--------------------|-----------------|------------------|
| Actual Positive    | True Positive   | False Negative   |
| Actual Negative    | False Positive  | True Negative    |


**Hypothesis testing:**

- **False Positive (FP)** $\leftrightarrow$ **Type I error**  
- **False Negative (FN)** $\leftrightarrow$ **Type II error**

---

## **Recall**
In $(22.10.5)$, 
$$
\text{statistical significance} 
= 1 - \alpha 
= 1 - P(\text{reject } H_0 \mid H_0 \text{ is true})
$$
And in $(22.10.6)$,
$$
\text{statistical power} 
= 1 - \beta 
= 1 - P(\text{fail to reject } H_0 \mid H_0 \text{ is false})
$$
Thus, 
$$
\text{Type I error rate} = \alpha = P(\text{reject } H_0 \mid H_0 \text{ is true}) 
$$
$$
\text{Type II error rate} = \beta = P(\text{fail to reject } H_0 \mid H_0 \text{ is false}) 
$$
Note:
- $\alpha$ also knows at Significant level.
- $\beta$ also knows at Sensitivity.

---

## **Mapping into Machine learning Confusion Matrix**
| Reality / Decision | Predict Positive | Predict Negative |
|--------------------|-----------------|------------------|
| Actual Positive    | True Positive   | False Negative $=\beta =P(\text{fail to reject } H_0 \mid H_0 \text{is false})$   |
| Actual Negative    | False Positive $=\alpha =P(\text{reject } H_0 \mid H_0 \text{ is true})$  | True Negative    |

---

### **Experimental Sample**

Finding out new drug effect or Not on a group of patients.

Hypothesis setup:
$$
H_0 : \text{Drug has no effect}
\qquad\text{vs}\qquad
H_1 : \text{Drug has real effect exists}
$$

| Reality / Decision | Predict Drug Effect | Predict Drug Not Effect |
|--------------------|-----------------|------------------|
| Actual Effect    | True Positive   | False Negative $=\beta =P(\text{fail to reject } H_0 \mid H_0 \text{ is false})$   |
| Actual Not Effect    | False Positive $=\alpha =P(\text{reject } H_0 \mid H_0 \text{ is true})$  | True Negative    |


