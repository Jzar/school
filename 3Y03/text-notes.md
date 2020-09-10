# Applied Stats & Probablity for Eng

## Chapter 2: Probability

**Goals**: 

1. Understand sample spaces & events for random experiements via graphs
2. Interpret probablitities and use them to calculate event probablities in discrete sample spaces
3. Permuations and combinatorics
4. Joint event probablities and intersections from probablitilies of individual events
5. Conditional Probablities
6. Determine the independence of events and use independence to caluclate probablities
7. Use Bayes' theorem for Conditional Probablitlies
8. Describe random variables and the difference between continuous and discrete random variables



### 2.1 Sample Spaces and Events

#### 2.1.1 Random Experiements 

**==Random Experiment==** $:=$ An experiement that can result in different outcomes, even though it is repeated in the same manner every time



Randomness can exist in experiments through small variation in variables that are not controlled for in an experiment. This will result in a different outcomes from similar initial conditions.

![image-20200909113429345](/home/jacob/school/3Y03/images/text-notes/image-20200909113429345.png)

- Statistical models need not be perfect abstractions: ( Newton's Laws are not perfect)
- Given a mathematical abstraction that is validated with measurements from our system, we can use the model to understand, describe, and quantify important aspects of the physical system and predict the response of the system to inputs.



#### 2.1.2  Sample Spaces

**==Sample Space==** $:=$ The set of all possible outcomes of a random experiment

- **discrete** if the set is *finite* or *countably infinite* 					ex. R^+^
- **continuous** if it contains an interval of real numbers

#### 2.1.3  Events

**==Event==** $:=$  A subset of the *sample space* of a random experiment

- often we are interested in collections of outcomes from a random experiment

**Events** can be described of in terms of each other using set operations, such as :

- *union* : set that consists of all elements contained in both sets 			$S_1 \cup S_2$
- *intersection**: set that consists of all elements that are not contained in both of the sets    	$S_1 \cap S_2$ 
- *complement*: the complement of an ***event*** in a ***sample space*** is the set of outcomes in the sample space that are not in the event.                 $S_1'$ 

`

###### **==Mutually Exclusive==** $:=$  A subset of the *sample space* of a random experiment