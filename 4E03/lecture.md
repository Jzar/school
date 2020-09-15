# 4E03 | Performance Analysis of Computer Systems

**Instructor**: Douglas Down : ` downd@mcmaster.ca`

**Office Hours**:  (instructor) Wednesday 9:30-11:30 will be “open” office hour

**Grading**:

- Midterm 25% (take home midterm) 
- Assignments (weekly)	15% (11, but mark is best of 6)
- Peer-review activities      15%
- Final Exam (2.5 hours)    45%

**Text**: *Performance Modeling and Design of Computer Systems,* **Mor Harchol-Balter** (optional)

**Course Coverage:**

1. Probability Introduction
2. Discrete-Time Markov Chains
3. Introduction to Queuing
4. Operational Laws
5. Simulation 
6. The Exponential Distribution and the Poisson Process
7. Continuous-time Markov Chains
8. Simple queues
9. Multi-server systems
10. Networks of queues
11. Reliability
12. Impact of variance on scheduling 
13. Load Balancing 
14. Applications

## Lecture 2 | A Crash Course in Probability  2020-09-10

- If you do the weekly assignments, the midterms and finals will be simple
  - best 6 of 11; 5 will drop
- Kritik is a tool to enable peer-review actives 
  - Open ended work that is marked by peers

#### Samples and Sample Space

- Suppose we have a data centre that has three servers (A, B, C)
- At any (randomly ) point in time, we look to see which servers are up and which servers are down ( failed) 
- *Experiment*: which servers are up, which are down?
- *Sample Space( $\Omega$*) : set of all possible sample / outcomes 
  - $\Omega$  $=$   \{ \( *w, w, w*),(*w, w, f*), (*w, f, w*), ( *w, f, f*), ( *w, f, f*), (*f,w,w*), (*f, w, f*), (*f, f, w*), (*f, f, f*)}

Where the components indicate if A, B, C, are working ( *w* ) or failed ( *f* )



#### Events 

- An event, $E$ m is any subset of the *sample space* $\Omega$ 
- $E_1$ corresponds to Server A failed:
  - $E_1$ $=$ $\{ ( f, w, w ), (f, w, f), (f, f, w), (f, f, f) \}$
- $E_2$ corresponds to at least two servers failed 
  - *Reminder*: Unions and intersections of events are also events:
  - $E_1 \cap E_2 = \{ (f, w, f), (f, f, w), (f, f, f)\}$  
  - Set of events where Server A and another server failed
- Complement of an event is also an event:
  - $E_{2}^{c} = \{(w, w, w), (w, w, f), (w, f, w), (f, w, w)\}$
  - Set of events where two servers are working

#### Probabilities

- $0 \leq P \{E\} \leq 1$: probability of event $E$ occurring

  ![image-20200910182752221](images/lecture/image-20200910182752221.png)

- The probability of an event, is the sum of its events
  
- $P\{E\} = \sum \{ P\{x\} \| x \in E \}$
  
- Probability of the Union of 2 sets sum of the two sets minus the probability of their intersection

  - If $S_1 \cap S_2 \neq \empty $ , then if we do not subtract the set of intersection from the sum, we will count the events probability twice. Therefore:
  - $P\{E\ \cup F\} = P\{E\} + P\{F\} - P\{E \cap F\}$ 

  ##### Theorem: 

  ##### 	$P\{E \cup F\} \leq P\{E\} + P\{F\}$

  - The Probability of the *union* of 2 events will only be the same when they are *mutually exclusive*, meaning their intersection is $\empty$ , the *empty set* 

#### Conditional Probabilities

- ==**Conditional Probability**== $:=$ The conditional probability of $E$ given $F$ is $P\{E | F\}$
  
  - $P\{E | F\} := \dfrac{ P\{E \cap F\}}{P\{F\}}$
  
    -  $\dfrac{ P\{E \cap F\}}{P\{F\}}$ is also called the ***Conditional Probability Test***
  
  - Note: the denominator (*probability of $F$* ) renormalizes over the new sample space ($F$) and the numerator (*probability of the intersection of E and F*) restricts to samples are are in $E$ *and* the new sample space
  
  - ex. we wish to compute the probability that *A* is failed given that exactly one server is failed
  
    ![image-20200910182720098](images/lecture/image-20200910182720098.png)

#### Independent Events

