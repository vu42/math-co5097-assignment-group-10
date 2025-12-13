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
MSE & Bias-Variance Trade-off
---
---
1. The _true parameter_ is $\theta$ of given population
2. $\hat{\theta}_n$ is an estimator of $\theta$ that depends on a sample of size $n$.
4. $\mu_n$ mean value of estimator.

---
From $(22.10.1)$ in the part of MSE, 
$$
\begin{aligned}

\mathrm{MSE}(\hat{\theta}_n, \theta) 
&= E\left[(\hat{\theta}_n - \theta)^2\right] \\[6pt]
&= E\left[((\hat{\theta}_n - \mu_n) + (\mu_n - \theta))^2\right] \\[6pt]
&= E[(\hat{\theta}_n - \mu_n)^2] + 2\,E[(\hat{\theta}_n - \mu_n)(\mu_n - \theta)] + E[(\mu_n - \theta)^2] \\[6pt]
&= E[(\hat{\theta}_n - \mu_n)^2] + 2\,E[\hat{\theta}_n - \mu_n]\,E[\mu_n - \theta] + E[(\mu_n - \theta)^2] \\[6pt]

\end{aligned}
$$

---
Having,
$$
\mu_n = E[\hat{\theta}_n] 
$$

And, 
$$
\mathrm{bias}(\hat{\theta}_n) = E[\hat{\theta}_n - \theta] 
= E[\hat{\theta}_n] - \theta
= \mu_n - \theta 
$$

From $(22.10.3)$,
$$
\textrm{Var}(\hat{\theta}_n) = E[(\hat{\theta}_n - E[\hat{\theta}_n])^2] = E[(\hat{\theta}_n - \mu_n)^2]
$$

Having, $\mu_n$ and $\theta$ are both constant, thus, 
$$ 
E[\mu_n - \theta] = \mu_n - \theta 
$$ 
$$ 
E[(\mu_n - \theta)^2] = (\mu_n - \theta)^2 = (\mathrm{bias}(\hat{\theta}_n))^2
$$
From having $\mu_n$, thus,
$$
E[\hat{\theta}_n - \mu_n] = E[\hat{\theta}_n] - \mu_n = \mu_n - \mu_n = 0
$$
---
From $(22.10.1)$ in the part of MSE, 
$$
\begin{aligned}

\mathrm{MSE}(\hat{\theta}_n, \theta) 
&= E[(\hat{\theta}_n - \mu_n)^2] + 2\,E[\hat{\theta}_n - \mu_n]\,E[\mu_n - \theta] + E[(\mu_n - \theta)^2] \\[6pt]
&= \textrm{Var}(\hat{\theta}_n) + (\mathrm{bias}(\hat{\theta}_n))^2 \\[6pt]

\end{aligned}
$$
However, this statement in reality is impossible to happen. Cause irreducible error is not due to the model being "wrong" or "unstable." It arises because real-world outcomes include randomness that features do not capture.
Hence, in practical, equation provided $(22.10.4)$ is true and could understand by follwing explaination:

$$
\mathrm{MSE}(\hat{\theta}_n, \theta)
= \underbrace{\textrm{Var}(\hat{\theta}_n)}_{\text{Variance}} + \underbrace{(\mathrm{bias}(\hat{\theta}_n))^2}_{\text{Bias}^2} + \underbrace{\operatorname{Var}(\theta)}_{\text{Irreducible error}} 
$$
---

This identity is the foundation of the bias–variance trade-off.

- **$Bias^2$** quantifies _systematic error_: how far the average model prediction is from the true function. 
- **Variance** quantifies _instability_: reflects sensitivity to random fluctuations in the training data. 
- **Irreducible error**  quantifies *intrinsic noise*: randomness in the outcome that cannot be explained by features, even if the true function $f$ were known.

---

**Why this is called a "trade-off":**

In practice, model design often involves choosing complexity (e.g., number of parameters, depth of a tree, regularization strength). 

Model complexity affects bias and variance in opposite directions.

- **Simpler models** tend to have **higher bias** but **lower variance**.
- **More complex models** tend to have **lower bias** but **higher variance**.

Because improving one component can worsen the other, model selection is a balancing act: 
1. Reducing bias without exploding variance.
2. Reducing variance without oversimplifying.

---

**High bias**: underfitting and lack of flexibility occurs when the model class is too restrictive to represent the true relationship between features and outcomes.

- **Example pattern:** A linear model fitted to a strongly nonlinear relationship.
- **Consequence:** Even with large datasets, the model remains systematically wrong.

