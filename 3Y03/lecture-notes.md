# *p* 3Y03

## Week 1 | Events and Manipulating Events

- Stats is the science of *collecting, analyzing, and inferring* from **data**
- **Probability** = mathematics of random events, intimately related to statistics
- **Experiment** = anything that produces **data**, while a ***random experiment*** is an experiement that can produce *different* outcomes from the same process
- **Sample Space** $:= S$ = the set of all outcomes of a **random experiment**

  - **Discrete** iff *finite* or *countably infinite*
  - **Continuous** iff *infinite*
- **Event** $:= E  \sube S$
- An *event* E, is a subset of the sample space *S* , where E is a set of outcomes
  - *E = {HHH, HHT, HTH, THH} ⊆⊆ {HHH, HHT, …} = S*
- Given some events, new events can be defined: 
- Given $E$, $E_1$, $E_2 \sube S$
  - **Union**: $E_1 \cup E_2 := \{ x \in S : x \in E_1 \lor x \in E_2\}$
- **Intersection**: $E_1 \cap E_2 := \{x \in S : x \in E_1 \land x \in E_2 \}$
  - **Complement:** $E' = \{x \in S : x \notin E\}$

If $E \sube S$ is any event, then $E \cup E' = S$ and $E \cap E'= \emptyset$

$S$ and $\empty$ are events, and $S' = \empty$ , given sample space $S$

- **Mutualy Exclusivity = ** Given $E_1, E_2, \sube S$ , two events are **mutually exclusive** if:
  - $E_1 \cap E_2 = \empty $
  - Inutition is that events cannot happen simultaneously, which using the coin exmaple with space $S = \{H, T\}$ would be the events $E_1 = \{H\}$ and $E_2 = \{T\}$
- Useful rules for **manipulating events** algebraically using events $A, B, C, \sube S$
- (A’)’ = A
- **Distributivity**:
  - (A ∪∪ B) ∩∩ C = (A ∩∩ C) ∪∪ (B ∩∩ C)
  - (A ∩∩ B) ∪∪ C = (A ∪∪ C) ∩∩ (B ∪∪ C)
- **DeMorgan’s Laws:**
  - (A ∪∪ B)’ = A’ ∩∩ B’
  - (A ∩∩ B)’ = A’ ∪∪ B’

### Counting Techniques

- **Basic Counting Principle**:

  - Suppose we have *r-many* experiments, and suppose the *ith* experiment has *n~i~* possible outcomes

  - The ***total number of outcomes*** from running all the experiments ***consecutively*** is

    $\displaystyle\prod_{i=1}^{r}{n_i =n_1*n_2 ... n_{r-1}n_r}$

  - **ex. coin flip:** if we toss a coin **3 times**, and each coin toss has **2 outcomes**, the the total number of outcomes if $\displaystyle\prod_{i=1}^{3}{2} = 2*2*2 = 2^3 = 8$


#### Permuatations

- ==**Permutations**: $n! = n ( n - 1 ) (n - 2) ... 3 * 2 * 1$==

  - Given *n* **distinct** objects, the number of ways to permute them is *n* **factorial**

  - In general,  the formula for a set of n distinct objects, the number of ways to permute $r \leq n$ of them is:

    $P^n_r = n Pr = n (n -1 ) .... ( n - r + 1) = \dfrac{n!}{(n-r)!}$

    - r = length of sequence, n = size of set to draw from. 

- Ex. number of 3 letter words with no repeats: $P_3^{26} = \frac{26!}{(26-3)!}$ = $26 * 25 *  24$

- Not all objects may be unique, ex. "**BANANA**"

- If all the letters were unique, there would be $6!$ perumtations, but since there are 3 As, and 2 Ns, some of the permutations leave the word unchanged

- There are 3! ways to permute the A's and 2! ways to permute the Ns. If we "cancel" the permuations that do nothing, we have $\frac{6!}{3!2!}$ = 60 many unique permutations

- Given $n = n_1 + n_2 + ... + n_r$ many objects with $n_i$ identical many objects of type i, there are

  $\dfrac{n!}{n_1!n_2!...n_r!}$

  ​    

#### Combinations

Given a group of n distinct objects, the number of ways to choose $r \leq n$ of them is

$C_r^n = n C r = (\dfrac{n}{r}) = \dfrac{n(n-1)..(n- r + 1)}{(n-r)!} = \dfrac{n!}{(n-r)! r!}$

n "choose" r

- **Binomial Coefficients** =  $(\dfrac{n}{r})$ 

  - Appear in many places, such as the binomial theorem

    $\forall x,y$ :  $(x + y)^n = \displaystyle\sum^{n}_{r=0}(\dfrac{n}{r})$

  - read as *n choose r*, or how many ways are there to choose r items from n elements

## Week 2 | Interpretations and Axioms of Probability

- Probabliity is used to quantify the likelihood, or chance that an outcome of a **random experiment** will occur
  - interpreted as the *limiting value* of the proportion of times the outcome occurs in *n* repetitions of the random experiment as n increases beyond all bounds

- **Equally Likely Outcomes** 
  - Whenever a **sample space** consists of $N$ possible outcomes that *are equally likely*, the probability of each outcome is $\dfrac{1}{N}$

- **Probability of an Event**
  - For a **discrete sample space**, the probability of an event **E**, denoted at P(E), equals the *sum* of the probabilities of the outcomes in **E**