- **==Independent Event==** : an event is independent if its probability is not affected by whether or not some other event happens

  - Events *E* and *F* are **independent** if:  $P\{E\cap F \} = P\{E\}P\{F\}$

  - $P\{E\}$ does not depend on $F$:

    ![image-20200910183158326](images/lecture/image-20200910183158326.png)
    
    ![image-20200914163120935](images/lecture/image-20200914163120935.png)

![image-20200914163211110](images/lecture/image-20200914163211110.png)

## Lecture 3 | 2020-09-14

#### 

#### Bayes Law

- ==**Bayes Law**== $:=$ $P\{F | E\} = \dfrac{P\{E|F\}P\{F\}}{P\{E\}}$
  - Suppose that we now the probability of $F$ given $E$,  what is the probability of $E$ given $F$?

Ex. 1



Someone is tested for a rare disease. Suppose that the testing methods for the disease are correct **99% of the time** (if one has the disease, the test is positive 99% of the time, if one does not, the test is negative 99% of the time). Suppose that disease occurs in the general population at the rate of one every 10,000 people. 

What are the chances that someone testing positive ***actually has the disease?***

- Event *A*: one has the disease
- Event *B*: one tests positive

$P\{A|B\} = \dfrac{P\{A|B\}}{P\{B\}}$

What have $P\{A\} = 0.0001$ and $P\{B|A\} = 0.99$, but do not have $P\{B\}$. To calculate this probablity, use the *Law of Total Probablity*

![image-20200914164159445](images/lecture/image-20200914164159445.png)

#### Random Variables

- **==Random Variable==** $:=$ a real-valued function of the outcome of an experiment. 
  - Usually denoted $X$
  - Examples
    1. The sum of the rolls of two dice
    2. Number of arrivals to a website by some time *t*
    3. The time until the next arrival to a website
    4. The CPU requirement of an HTTP request
  - 1 & 2 are *discrete*, 3 &4 are *continuous*
  - 2: if *N* is the associated random variable, the we can define events such as *the number of arrivals is less than or equal to five* and *the number of arrivals is between 1 and 3*

#### Distributions

- **==Distribution==** $:=$ $F_{X}(x) = P\{X \leq x\}$
  - Compact way of defining the probablities of events

#### Continuous Random Variables

- For quantities that take on values on a continuum - time is an important one for us

- **Density function** = $f_X(x) = \dfrac{d F_{x}(x)}{dx}$

  ![image-20200914164939589](images/lecture/image-20200914164939589.png)

#### Discrete Random Variables

- ==Probablity mass function== (**p.m.f**) gives the probabilities that the random variables equals values in a discrete set (its range of possible values)

  $p_x(i) = P\{X = i\}$

  

![image-20200914165249800](images/lecture/image-20200914165249800.png)

#### Summary Statistics - Mean

- **==Expected Value (mean)==** $:=$ a predicted value of a variable, calculated as the sum of all possible values each multiplied by the probability of its occurrence.
  	-  **Discrete:** $\sum_i i p_x(i)$
  	-  **Continuous:** $\int^\infin_{-\infin}x f_X(x)dx$ 
- 

#### Variance and Standard Deviation

- **==Variance==** $:= $ $Var(x) = \sigma^2_X = E[ (X - E[X])^2]$

  An important summary statistic is the *variance* which measure the expected deviation from the mean, *how spread out the distribution is*

  - puts more weight on values that are further away from the mean

- **==Standard Deviation==** $:= \sigma = E[X^2] - (E[X])^2$

  - The square root of the variance

### Some Useful Distributions:

#### Geometric Distribution

- **==Geometric Distribtuion==** $:=$ $p_x(k) = q(1 -1)^{k-1}, k \in \mathbb{Z}^+$

  where *q* is the *probablity of success* for an experiment. *1-q* is the *probability of failure*, and $p_x(k)$ is the probability that success first happens on the kth trial. 

  - Arises in applications like testing: if we do **independent tests**, how many tests must be performed before success?
  - $E[X] = \dfrac{1}{q}$
  - $Var(X) = \dfrac{1-q}{q^2}$

#### Poisson Distrubtion

- **==Poisson Distribution==** $:=$ o	

  - a discrete probability distribution that expresses the **probability of a given number of events** occurring in a *fixed interval of time or space* if these events occur with a known *constant mean rate* and *independently* of the time since the last event

    $p_x{k} = \dfrac{e^{-\lambda}\lambda^k}{k!}, k \in \mathbb{Z^{0+}}$

  - Sums to one: $\sum_{k=0}^{\infin}e^{-\lambda}\dfrac{\lambda^k}{k!}$