This is commonly referred to as **underfitting** (or *lack of flexibility*): The model cannot capture higher-dimensional or nonlinear structure, so its predictions remain consistently off target.

---

**High variance**: overfitting and poor generalization occurs when a model is overly flexible relative to the available data.


- **Example pattern:** A very deep decision tree trained on a small dataset.
- **Consequence:** The model fits not only signal but also noise, and small changes in training data lead to large changes in the learned model.

This is commonly referred to as **overfitting** and leads to **poor generalization**: performance appears strong on training data but degrades on new data.


**Practical Keynotes**

- When **MSE** is  large, investigate whether the dominant source is bias (underfitting), variance (overfitting).

- Tuning model complexity and regularization is fundamentally about navigating the bias–variance trade-off.


---
# Statistics
Hypothesis Testing & Confusion Matrix
---
---
## 1. Hypothesis Testing Setup
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

## 2. Four Possible Outcomes (Confusion Matrix View)

**Machine learning confusion matrix**

|  | Predict Positive | Predict Negative |
|--------------------|-----------------|------------------|
| **Actual Positive**    | True Positive   | False Negative   |
| **Actual Negative**    | False Positive  | True Negative    |

- **False Positive (FP)** **Type I error**  
- **False Negative (FN)** **Type II error**

---

## Base knowledge
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

## Mapping into Machine learning Confusion Matrix
|  | Predict Positive | Predict Negative |
|--------------------|-----------------|------------------|
| **Actual Positive**    | True Positive <br> $=$ Correct decision   | False Negative $=\beta$ <br> $=P(\text{fail to reject } H_0 \mid H_0 \text{ is false})$   |
| **Actual Negative**    | False Positive $=\alpha$<br>$=P(\text{reject } H_0 \mid H_0 \text{ is true})$  | True Negative <br> $=$ Correct decision   |

---

## Example

Hypothesis: Finding out new drug effect or Not on a group of patients.

$$
H_0 (Null\,hypothesis): \text{Drug has no effect}
\qquad\text{vs}\qquad
H_1 : \text{Drug has real effect exists}
$$

|  | Predict Drug Effect | Predict Drug Not Effect |
|--------------------|-----------------|------------------|
| **Actual Effect**    | True Positive <br> $=$ Correct decision   | False Negative $=\beta$<br>$=P(\text{fail to reject } H_0 \mid H_0 \text{ is false})$   |
| **Actual Not Effect**    | False Positive $=\alpha$<br>$=P(\text{reject } H_0 \mid H_0 \text{ is true})$  | True Negative <br> $=$ Correct decision   |

---
## Intepretation
- Type I error rate (FP):
    - False alarm - **Falsely** "discover" something. 
    *[Discover something exist, however, it does not.]*
    - In ML terms: you predicted "positive" when the truth was negative

- Type II error rate (FN):
    - **Missing** "discover" something.
    *[Skip a fact that is existed.]*
    - In ML terms: you predicted “negative” when truth is positive.

---
## Some reasons may lead to that and solvings

- Type I error rate (FP):
    - Random noise sample (Sample selection technique)
    
- Type II error rate (FN):

    - Sample size is small (So increase the sample size)
    - Results are noisy (So redesign experiment, or change the measurement)
    - The observed effect is weak (So increase the treatment, or the sample size)

---
**Medical Screening**
- Screening can falsely alarm healthy people or overlook real disease.
- Screening test would be cheap, easy to administer, and produce zero false negatives, if possible. 
- Large sample.
*Hence*, more Type I error (false positive) and less Type II error (false negative)

Vietnam COVID-19 Screening Example: 
- **Hypothesis**: A person has COVID-19.
- **Null-Hypothesis $(H_0)$**: A person does not have COVID-19. 
- **Type I error (FP)**: The **test says a person has COVID-19** when they are **actually healthy**. Which leads to unnecessary isolation, anxiety, and resource use.
- **Type II error (FN):** The **test says a person is healthy** when they **actually have COVID-19**. Leads to undetected spread and delayed treatment.

---
## Reference 

[1] D. Zhang, Z. C. Lipton, M. Li, and A. J. Smola "Statistics," in *Mathematics for Deep Learning*, d2l.ai. Available: https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/statistics.html

[2] C. J. Geyer, "Models, Parameters, and Statistics," University of Minnesota, Minneapolis, MN, USA. Available: https://www.stat.umn.edu/geyer/old/5102/n2.pdf

[3] "Type I and type II errors," *Wikipedia*, Wikimedia Foundation, Available: https://en.wikipedia.org/wiki/Type_I_and_type_II_errors.