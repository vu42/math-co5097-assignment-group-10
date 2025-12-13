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

# Random Variable
Probability Density Function - PDF
---
---
# 1. Definition
The **Probability density function** (PDF) of a ***Continuous random variable*** X is a function that associates a probability with each range of realizations of X, denoted as $p(x)$. <sup>[2]</sup>

The probability of $X$ is: <sup>[1]</sup>

$$\boxed{P( X \in (a, b])=\int_{a}^{b} p(x) \,dx.}\tag{22.6.9}$$

---
# 2. Step-by-step Computation
## Step 1: From Discrete to Continuous
#### Step 1.1: Formulate the problem
- Suppose we measure the height of all adult males in a population:
  - Random Variable $X$: The height of a randomly selected person.
  - Characteristics: Height is a continuous variable. A person is not just exactly 170cm or 171cm tall, but could be 170.5cm, 170.53cm, etc.
- Objective: We want to calculate the probability (percentage of people) whose height falls within a tiny interval from $x$ to $x+\epsilon$.
  
---
#### Step 1.2: Geometric Visualization
![alt text](image-1.png){

---
#### Step 1.2: Geometric Visualization
- Blue Bars: Represent the actual data (the proportion of people falling into specific height intervals).
- Red Curve: The probability density function $p(x)$. This function represents the probability density at point $x$.

---
Consider the strip located at position $x$ in the illustration:
- When the width $\epsilon$ is sufficiently small, the curve $p(x)$ in this region changes negligibly. We consider the density from one end to the other to be flat and constant.
  $$\text{Density in this interval} \approx p(x)\tag{2.2.1}$$
- We apply a basic physical principle:
  $$\text{Total Quantity} = \text{Density} \times \text{Size}\tag{2.2.2}$$
    - Total Quantity: The probability we seek, $P(x \le X \le x + \epsilon)$.
    - Density: The value of the density function $p(x)$.
    - Size: The width of the interval $\epsilon$.
---
#### Step 1.3: Conclusion
Substituting these quantities into the equation above, we obtain:
$$P(x \le X \le x + \epsilon) \approx p(x) \cdot \epsilon.\tag{2.2.3}$$
---

### Step 2: Partitioning
Imagine the large interval from $a$ to $b$ is a long loaf of bread. To calculate the total, we slice this interval into $N$ equal, thin slices.
- The width of each slice is $\Delta x$ (let's denote this as $\epsilon$).
- The division points are: 
   - $x_0, x_1, x_2, ..., x_N$.
   - $x_0 = a$
   - $x_N = b$
---
### Step 3: Discrete Summation
The probability of the random variable $X$ falling into the large interval $[a, b]$ is simply the sum of the probabilities of it falling into each individual small slice (since these slices are disjoint).
$$P(a \le X \le b) \approx \sum_{i=0}^{N-1} P(x_i \le X \le x_i + \epsilon).\tag{2.2.4}$$
---
### Step 4: Substitution
For each slice $i$ (starting at $x_i$), apply formula $(2.2.3)$, we have: 
$$P(a \le X \le b) \approx \sum_{i=0}^{N-1} p(x_i) \cdot \epsilon.\tag{2.2.5}$$
---
### Step 5: The Limit (Transition to Calculus)
We let the number of slices $N$ approach infinity ($N \to \infty$), which means the width of each slice $\epsilon$ approaches zero ($\epsilon \to 0$).

Mathematically:
- The approximation $\approx$ becomes equality $=$.
$$P(a \le X \le b) = \lim_{\epsilon \to 0} \sum_{i=0}^{N-1} p(x_i) \cdot \epsilon.\tag{2.2.6}$$
- The summation symbol $\sum$ becomes the integral symbol $\int$.
- The finite width $\epsilon$ becomes the differential $dx$.
$$\lim_{\epsilon \to 0} \sum_{i=0}^{N-1} p(x_i) \cdot \epsilon = \int_a^b p(x) dx.\tag{2.2.7}$$
---
Thus, we have proven that:
$$P(a \le X \le b) = \int_a^b p(x) dx.\tag{Q.E.D.}$$
---
# 3. Exercises
> Suppose that we have the random variable with density given by $p(x) = \frac{1}{x^2}$ and $p(x) = 0$ otherwise. What is $P(X > 2)$?

We have: 
$$p(x) = \begin{cases} \frac{1}{x^2}, & \text{with } x \ge 1 \\ 0, & \text{otherwise} \end{cases}$$
---
## Step-by-step computation
**Step 1: Set up the probability formula**

For a continuous random variable, the probability that $X$ falls within a range is the area under the density curve $p(x)$ for that range. Apply the Formula $(22.6.9)$, we have: 
$$P(X > 2) = \int_{2}^{+\infty} p(x) \, dx$$
---
**Step 2: Substitute the function**

Since the range is from $2$ to $+\infty$ (which satisfies the condition $x \ge 1$), we use the function $p(x) = \frac{1}{x^2}$:
$$P(X > 2) = \int_{2}^{+\infty} \frac{1}{x^2} \, dx$$
---
**Step 3: Find the antiderivative**

Rewrite $\frac{1}{x^2}$ as a power to make it easier to integrate: $x^{-2}$. 

Apply the power rule for integration $\int x^n dx = \frac{x^{n+1}}{n+1}$, we have:
$$\int x^{-2} \, dx = \frac{x^{-2+1}}{-2+1} = \frac{x^{-1}}{-1} = -\frac{1}{x}$$
---
**Step 4: Evaluate the limits**

Apply the Fundamental Theorem of Calculus for the limits $2$ to $+\infty$:
$$P(X > 2) = \left[ -\frac{1}{x} \right]_{2}^{+\infty}$$
Substitute the upper limit ($+\infty$) and the lower limit ($2$):
$$P(X > 2) = \left[ -\frac{1}{x} \right]_{2}^{+\infty}= \lim_{x \to \infty} \left( -\frac{1}{x} \right) - \left( -\frac{1}{2} \right)$$
   As $x$ approaches infinity, $\frac{1}{x}$ approaches $0$.
Subtracting a negative becomes addition: 
$$P(X > 2) = \lim_{x \to \infty} \left( -\frac{1}{x} \right) - \left( -\frac{1}{2} \right)= 0 + \frac{1}{2} = 0.5$$
---
Conclusion:The probability $P(X > 2)$ is 0.5 (or 50%).
![alt text](image-2.png)