### Axioms of Probability

Probability is a number that is assigned to each member of a collection of events from a random experiment, that satisfies the following:

- $P(S) = 1$, where $S$ is the **sample space**
- $0 \leq P(E) \leq 1$ *for any event*
- For two events, $E_1$ and $E_2$, with $E_1 \cap E_2 = \empty$ then $P(E_1 \cup E_2) = P(E_1) + P(E_2)$

The property that $0 \leq P(E) \leq 1$ is equivalent to the requirement that a relative frequency must be between 0 and 1

$P(\empty) = 0$

$P(E') = 1 - P(E)$

$P(E_1) \leq P(E_2) \iff E_1 \subseteq E_2$

#### Unions of Events and Addition Rules

Joint Events are generated by applying basic set operations at individual levels:

**Probability of a Union**

​	if A and B are **mutually exclusive**, then their intersection is ***zero***

- For 2 sets:

  $P(A \cup B ) = P(A) + P(B) - P(A \cap B)$

- For 3 or more sets:

![image-20200929211240449](images/lecture-notes/image-20200929211240449.png)

#### Mutual Exclusion

- **Mutual Exclusive** - for all pairs $E_i \cap E_j = \empty$, for $E_i,E_j \subseteq S$
  - $P(E_i \cap E_j) = P(E_i) + P(E_j)$

#### Intersection of Events and Mulitplication Total Probability Rules

##### Total Probability Rule (2 Events)

*For any events, A and B*

$P(B) = P(B\cap A) + P(B \cap A' ) = P(B|A)P(A) + P(B|A')P(A')$

##### Total Probability Rule (Multiple Events)

*Assume $E_1, E_2, ... , E_k$* are *k* mutually exclusive 

$P(B) = P(B \cap E_1) + P(B \cap E_2) + ... + P(B \cap E_k)$

### Random Variables

-  **Random Variable  =** function that assigns a real number to each outcome in the sample space of a random experiement

  - denoted in capital, like $X$

  - After an experiment is conducted, the measured value of the random variable is denoted by a lowercase letter such as $x$

    **Discrete random variable** = random variable with finite (or countably infinite) range

    **Continuous Random Variable** = random variable with an interval (either finite or infinite) of real numbers for its range

### Probability Distributions and Probability Mass Functions

- **Probability Distribution** = description of the probabilities associated with the possible values of $X$.
  
  -  For a **discrete** random variable, the distribution is often specified by just a list of the possible values along with the probabilities of each
- **Probability Mass Function** = function that gives the probability that a discrete random variable is exactly equal to some value. Given:
  - $f(x_i) \geq 0$
  - $\displaystyle\sum^n_{i=1} f(x_i) = 1$
  - $f(x_i) = P(X = x_i)$
  
  

## Week 3

### Cumulative Distribution Functions

- **Cumulative Distribution Functions** = is the probability that $X$ will take a value less than or equal to $x$

  - $F:\mathbb{R} \rarr [0,1], \forall x \in \mathbb{R}$

  - $F(x) = P(X \leq x)$

  - Suppose that X is a DRV with range $\{x_1,x_2,...\}$. pmf $f(x)$ and cdf $F(x)$. Then $F(x)$ satisfies

    - $\forall x \in \mathbb{R}, F(x) = P(X \leq x) = \sum_{x_i \leq x} f(x_i)$
    - $\forall x \in \mathbb{R}, 0 \leq F(x) \leq 1$
    - $\forall x,y \in \mathbb{R}, \text{if } x \leq y, \text{then } F(x) \leq F(y)$

  - NOTE: if $f(x)$ and $F(X)$ are the ***pmf*** and ***cdf*** of $X$, they are "inter-defineable":

    ​	$F(x_n) = \displaystyle\sum^{n}_{i=0} f(x_i)$

    ​	$f(x_n) = F(x_n) - F(x_{n-1})$

### Mean and Variance of a Discrete Random Variable

- **Mean (Expected Value)** = is the average outcome. Weighted sum of all outcomes with their probabilities

  ​	$\mu = E[X] := \displaystyle\sum_{i=1}^n x_if(x_i)$

- **Variance** = Average distance from the mean 

  ​	$\sigma^2 = V[X] := E[(X - u)^2] = \displaystyle\sum_{i=1}^n(x_i -\mu)^2f(x_i)$

  - Other formula which may be useful:

    $V[X] = \displaystyle\sum_{i=1}^n x^2_i f(x_i) -\mu^2 $

    ​			$= E(X^2)-E(X)^2$

### Binomial Distribution

- **Bernouli Trial** = experiment with *two possible outcomes*; failure or success
  - $p$ - probability trial is successful
  - $(1 - p)$ - probability trial fails

- **Binomial Distribution** = written as $X \sim \text{Bin}(n,p)$, it is experiment where a **Bernouli Trial** is run ***n***-times with fixed probability $p$ of success

  - $n$ - number of trials run
  - $p$ - fixed probability of success
  - trials occur ***independently***
  - $X$ - the number of successful outcomes in the ***n***-many **independent** Bernouli trials

- **Probability Mass Function**:

  - When $X \sim \text{Bin}(n,p)$

    $f(x) = \displaystyle\binom{n}{x} p^x (1-p)^{n-x}$

    - $X$ - $x \in (1,n)$

- **Mean** = $E[X] = np$