# 4HC3 | Human Computer Interactions

## Lecture 1 : Meta Lecture / Syllabus - 2020-09-10

**Instructor**: Kevin Browne `brownek@mcmaster.ca`

- PhD in HCI
- Master done @ IBM
- Software Hamilton, Hamilton Code Clubs, The Forge



==**Human Computer Interfaces**== = space where interations between humans and computers occurs

- Intersections of: *Computer Science, Pyschology, Graphic Design, Business, Ergonomics*

**Course Coverage:**

- UI Design Goals
- Mockups, wireframing, prototyping
- Users, tasks
- User Research
- Accessible Design
- Design heuristics, principles, theories
- Design thinking
- User interface design processes
- Testing user interfaces
  - Usability testing
- Implementing user interfaces
  - Technologies, related architectures when relevant
- User help (videos, manuals, etc)
- HCI research & case studies

**Technologies:**

- HTML and CSS
- JavaScript
- ReactJS
- No back-end code required

Coverage of game engines, mobile app dev, and other technologies will occur --- popular interfaces will be discussed in class

**Breadth** not **depth** course



**Mark Breakdown**:

- Assignments 				35%
  - 7 assignments x 5% each
- Projects                          35%
  - Milestones with different weights over term
  - Individual or group
- Final Exam                     30%

## Lecture 2 | UI Design Goals - 2020-09-10

### Real World Example

Why do you think the design for this telephone performed better than a rotary phone?

![image-20200917140203469](images/lecture/image-20200917140203469.png)

![image-20200917140225462](images/lecture/image-20200917140225462.png)

**Smaller learning curve**, easier to use, don't need to use rotary dial

### UI Design Goals

- There are ***many*** potential goals for user interfaces, together they make up usability

  - usability is more than "easy to use"

- We can organize these goals in different taxonomies, i.e. categorizations

  

  We'll use a taxonomy of **8** **goal categories** largely dervied from the taxonomy use by *Ben Schneiderman*

#### 8 Design Goal Categories

- **==Learnability==** - How easy is it for users to accomplish *basic tasks* the **first** time 

- **==Retention==** - When users *return* to the design after a period of time, how easily can they **re-establish proficiency**
  - Can call this goal ***memorability***

- **==Performance==**s - Once users have learned the design, **how quickly** can they perform tasks?
- **==Error Rates==** - **How many** errors do users make? **How severe** are these errors? **How easily** can they *recover* from the errors?
- **==Subjective Satisfaction==** - **How pleasant** is it to use the design?
- **==Accessibility==** - **How accessible** is the interface to users with different disabilities?
- **==Functionality==** - **What range of operations** does the user interface support
  - *How much is can do* **not** how well it can do its functions
- **==Trustability==** - How much **do users trust** the interface?

#### UI Design Goals vs Requirements

- **Functional requirements** $:=$ the required behaviours of a system (i.e. what it can *do*)

- **Non-Functional requirements** $:=$ criteria by which to judge operation of a system

- UI design goals are closely related to the idea of **non-functional requirements** (aka **quality** **attributes**)
  - UI Design goals are a subset of non-functional requirements
  - Though functionality (range of operations)
  - Specific goals might be captured with tangible requirements

#### UI Design Goal Taxonomies

- Another common taxonomy comes from "*Ergonomics of human-system interaction*"(ISO 9241-11:2018)
  - **Effectiveness**
  - **Efficiency**
  - **Satisfaction**
- Usability is defined as "the extent to which a system, product or service can be used by specified users to achieve specified goals with **effectiveness, efficiency and satisfaction**"

We can specify other categories of goals, for example:

- **Safety** : how safe is the system for users
- **Understandability**: How easy is it to understand the system?
- **Responsiveness**:  how long does it take to complete tasks?

Most categories can fall under one of our existing categories:

- **Safety** is a category of **error rate**
- **Responsiveness** is a form of **performance**
- **Understandability** is tied to **learnability** 

### Trade-Offs

- **Trade-offs** occur when we sacrifice quality in one goal to improve quality for another goal
- For virtually all user interfaces of enough sophistication, trade-offs become necessary
  - The trade-offs may not be though about consciously, they may occur implicitly, but they exist
- Making the "right" trade-off decisions is critically important to the success of a system



ex. Wifi Hotspot menu in iOS or Android

- Less options; more decisions made for you

  | UI Design Goal | Android                                 | iOS                                     |
  | -------------- | --------------------------------------- | --------------------------------------- |
  | Functionality  | more options, more ability to customize | fewer options, decisions made for users |
  | Performance    | Need to                                 |                                         |
  | Error Rates    |                                         | won't allow you to mis-configure        |

  

### Measuring Goals

- Important for us to be able to measure goals
  - To know if we are improving an interface or not 
  - To compare interfaces with one another objectively 
  - To write requirements that can be verified 
- Not straight forward though...
  - What performance measures and error rates matter from one system to the next?
  - How do we measure subjective satisfaction, learnability, trustability, and less objective goals?

#### Performance 

- How **long** it takes a user to perform a task
- Number of clicks/taps required to perform a task
- How many tasks can a user accomplish in a time period?



#### Error Rates

- **Errors per task**, **errors per time period**
- *Success rate* at completing task

#### Subjective satisfaction, trustibility

- Surveys can help make it objective
  - "I liked using this interface" with Yes/ No responses
  - Likert scale questions
    Pick from different options (Strongly disagree, agree, etc. 1-N for N categories)

#### Learnibility & Retention

- Perform an experiment 
  - Ask users who have never seen interface before to perform a task
  - Measure how long it takes 
  - Compute an average 
  - Repeat same process a month later

Measuring goals is very related to testing user interfaces, a toopic we'll dive into more later

- A host of techniques exist to test interfaces, which ***themselves*** have trade-offs in terms of their performance, ease of use, etc.

- Suffice to say it is possible to measure goals, even realtively subjective ones

## Lecture 3 | User Interfaces Prototyping - 2020-09-11

### User Interface Prototyping

- **==User Interface Prototyping==** = iterative development technique in which interface **sketches**, **wireframes**, **mockups** and **prototypes** are created
  - Users themselves are typically active in the process of *creating* and *evaluating* these design artifacts

**What's the difference?**

- Often, the above terms are used interchangeably. For the purpose of the course, they will be defined as follows:

#### Sketches 

![image-20200911114110272](images/lecture/image-20200911114110272.png)

- **==Sketches==** $=$ are hand-drawn representations of user interface designs
  - Sketches have ***virtually zero barrier to entry***
    - Even a non-technical customer/user can sketch
    - Anybody can sketch
  - Sketches are very **low fidelity** 
    - Prototyping methods often ranked from low fidelity to high fidelity
    - Lower fidelity means low lovel of detail 

#### Wireframes

![image-20200917143909157](images/lecture/image-20200917143909157.png)

- Wireframes accurately represent interface page layout and organisation of content
  - But lack colour, typography, images and graphics
  - i.e. ***blueprints***
- Increased *precision* over sketches and use of software makes wireframes less accessible than sketches
- More time consuming to create than sketches, but relatively ***higher fidelity***

**Wireframe** = structure + functions + content 

#### Mockup

![image-20200917144004929](images/lecture/image-20200917144004929.png)

**Mockup** = static but accurate representations of the application interface

- Colour, typography, and graphics *should* be included
- Mockups are not interactive, cannot click and perform actions
- Equivalent to screen captures

Much more time consuming than wireframes, but very high fidelity

#### Prototypes

- Prototypes are an accurate ***and*** iteractive representation of the application interface
  - We can perform actions in a prototype and the result should be the same in the full working application
- Difference between prototype and completed application?
  - Not connected to a back-end and the logic is hardcoded
- Highest fidelity, and most time intensive to create
- Created with the same tools as the completed application
  - HTML, CSS, JavaScript, etc.
- They may also be created with purpose built tools that allow for code-free experiences
- **Fully functional in terms of UI**



![image-20200917144046159](images/lecture/image-20200917144046159.png)

#### Tools

- Sketches:
  - Pen, paper, whiteboard
- Wireframes
  - wireframe.cc
  - draw.io
- Mockups
  - GIMP
  - HTML,CSS
- Prototypes
  - Sketch, Proto.io, Moqups
  - HTML,CSS,JavaScripts

#### Cost vs. Fidelity

![](images/lecture/image-20200917144133597.png)

### Where Do CS/SE Experts Fit?

**Professor's opinion:**

- CS & SE grads work in the *prototyping stage* 
- **Freelancer or startup**: Maybe every stage!
- Specialized roles
  - Business/client focused roles  - **sketches** with client
  - UX experts, graphic designers creating **wireframes** & **mockups**
  - CS/SE experts doing **interactive prototype** -- *focusing on the interactivity!*
- Traditional wireframe is the *most likely* to be skipped

### Course Focus:

- *Some* **wireframes** and **mockups**
  - Importance in understanding how they work / how to build one
- Focus will be on ***interactive* prototypes**
  - Connects naturally with testing of user interfaces which is another common area for CS/SE experts

## Lecture 4 | User Analysis - 2020-09-15

### User Analysis

- **==User Analysis==** = determining *what* **characteristics** of our users may incluce the design of an interface

  - Closely related to, *but distince from* **task analysis**
  - **Task analysis** = analysis of how user tasks are performed to influence the design of our interface

  **User analysis** and **Tasks analysis** are often done together to *inform* and *guide* **user interface design**

  - Both take place *before* design takes place
  - **Users** and their **tasks** can vary in many different ways

### User Diversity

#### Physical Abilities

- ***Antrhopometry*** studies human body measurements
- **Perception** abilities
  - Vision-related: *low vs. bright* light, colours, response times, depth perception, visual aids
  - Similar concerns to hearining abilities

#### Cognitive Abilities

- Classifications by the *journal of Ergonomics Abstracts*
  - **Short term** and **working memory**
  - **Long term** and **semantic memory**
  - problem solving and reasoning
  - decision making and risk assement
  - language communication and comprehension
  - search, imagery, and sensory memory
  - learning, skill development, knowledge acquisition and concept attainment
- Most adults can hold 7 $\pm$  2 in their shortterm memory (Miller, 1956)
  - Makes a range of 5-9 menu items ideal

#### Personalities

- Different taxnomies and ways to measure exist with lively debates
  - eg. Myers-Briggs: contreversial as psedueo-science 

- Some interfaces allow users mulitple way to organize information
  - Designing for different *types* of users

#### Cultural 

- Beyond language translation, there are many other concerns when presenting information:
  - Titles like Mr. , Mrs, etc.

#### Users with Disabilities

- Vision Impairments
  - Screen readers
- Hearing impairments

##### Accessibilitiy Guidelines

- Web Content Accessibility Guidelines (WCAG)
- Accessibility for Ontarians with Disabilities Act (AODA)



#### Age

- **Seniors**
  - Physical, cognitive abilities generally declining
- Accommodating Seniors
  - Larger font-sizes
  - Larger buttons
  - Text description underneath icons
    - Icons meaningful to 20-40 year old people may not be meaningful to 90-year olds
    - May not be meaningful for younger individuals as well, **e.g.** Floppy disk save icon
  - Touchscreens over mouse interface
  - Autocomplete word/search suggestions
    - This was originally inspired by accommodating seniors
  - Lower congitive loads
    - Present less options, less information, simplified layouts

- **Children**
  - Age-limited abilities, e.g. reading, comprehension
- Accommodating Children
  - Fostering curiosity, intrinsic motivation
  - Safety concerns
  - Dexterity and other abilities
    - Can they be expected to drag, double-click, etc.
    - Attention span

#### Devices

- High speed vs low speed internet access
  - Are users with lower speeds accommodated?
  - Techniques exist to allow web server to send *smaller* images to certain users
- Display size & resolution
  - Smartphones with 3.5" screens vs. desktops with 27" screens
  - Resolutions from 640x480 to 4k
  - **Responsive design** is key
- Inputs: *touchscreen* vs. *mouse & keyboard*

### Universal Design

- **==Universal Design==** =  *design of products and environments to be usable by all people, to the greatest extent possible*
  - Can you really design for everyone? YES: wheel chair ramp, push to open doors
- Removing mouse-only interactions such as "hover to see information"
  - Helps users with vision or motor impairment, but now you can use the webapp on the phone
- High contrast information display
  - Helps users with vision impairment, *but* also helps other users when they are in sunlight
- Alt text on images
  - Helps users who use screen readers, but also helps you when bandwidth speed is too slow to send image

#### Users and Design

- Universal design as a general philosphy is virtually always good to practice, and to keep "top of mind"
- However, you **cannot** design for everyone all the time
  - Eg. when you have a *target user* 
    - Will our decisions about design be optimal if we're always considering every possible user equally?
- **User analysis** allows us to better understand our uses to influence our design for them

#### User Research

- **==User Research==** = focuses on understanding user behaviours, needs, and motiviations through observation techniques, task analysis, and other feedback methodologies
  - Technically done before design exists



##### User Research Techniques

-  Individual interviews with users

  - Use a script, be informal, both

- Focus groups

  - Feedback from small, diverse groups
  - Often informal but moderated discussions

- Personas

  - Creation of a representative user based on available data and user interviews
  - Fictional person, age, personality type, goals, what they're frustrated about
  - Person that you are specifically designing for that are representative of your average user-base
  - e.g. teams would have student persona, professor persona

- Use cases

  - Wirtten descriptions of how users will perform tasks
  - Include user's goal(s) steps or subtasks, how the UI can work
  - UML diagrams

- Card Sorting

  - Card sorting helps us to answer the question: 

    What information is, or ***should*** be associated with what other information

  - Helps us to arrange website menus, workflows, navigations

  - Process

    1. A person representative of the audience receives a set of index cards with terms written on them
    2. This person groups the terms in whatever way they think is logical, and gives each group a category name, either from an existing card or by writing a name on a blank card
    3. Testers repeat this process across a group of test subjects
    4. The testers later analyze the results to discover patterns

##### Interviews vs. Surverys

- Interviews and focus group
  - high cost/time commitment per user
  - Far less anonymitity

## Lecture 5 | Task Analysis / Divergent & Convergent Thinking -  2020-09-17

### Task Analysis

- **==Task Analysis==** = the analysis of how **user tasks** are performed in order to influence the design of our interface
  - **User analysis** and **task analysis** are often done together to infrom and guide user interface design

### User Domain Knowledge

- How much **expertise** does the user have that is *relevant* to the interface's **problem domain**? 

Common breakdown: **beginner v. expert**:

- **Beginners** sometimes called "novice users"
- **Experts** sometimes called "power users"
- Beginners are new to a task, experts have comprehensive knowledge

In reality, its ***very much a spectrum***

- **Intermediate users** are more advanced, but not experts and make the majority of most user bases

How can we accomodate both types of users?

ex. *Additional / Advanced Settings*

![image-20200917150047434](images/lecture/image-20200917150047434.png)

### User Roles

- The same system can have *groups* of **users** with defined roles
  - **user** vs. **admin**

![image-20200917150213846](images/lecture/image-20200917150213846.png)

### Ethnographic Research

- **==Ethnographic research==** = Qualitative user research method based on observing users in their real-life environment
  - Embedding yourself on the factory floor and *observing all roles*; what they involve
  - We can user **interview**, **surverys**, and other **user research methods** to inform **task analysis** too
  - **Ethnographic research** can be especially effective for discovering **user roles**, **workflows**, and **tasks**

### Tasks

- **==Task==** = **goal** directed *behaviours* or series of *behaviours* involving the user interface
  - often **hierarchical** and represented in a ***tree structure***
  - Often made up of **subtasks** which themselves can have subtasks
  - Sometimes the terms **goals**, **activities**, and **process** are used instead of "***tasks***"
    - top level **task** may be referred to as a **goal**

**Note:** whenever possible, try ***not*** to refer to the interface, especially specifics about the interface, when creating tasks

- ex. "Finding directions from Hamilton Ontario to Ottawa, Ontario"
- Goal directed activity, but no reference to *how* the task is accomplished in the UI
- ***Informs*** design **does not** define it

#### Task and Subtask example

- Search the store for products
  1. Filter search results by category
  2. Filter search results for sales
  3. Sort search results from lowest to highest price
  4. Sort search results from highest to lowest price
- In the above, we have a task and 4 subtasks
  - Notice that we don't make reference to the UI or how they are achieved

#### Conducting Task Analysis

- Question to think about:
  - **What** makes users *begin* a task?
  - **How** do users *complete* a task?
  - **What** information do users need to *complete* the task?
  - What **tools** do users need to *complete* the task?
  - Do the subtasks have an **order**?
  - **How** do users know **when** a task is *complete*?

Try to limit a task's subtasks to **4-8*** subtasks

- If there is more, it suggests that the hierarchy may require more layers

#### Hierarchical Task Analysis

- **==Hierarchical Task Analysis==** = form of task analysis
  - In addition to a **task hierarchy**, adds concepts of ***operations*** and ***plans***
- **==Operations==** = actions performed by the user. They are the subtasks which cannot be broken down further
  - Basic unit of task
  - Action does not mean "click X", its still at a higher level of abstraction
  - "sort by X", etc
  - **All** bottom-level tasks should be ***operations***
- **==Plans==** = How tasks are to be carried out; defined ordering of operations
  - First x, then y, then z

**Process:**

1. **Define task being analysed:** as well as the purpose of the **task analysis**

2. **Conduct data collection**: Pay particular attention to areas such as *technology*, *machine* and *team member* iteration, decision making, and *task constraints* to better understand the **process*

3. **Determine the overall goal of the task**: This should be in place at the top of the **task hierarchy**

4. **Determine Task Sub-Goals**: Decompose the overall goal into *corresponding* **sub-goals**. Together, these subgoals should comprise the tasks necessary to accomplish the overall goal

5. **Perform Sub-Goal decomposition**: Subgoals should be further broken down into *additional* **subgoals** and **operations**.  Continue this process until you reach an appropriate operation, which specifies the action that actually needs to be done to accomplish the goal. There should always be an operation at the bottom level of *any* branch in a **HTA**

6. **Develop Plan Analysis**: After describing all the subgoals and operations, add the plans. Plans explain how a goal should be accomplished. These may be in the format "do A, do B, do C"

   

### Divergent & Convergent Thinking

- **==Divergent Thinking==** = Thought process or method used to *generate* creative ideas by exploring many possible solutions

  - Quantity over quality
  - Novel ideas
  - Creating choices

  Similar to **brain storming**

  - "Right-Brain"
    - Creative, Artistic, Solution generating

- **==Convergent Thinking==** = Though process or method to make a *deliberate* and *conscious* choice. We purposefully apply criteria as we screen, select, evaluate, and refine options

  - Analyse and filter
  - Useful ideas
  - Make decisions

  Similar to **analysis and judging**

  - "Left-Brain"
    - Logical, Analytical, solution reducing

![image-20200917152708077](images/lecture/image-20200917152708077.png)

#### Design Thinking

Convergent thinking and divergent thinking are often used as part of **design thinking**

- **==Design Thinking==** = design process and set of related tools for creative problem solving
  - We'll talk more about design processes for user interface design later.. there are others

![image-20200917152841855](images/lecture/image-20200917152841855.png)

![image-20200917152914664](images/lecture/image-20200917152914664.png)



#### Thinking Divergently

- **Brainstorming**
  - Classic un-directed brainstorming, just write down whatever you think
- **Journal**
  - Keep a journal of ideas to write them as they occur
- **Freewriting**
  - Write freely without structure or stopping 

- **Mindset**
  - Research shows we think divergently best when we are *happy, feel less pressure, less anxiety, well-rested*

- **Oxymoron**
  - Explore what happens when you remove what's most essential about a product or concept to generate new ideas
- **Arbitrary Constraints**
  - Set constraints and create designs within them
  - Forces more creative thinking
- **Brainwriting**
  - Have everyone write down their own brainstorm, then share together afterwards
  - Helps negate groupthink or going down a sub-optimal path
- **Lateral Thinking** - solving illogically
  - Random entry idea generating tool
  - Provocation
    - Say something provocative to motivate ideas
  - Disproving
    - Take a popular idea and try to disprove it
- **Scamper**
  - **Substitute**: come up with another topic that is equivalent to present the topics
  - **Combine**: adds information to the original topic
  - **Adjust**: identifies ways to construct the topic in a more flexible and adjusted material
  - **Modify**: Magnify,magnify, creatively changes the topic or makes a feature/idea bigger or smaller
  - **Put**: to other uses uses identifies the possible scenarios and situations where this topic can be used/implemented
  - **Eliminate**: removes ideas or elements from the topic that are not valuable
  - **Reverse**: rearrange, evolves a new concept from the original concept

#### Inspiration

- Search for solutions similar to the problem you are solving
- Note and categorise the different design features that the solutions are using
- Attempt to combine these design features in new ways relevant to your problem

## Lecture 6 | UI Design: Guidelines - 2020-09-22

### UI Design Recap

- *Sketches/wireframes/mockups/prototypes* **represent** our design
- **User analysis** and **Task analysis** *inform* and *influence* our design
- **Divergent thinking** helps us *create* and *explore* design space
  - **Convergent thinking** is where we *make* **design decisions**

Begs the question: ***how*** and ***why***? 



### Design Decisions

- **==Design Decisions==** = decisions we make during the design of an interface
  - ex.
    - Font / Font size
    - Layout
    - Colour
    - Input

##### *Making* Design Decisions

**Strategies:**

- **Intuition**: How do you know its a *good* design decision though?
- **Experience:** How do you know there isn't a *better* way?
- **Reference:** Is what *others* are doing the *best* way?
- **Consensus:** Is the *crowd always right*? How to account for *group think?*

**Consider:** how would you feel about using a **bridge** built on *intuition*? What about major        **surgery** based on *consensus*?

- UI design *guidelines,principles,* and *theories* can also help us to guide **design decisions*
  - Many are based on *empirical evidence*, though some are based on industry-wide experience, or other reasoning
- Guidelines, principles, and theories can offer a more solid basis for many of other design decisions
  - But they *can't* make **all** of our decisions for us

### Guidelines, Principles, and Theories

#### Guidelines

- **==Guidelines==** = provide **low-level** advice about good practices and cautions against dangers
  - **Do's and don't's**
  - Tend to be specific to *application, device, or part of UI*

##### Examples

- **Standardise task sequences:** allow users to perform tasks in the *same sequence* and manner across similar conditions
- **Ensure that links are descriptive:** When using links, the link text should accurately describe the link's destination
- **Use unique and descriptive headings:** Use headings that are distinct from one another and conceptually related to the content they describe
- **Use radio buttons for *mutually exclusive choices:*** When you need to choice one option
- **Develop Pages that will print properly:** If users are likely to print one or more pages, develop pages with dimensions that print well
- **Use thumbnail images to preview larger images:** When viewing full-size images is not critical, first provide a *thumbnail* of the image
- **Increase Web Site Credibility:** Provide a ***FAQ***. Show the author's credentials. Provide citations. Ensure the site is frequently linked by other credible sites.
- **Reduce the user's workload:** Allocate functions to take advantage of the *inherent respective strengths*

- **==Principles==** = are **middle-level** strategies or rules to *analyse* and *compare* **design alternatives**

- **==Theories==** = are **high-level** , *widely applicable* frameworks to draw on during design and *evaluation*. 

  - Useful to support communication and teaching
  - Can also be *predictive*, such as those pointing times by individuals or posting rates for community discussions

  

## Lecture 7| UI Design: Principles & Error Message Guidelines - 2020-09-24

### Principles

- ==**Principles**== = **middle-level** strategies or rules to analyse and compare design alternatives
  - more *abstract* and require more interpretation than guidelines
  - more *enduring* than guidelines: (**not** specific to OS, or device)

##### 8 Golden Rules of Interface Design - (Ben Scheindermen)

1.  ==**Strive for Consistency**==

   - Similar sequences of actions for similar situations
   - Use identical terminology across the application
   - Limit the number of exceptions to consistency, ensure they are comprehensible 

2. ==**Seek Universal Usability**==

   - Account for user characteristics (*age, language, culture*)

   - Account for **beginner** to **expert** users

     - explanations, shortcuts or performance enhancements

   - Design for transformation of content (text represents all media)

     ![image-20200924114720693](images/lecture/image-20200924114720693.png)

3. ==**Offer Informative Feedback**==

   - Interface should provide feedback for user actions

     - How do users know their action has been registered?

       ![image-20200924114849951](images/lecture/image-20200924114849951.png)

   - Feedback should be *inline* with the **frequency** and **importance** of the action 

     - Minor, frequent actions can provide modest responses
     - Major, infrequent actions can provide more extensive responses

4. ==**Design Dialogues To Yield Closure**==

   - After a series of actions, give users a sense of **closure** with information feedback

   - Sequences of actions should have an organization from beginning, middle, to an end with closure

     1. Select report type
     2. Enter in details regarding report 
     3. Produce report and present to user

     ![image-20200924115030618](images/lecture/image-20200924115030618.png)

5. ==**Prevent Errors**==

   - Where ever possible, design the interface such that users ***cannot*** make mistakes
   - If user make an error, interface should provide clear and constructive instructions ***to fix it***
   - Preventing errors
     - Disable or "grey out" options that aren't relevant
     - Don't allow airplane engines to go in reverse unless the landing gear is down
   - Force complete sequences of actions
     - Either automate a series of actions after a user action
     - OR make sure user *finishes* a sequences of actions
       - If left half complete, have an alert to user to finish it

6. ==**Permit Easy Reversal of Actions**==

   - Wherever possible, **make actions reversible**
   - Allow users to feel confident trying things
   - Allow reversal of single actions but also groups of actions

7. ==**Keep users in Control**==

   - Users should always have sense that they are in control ***especially*** more experienced users
   - Users **lose** control if:
     - Cannot produce a desired result or obtain required information
     - Are forced to go through a lengthy data entry process
     - Interface behaviour change unpredictably
   - Let users *skip* over content, move back and forward through a process, etc.

8. ==**Reduce Short-Term memory load**==

   - Users shouldn't need to remember information on one page and then use it on another
   - Don't exceed the 7 $\pm$ 2 rule of short-term memory
   - Break up lengthy forms and processes into logical subforms and processes

#### Another Principle...

- 8 Golden rules aren't the only principles
- Another principle: **Ensure human control while increasing automation**
- Increase automation of tasks as much as possible, and in the ways that **machines perform better**, but ensure **human control** is maintained, especially in the ways *humans* perform better

| Human                                                      | Machine                                       |
| ---------------------------------------------------------- | --------------------------------------------- |
| Draws on strengths and experiences and adapt to situations | Rapid consistent response for expected events |
| Select alternatives when first approach fails              | Process data with anticipated patterns        |
| Make subjective value based judgements                     | Perform repetitive actions reliably           |
| Develop new solutions                                      | Perform several actions simulataneously       |
| Request help other humans                                  |                                               |



#### Ensure Human Control While Increasing Automation

- *Routine*, *predictable* tasks are generally better given to machines when possible
  - Humans will get tired, make mistakes, etc.
- Unpredictable and novel tasks are generally better given to humans when possible
- The curve is always shifting on this trade-off
- Air traffic control
  - Much of the system of air traffic control is automated and for good reason
  - What about a plane needing an emergency landing?
  - What about a closed runway?
- Air plane disasters sometimes occur from *too much automation* and not enough human control

### Error Message Guidelines

#### What are the characteristics of *good* error messages?

- Make errors **explicit** and **clear** that it is an error that has taken place
- Make them visible
- **Don't** change application state too much in response
- Place error message close to where the error has taken place
- Text should target the *user* **not** the *programmer*
- **Don't** blame the user, if anything, **blame the app**
- ***tell the user how to fix the error!***
- user "warmer" language, colour, and iconographpy
- Does the error ***really*** need a big red X or stop sign? Do you even need the *word* error?
- User humour! Humour can ease anxiety, and a delightful surprise instead of a pain point
  - Don't go too far this can quickly cross over into being patronising to your user

## Lecture 8 | UI Design: Component-based Front-end Architecture 

### Why Component-Based?

- Basic computing and software principle: 

  - To build programs *that will scale*, we need to **separate** our code into different **modules** with *different concerns*
  - **separation of concerns!**

- We **sort of** get this with HTML, CSS, and JS

  - HTML - structure
  - CSS - style
  - JavaScript -behaviour
  - And we ***can*** further subdivide into different CSS files, include external libraries, etc.

- But in practice, this approach only scales so far .... 

- More **interactivity** means more **DOM** manipulation

  - Querying tags based on IDs and classes and writing code that's all about sticking data inside them
  - As opposed to code focused on layout, or structure, or solving our problem ... this type of code is some of the worst to write
  - This isn't what HTML DOM was built for originall either, JS does this because it's needed, but its a bit hacky

- DOM manipulation is ***expensive***:

  - Causes browser to re-render
  - Modern apps have ***VERY*** complex DOM trees ... hundreds of thousands of nodes, higher than ever tree depth, etc.
  - Making many small DOM changes is ***not*** ideal

- Let's say we make a "news feed" for Facebook profiles with HTML, CSS, JavaScript

  - because we need the same news feed for groups, how do re-use that functionaility
  - Not as easy as you would hope...
    - We can use a technique called "HTML templating" on our server to help with this, constructing pages made up of HTML templates glued together and sending them
    - Doesnt **scale** in terms of maintainability, we can end up with spaghetti code very easily

- **Single Page Applications (SPA)** are a type of web app that only do one initial page load of HTML, CSS, and JavaScript

  - Subsequent data or content that is needed is fetched by having JavaScript communicate with the server using:
    - AJAX - http requests done in the backend
    - WebSockets - bi-directional communication tech
  - From the user's perspective, the ***entire page never refreshes***

- **SPAs** provide a superior user experience

  - Entire page doesn't reload in-response to actions
  - Imagine if our phone and desktop apps did this 
  - Leads to higher subjective satisfaction for users

  **Trade off:** SPAs more technically difficult to build

  **component** **based** *is more suited towards SPA*

- For more on "why" we use them...

  - Does your web app need a front-end?

- Component-based frameworks developed in response to these problems

  - Tread DOM manipulation completely differently
  - Completely different separation of concerns
  - ***allow for creation of reusable components of functionality***

### Traditional Multipage Applications

![image-20200925114026586](images/lecture/image-20200925114026586.png)

### Single Page Application

![image-20200925114059011](images/lecture/image-20200925114059011.png)

### Big 3 Component Based Frameworks

1. Vue
   - Easiest to learn, super elegant code, instructor's favourite
2. Angular
   - Widely used, but has a "split ecosystem" between incompatible older and newer Angular version, documentation and learnabililty relatively harder 
3. React
   - Only slightly harder than Vue to learn, widely used in industry and we get React Native as a bonus

#### React

- Front end JS framework for interactive UI
  - Developed in 2011 at Facebook
  - Opensourced in 2013

##### Virtual DOM

- **Virtual DOM:**

  - lightweight abstraction of the DOM
  - essentially keeps a local and simplified copy of the DOM as part of its operation

- **Change in App State:**

  - does a *diff* between the last virtual DOM render
  - Handles any required DOM updates efficiently

- **Rendered** onto DOM at a specific element

  - From there, React controls the DOM at this element

  - In below example, `<h1>Hello,world!</h1>` is being **rendered by React** *into the div with id root*

  - `<h1>Hello, world!</h1>` may *look* like HTML, but its actually **JSX** code

    ```react
    <div id="root"></div>
    <script type ="text/babel">
    	ReactDOM.render(
        <h1>Hellow, world!</h1>,
        document.getElementByID('root');
        )
    </script>
    ```

    

#### React Components

- We can create **components** like this:

  ```react
  class MyComponent extends React.Component{
      render() {return <h1>Hello world</h1>}
  };
  ```

  

## Lecture 9 | Theories - 2020-09-29

### Theories

- **==Theories==** = **high-level**, widely applicable frameworks to draw on during **design** and **evaluation** as well as to support **communication** and **teaching**
  - can be *predictive*
  - more *abstract* than **principles** and **guidelines** and require *the most* interpretation

### Fitts' Law

- ==**Fitts' Law**== = Predicts that the time for a user to point to a target area is a ***function of the width of the target*** and ***the distance to the target***
  - Scientific Law discovered by *Paul Fitts* through experimentation in 1954
  - Targets that are **bigger** and **closer** to where the user is currently pointing will be *faster* for a user to interact with
  - Targets that are **smaller** and **further** will be *slower* for a user to interact with
- One of the most **objective** and **concrete** concepts in design
  - Tested over decades
  - Reproduced many time
  - Holds for "pointing device", whether its controlled with finger, mouse, joystick, eyes, tongue, etc.

##### Example

Which button will the user reach first with their cursor in this position? Why?

![image-20200929113553532](images/lecture/image-20200929113553532.png)

#### Formalisation

​	==$ID = log_2(\dfrac{2D}{W})$==

​	$ID - $ index of difficulty

​	$D - $ distance from the starting point to the target centre

​	$W - $ width of the target 

##### Computing Mean Pointing Time

**Variables:**

- $MT - $ mean time

- $a,b - $ constants dependent on input device

- $ID - $index of difficulty

- $D -$ distance from the starting point to target centre

- $W -$ width of the target

$MT = a + b * ID = a + b * log_2(\dfrac{2D}{W})  $

#### In Practice

- Designers generally aren't computing values with these equations
  - Instead, the core idea behind Fitt's law is used to inform design decisions
  - Ex. OS X Common Menu Bar
- Group buttons that are likely to be used together
  - Think: rewind, play, pause, fast forward
  - Sometimes play even turns into pause and vice versa
- Have an option that's ***bad*** or ***dangerous*** for the user?
  - Keep it *far away* from the main group of buttons
- Corners of the screen will always be fast to reach
  - Start button, OS X apple icon
- Position near the corners of the screen, but not the corners, will take the longest to reach
  - ***least valuable screen space***

### Norman's 7 Stages of Actions

- Users undergo these stages while interacting with an interface
  - ***cyclical pattern***

1. ***Forming* the Goal**
2. **Forming the Intention**
3. **Specifying the Action**
4. **Executing the Action**
5. **Perceiving the System State**
6. **Interpreting the System State**
7. **Evaluating the Outcome**

#### Norman's Definitions

- **mapping** = relationship between the elements of two sets of things
  - mapping between light switches and lights
- **conceptual model** = an explanation, usually highly simplified, of how something works
  - eg. folder and file icons
- **feedback** = communication about the results of an action
  - when you hit a button and button lights up / vibrates
- **system image** = is the combined information available to the user
  - ***complete picture***
  - What the interface looks like
  - How similar interfaces work
  - Instruction manual
  - Sales and marketing videos and images

##### Examples

Excellent conceptual model usage

![Excellent conceptual model usage](images/lecture/image-20200929115915483.png)

vs. how it was handled during the pandemic: conceptual model broke down!

![image-20200929120037430](images/lecture/image-20200929120037430.png)

#### Four Principles of Good Design

Principles suggested by Norman based on **7 Stages of Action**

1. The **state** and the **action** alternatives should be *visible*
2. There should be a *good* **conceptual model** with a *consistent* **system image**
3. The **interface** should include *good* **mappings** that reveal the relationships between stages
4. **Users** should receive *continuous* **feedback**

#### Gulf of Evaluation

- **==Gulf of Evaluation==** - degree to which the interface provides representation that can be directly perceived and interpreted in terms of the expectations and intentions of the user
  - ie. the **gulf of evaluation** is the *difficulty* of assessing the **state of the system** and *how well* the interface supports the discovery and interpretation *of* that **state**
- "The gulf is small when the system provides information about its state in a form that is easy to get, is easy to interpret, and matches the way the person thinks of the system"

#### Examples

- What if your OS ***did nothing at all*** when transferring files between folders?

  - Poor gulf of evaluation, you won't know what to expect

- What if instead your operating system showed a spinner or hourglass

  - You would at least know ***something*** is happening, ***some*** system state is reflected, but you wouldn't know ***what*** is happening

  

### Gulf of Execution

- ==**Gulf of Execution**== - degree to which the **interaction possibilities** of an interface *correspond* to the **intentions *of the person*** and *what* the person perceives is **possible** to do with the interface
  - ie. the difference between the **intentions of the user** and ***what the system allows them to do*** OR *how well* the **system** *supports* those actions
  - Not clear to the user on how to do what they want to do 

### Affordances

- **==Affordances==** - are the action possibilities that are readily perceivable by an actor 
  - (Norman, 1988)
  - Eg. handle on a kettle makes it readily perceivable to the user that they can hold the kettle by the handle
- ==**Affordances**== - are a relationship between the properties of an object and the capabilities of the agent that determine just how the object could possibly be used
  - (Norman, 2013)
  - ie, given the object properties and capabilities of the actor (user), what does the object allow for?
    - An actor can sit on a small wooden chair
      - Object property: space for user to sit, provides support
      - Actor capability: small enough to fit on chair without breaking
  - Users have capabilities, Objects have properties, relationships between them are affordances

### Signifiers

- **==Signifier==** - communicate where the **action** should take place 

  - (Norman, 2013)
  - refers to any mark or sound, or any perceivable indicator, that communicates appropriate behaviour to a person
  - **affordances** determine *what* **actions** are possible, **signifiers** indicate *where* they take place

  Allow us to communicate to a user through design how something is used without explaining it to them directly

![image-20200929121812616](images/lecture/image-20200929121812616.png)

*clues in the interface to signify what can be done*

## Lecture 10 - Live Demo of React - 2020-10-01

See recording:

## Lecture 11 - Live Demo of React

See recording: 

## Lecture 12 - Usability Testing - 2020-10-06

### Usability Testing

- ==**Usability Testing**== = technique to evaluate the usability of an interface by testing it on users

  - users actually ***use*** the interface during a **usability test**
    - users are typically asked to carry out tasks that the interface performs
    - Testers will observe the user using the interface, while listening and taking notes
  - **usability testing** is a form of *research*
    - another way to learn user's needs, behaviours, motivations
    - Actually about learning as much, or even more than, get a "pass" or "fail"

  

![image-20201006115431682](images/lecture/image-20201006115431682.png)

![image-20201006115445915](images/lecture/image-20201006115445915.png)

![image-20201006115458648](images/lecture/image-20201006115458648.png)

- importantly, **usability testing** does not correspond 1-1 with *Verification* or *Testing* in Waterfall (or even Agile)
  - in these models, testing is usually referring to unit testing, integration testing, acceptance testing
  - answers: does the software we've built satisfy requirements ***not the users***

#### Why Conduct Usability Testing

- Identify **usability issues**
  - Identifies required changes
- Learn if participants can successfully complete tasks and how well they can complete them
  - How long will it take them to complete tasks?
  - We can record metrics for performance 
- Find out how participants think and feel about the interface
  - How satisfied are participants with it?

#### How to Conduct Usability Tests?

- Formal Usability testing labs are **not required**
- Fundamentally: if you're asking a user to perform tasks, your application accomplishes while observing their behaviour, you're usability testing

- **Test Plan**:
  - Good usbaility tests document all details for how testing will occur
  - Not one-size-fits-all; tune to the interface, users, and goals
- Participants need to be **recruited**
  - How many? From where? What demographics?

#### Sketch, Wireframe, Mockup Usability Tests

- User is asked to interact with sketches and other non-interactive early-stage prototypes
- Tester flips pieces of paper or manually changes the screen in response to user actions
- Fascinatingly, users have been shown to provide more open feedback to low-fidelity prototypes!
  - Why? Low fidelity implies low effort thus far, compared to telling the test the full-blown application is no good

#### Discount Usability Testing

- More focus on qualitative observations, earlier stage prototypes, use of the think-aloud method, and testing with about 5 participants
- Qualitative observations require less time to prepare
  - Compared to more quantitative methods like surveys and collecting other day
- **Think-aloud techniques** involve asking participants what they are thinking as they use the interface

![image-20201006120255502](images/lecture/image-20201006120255502.png)

##### Testing with Only 5 Users

- Research has shown its actually enough to find a majority of usability issues
  - A lot of time spent with additional users is simply identifying the same issues over and over
- Critics do exist and are correct to point out that this will leave usability issues unidentified
- However, low number of test participants repeated testing:
  - 25 participants worth of testing to spend: is it better to use 25 on one iteration, or 5 for several iterations of testing?

#### Competitive Usability Testing 

- Participants test competing interfaces
  - One version v. another version 
  - Interface v older version
  - Interface v a competitor
-  **within-subject test designs**  =  same participants test both interfaces
  - more typical; allows participants to make direct comparisons
- **Between subject designs** = different participants test the interfaces

##### A/B Testing

- Two groups of users are randomly assigned to either a control group (no change) or the treatment group (with the change) and a dependent measure is tested to see if there is a difference between groups
  - The change in A/B testing is some difference in the design of the interface
  - We can use stats on the results "with a 99% confidence, we can say that...."
- Widely use in industry

#### Remote Usability Testing

- Usability testing done online instead of in person
- **Synchronously:**
  - Tester observing users *as* they perform the tasks
  - Sometimes called **moderated** or **monitored**
- **Asynchronously:**
  - users performing tasks and testers observing results later
    - Tests may be able to watch a recording
    - Sometimes called **unmonitored** or **unmoderated**
- Can actually be more cost effective
- Can open up test populations
- Can be more realistic: not in a lab environment

#### Other Types of Usability Tests

- **Field Testing** = focused on testing the interface in realistic or natural environments
  - Testing an interface for a hospital in the hospital
- **Universal Usability Testing** = focused on testing  with diverse users, hardware, software, networks
- **Can-you-break-this Testing** = when users are challenged to find fatal flaws in the interface
  - Used frequently with video games
- **Lab Testing** = done in a **usability lab** with equiptment such as two-way mirrors and recording devices
  - High-fidelity observations, potentially less realism
  - Sometimes lab resemble a living room or office to add realism to the setting
- **Guerilla Testing** = done in a public place with randomly chosen participants
  - coffee shop

### Usability Testing Observations Techniques, Tools, and Metrics

#### Note-Taking

- As the users perform tasks with the interface, we can take notes to analyze and summarize later
- Notes can be more formal with categories, checklists, and/or questions
- Free form written observations of the participants experience
  - "Appeared confused when trying to find the pay button"
  - "Smiled at the pop sound effect after clicking delete"

#### Usability metrics

- **Metrics** = what is measured quantitatively by **usability tests**
  - Time to perform a tasks (performance)
  - Ability to complete tasks successfully
  - Error rates associated with a task
  - Subjective satisfaction of the user
- **Measures** = *how* we measure metrics
  - Metrics can be measured in different ways
- **Logging** = application programmatically recording metrics 
  - works well with *performance* and *error rates*
  - We can add code to our interface to record user actions and track time, etc
  - High accuracy, great data

#### Task Performance

- Tasks we ask the users to perform could be any tasks or subtasks in our task hierarchy we wish to test
- But typically the tasks that are tested are the most **high level** tasks (goals), that take more time to perform and are made up of subtasks themselves
- If users are failing to perform tasks, we need to account for this in our data presentation and analysis
  - look at performance individually instead, also present a table of percentage failed to perform tasks

#### Surveys

- Surveys can be done before and or after the user uses the interface to collect data as part of a usability test
  - Inexpensive in time and money, modern tools
  - Survey data can be anonymous
- Surveys done before testing can be used to collect demographic data and user characteristics
- After testing can be used to collect data about how users think about feel about the UI
- We can use statistical analysis on survey data
- We can use survey data to provide a metric for subjective satisfaction, trust ability and other user feelings

##### Likert Scale 

- ==**Likert Scale**== = Scale that maps numerical values to agreement level
  - Strongly disagree - 0 
  - Strongly agree - 4
  - ***agreement level***
  - ![image-20201009115306604](images/lecture/image-20201009115306604.png)

##### Semantic Differential (SEQ)

- ==**Semantic Differential**== = Quantify any discrete amount of responses between two semantically different ideas
  - ![image-20201009115254966](images/lecture/image-20201009115254966.png)

##### System Usability Scale (SUS)

- **==System Usability Scale==** = Likert but with 10 options
  - Results can compute score from 0-100
  - https://www.usability.gov/how-to-and-tools/methods/system-usability-scale.html

#### Interviews

- Conduct ***before*** and ***after*** Usability Testing
  - *almost always* done at the end of **usability testing**
  - More expensive in time than **surverys**
  - Tend to receive *less **honest** feedback* than **surveys**
  - Can ask more *probing* / *targeted* questions
- **Interview** questions can be scripted in advance
  - But interviews can also be done more free form
  - Blend of both is usually best
- Can be good to have **two interviewers**
  - Take questions
  - Take notes

##### Conducting Interviews

- Decide on **goals** in advance
- Explain the **purpose** to the **user**
  - Helps them understand *how* they can be helpful
- Make the **user** feel *comfortable*
  - They will likely share *more openly* if they're comfortable
  - Give visual / audibly feedback cues
    - Nod and actively listen
  - Begin with easy questions, less judgemental
  - Be authentic
- Prepare questions in advance
  - Create a list
  - Get feedback on the list from peers
  - Ensure that question ***aren't leading questions***
  - Write questions that **promote dialogue**
  - Anticipate responses and create **follow-up questions**

#### Think-Alouds

- ==**Concurrent Think Aloud (CTA)**== = **Tester** asks **participant** to think aloud ***while using the interface***
  - Understand participant's **stream of thoughts**
  - Can't extract accurate usability metrics like performance time
- **==Retrospective Think Aloud (RTA)==** = Is when tester asks participant to **retrace** their thought process *after* having used the interface
  - Less reliable for understanding participant thoughts
  - Doesn't interfere with usability metrics
  - Increases total test time
  - Can show participants video of themselves using the interface to help with **RTA**

#### Probing

- **==Concurrent Probing==** = Tester asks the participant probing questions about their thoughts *as they use the interface*
  - Participant becomes confused / excited, tester can ask why in the middle of the test
  - Issue is that this ***interferes with the testing itself***
- **==Retrospective Probing==** = Tester asks probing questions about their thoughts *after using the interface*
  - **Doesn't** interfere with testing, but ***reliability issues***
  - Can be done as part of a post-test interview

#### Eye-Tracking

- Software can be used to determine where users look within an interface
- Heat map can be generated from this data

#### First Click Testing

- Where we ask the user where they would first click for starting a task

#### 5 Second Testing

- Give a user a question, and then show them the app for 5 seconds to answer it
- Can user quickly identify something?

## Lecture 13 | Usability Test Plans, Recruitment, and Reporting

### Usability Test Plans

- ==**Usability Test Plan**== = Documentation that covers all aspects of how tests will occur
  - Includes:
    - Scope
    - Purpose
    - Schedule/Location
    - Format
    - Participants
    - Equipment
    - Roles
    - Sessions
    - Tasks / Scenarios
    - Observations 
    - Metrics
    - Instruments (**Surveys**, **Interviews**)
    - Participant Instructions (in the case of **asynchronous testing**)

#### Scope

- *What* application is being tested?
- *What* **features** of the **application** are being tested?
- *When* is the **testing** occurring? 
- *What* **version** of the product or interface?
  - Version 10.5?
  - Sketches? Interactive prototype?

#### Purpose

- What are you concerned with? What questions do you want to answer through **usability test**
- What are your goals in conducting the testing?
  - Goals can very general or very specific

- **General Goals**:
  - Do users easily learn how to use the application? 
  - Do users commit many errors when using the app?
- **Specific Goals**:
  - Can users use the shopping cart successfully?
  - How long will it take users to find the advanced settings?

#### Goals

- You only have *so much time* with each user
  - How many goals can you realistically achieve?
  - **don't have too many goals**
- Goals should *drive* decisions about the design of the rest of the test plan
- Goals should be carefully thought out, tied to goals for your application and concerns about its design

#### Schedule and Location

- When and where will your tests take place?
- Will it be done remotely or in-person?
- Specific about how many sessions you will hold

#### Format

- Will it be **moderated** or **un-moderated**

#### Participants

- **Who** are the participants in your **usability test**?
  - Do you know who they are?
  - Do you know any demographic information?
- How were the participants recruited, or how are they going to be recruited?
- How well do the recruited participants match your target demographics?

#### Equipment

- What equipment will be used during the test?
  - Hardware
  - Software?
  - Recording devices?
- What will be recording with equipment?

#### Roles

- Who will conduct the usability tests, and what role will they play?
- A usability specialist might conduct the test, and a note-taker might take primary responsibility for taking notes

#### Sessions

- What is the order of activities for a test session with a participant?
  - Ex
    1. Pre-study survey
    2. Ask participant to perform task x
    3. ....
    4. Post Study Survey
    5. Post study interview
- How long will a session take?
  - 60-90 mins is typical in large application
  - Can be done in 10-20 minutes for smaller apps or more focused scopes

#### Tasks and Scenarios

- What **Tasks** wil you ask users to carry out?
  - Tasks can come from our task hierarchy, at different depths
- Tasks are generally better written in the form of a **scenarios** with specifc information
  - instead of "use the app to buy a book" say "use the app to find and buy the book 1984"
    - remove unnecessary freedoms in the problem space
- **Exploratory Tasks** = open-minded and may not have a specific correct answer
  - Useful for learning how people discover information, not for quantitative results
  - "You are interested in booking a vacation for your family. See if the site offers anything that you might suit your needs"
- **Specific Tasks** = more focused and have a definitive end point
  - Find the saturday opening hours for the Sunnyvale Public Library 

#### Observations

- How will you be making observations?
- Metrics and instruments:
  - Will you be recording metrics?
  - Will you be conducting any interviews?
  - Will you be conducting any surverys?

#### Metrics

- What quantitative metrics will you measure?
  - How will you measure them?
- Will you produce metrics for users feelings and thoughts that don't have straightforward quantification?
  - How will you measure these?

#### Surveys

- Will participants complete a survey?
  - What survey will participants complete?
  - What questions are on the surveys?
  - When will participants complete the surveys?

#### Interviews

- Will interviews be conducted?
  - Is there a script of preset questions?
  - Are there follow up questions?
  - Will it be unscripted, or scripted?

#### Instructions

- If the test in asynchronous, then the steps required are clearly laid out
  - How to access the application
  - How to access surveys
  - What tasks are requested to be completed
- Tester can be expected to carry out instructions 

### Recruiting Participants

- The most important thing is to ensure **participants** are *similar* to your **target user**
- ***avoid conflicts of interest***
- Screen:
  - demographics
  - Personality
  - Work experience
  - Background knowledge
- Nice applications, screening becomes more important
- Compensating participants can help ensure they take the test more seriously

### Usability Test Report

- Results might be reported verbally in a meeting, with slides or in a formal written report
- Usability test reports should include:
  - Background summary
  - Methodology
  - Test results
  - Analysis of Results
  - Recommendations
- We can create sections with these headings but like usability test plans, we don't have to use these exactly
  - We may have additional sections

#### Background Summary

- Summary and methodology are both made up of essentially the same information as the test plan
  - But the audience is potentially different... testers vs. managers for example
  - Information is generally best summarised 
  - Usability test report should be more universally accessible
- Made up of these portions of the test plan, summarised:
  - Scope
  - Purpose
  - Schedule / location

#### Methodology

- Made up of these portions, summarised:
  - Format
  - Participants
  - Equipment
  - Roles
  - Sessions
  - Tasks
  - Observations
  - Metrics
  - Instruments
  - Participants instructions

#### Results

- Present the data that was collected:
  - Survey Data
  - Metrics recorded by the application
  - interview data
  - Note-taking observations
- Utilise tables, graphs, screen captures, wherever illustrative or helpful to present the data and results
  - Test of performance times
  - where in the app an issue is discussed

#### Analysis

- Analyse the results should answer: what was learned? What is evident or likely from the results?

  - We can call what was learned **findings**

- How does the data support the **findings**

- What usability issues were identified?

  - Can organise them by priority, for example;

    - Low- most cosmetic issues
    - Medium - can be frustrating for users
    - High - must be fixed as soon as possible
    - Critical - app cannot be released without fixing them

  - Frequency of occurrence of the issue may be reported, and may be a factor in the issue's severity level

    ![image-20201009130909974](images/lecture/image-20201009130909974.png)

- Findings can be reported per-scenario, aggregate across scenarios, or both

- Analysis should not be exclusively negative 

- **findings should be as specific as possible**

#### Recommendations

- Changes recommended as a result of the findings of the usability test
- Recommendations should be associated with findings
- What is the reasoning for the recommendation?
  - This is not the same as the findings
  - The reasoning is why you believe the recommendation will address the finding
  - eg. "we should move the search bar to the top right, because that's where users were moving their focus to look for it"

##  Lecture 14 | Websockets and Bootstrap with React - 2020-10-09

### Websockets with React

- There are several Websocket libraries we can use with React

- We can use the same socket io library we discussed in tutorial, as an npm package exists for it

  - `npm install socket.io`

- If using `create-react-app`, import the package, and create the socket:

  ```react
  import io from 'socket.io-client';
  const socket = io('http://localhost:3001');
  ```

- Because the React app itself already runs on port `3000`, we'll connect to a server with websockets using `3001`

### Incoming Messages

- From there, we can setup the handling of **incoming messages**

```react
constructor(props){
    super(props);
    
    socket.on('connect', function(){
        socket.on('chat message',
                 function(data){...
                               })
    })
}
```

- We can **send/emit messages** wherever we like, for example, in **event handlers**:

  ```react
  submit()
  {
      socket.emit('chat message', this.state.input);
      this.setState({input: ""})
  }
  ```

### Bootstrap With React

- A version of **Bootstrap** purpose-built for **React** has been created
- It uses **Bootstrap React Components** rather than CSS classes, and it drops dependencies
- Install with bootstrap package:
  - `npm install react-bootstrap boostrap`
- Import bootstrap in App.js and import the ***specific components you need***
  - `import 'boostrap/dist/css/bootstrap.min.css';`
  - `import {Button, FormControl, ListGroup} from 'react-bootstrap'`
- We can then use <Button /> and the other components in our JSX expressions... that it!

## Lecture 15 | Example Usability Test

Missed for 4AA4 Midterm

## Usability Evaluation

- **Usability testing** is one common way of evaluating a user interface
  - Potential problems:
    - What if we don't have access to users?
    - What if we don't have the time or resources?
    - Does a short 15-90 minute test capture how users will experience the UI over longer periods of time?
- **Usability Inspections** = evaluations of user interfaces through *inspection*, generally performed by **non-users** such as **usability experts**
  - **Types:**
    - Heuristic evaluation
    - Cognitive walkthrough
    - Pluralistic walkthrough
  - Jacob Nielson's <u>*Usability Inspection Methods"*</u> formalized and popularized inspection techniques in the 1990s

### Heuristic Evaluation

- **Heuristic Evaluation** = when an **evaluator**, ideally a **usability expert**, evaluates an interface with respect to a set of guidelines (*principles, theories, etc*)
  - Developed by usability consultants Rolf Molich and Jakob Nielsen
  - Primary goal is to identify **usability issues** and UI problems
  - Can be done on a per-task basis, but is more often interface-wide
- One set of guidelines / principles may be used, or mutiple may be used
  - Guidelines should be *relevant to the interface*
  - Use *niche* guidelines for your specific type of UI
    - Mobile learning applications heurisitcs
    - Touch-screen based mobile device heuristics
    - Heuristics for video games, 
    - etc...
- **Evaluator** = ideally an expert that is familiar with the familiarity guidelines and principles
  - *knows how to interpret them properly*
  - Offers informative feedback 
    - which is a bit subjective, we need to make it quantifiable 

- Example Sheet:

  ![](images/lecture/image-20201022114149547.png)

#### Pros

- Fast and inexpensive
- Can be done early in dev process and *without users*
- Can be done with internal resources

#### Cons

- Results are influenced by the knowledge and biases of the reviewer
- Only one reviewer means they will miss things!

### Cognitive Walkthrough

- **Cognitive Walkthrough** = **usability inspection** method where the evaluator step through tasks the users will perform

  - At *each step*, evaluator simulate a user's though process
  - Goal: uncover **usability issues** *with respect to **learnability**
  - Performed in **optimal action sequence**
    - assumes optimal path & no fumbling around
    - Identify where user would get confused while following optimal sequence

- Example Walkthrough:

  ![image-20201022120534006](images/lecture/image-20201022120534006.png)

#### 4 Common Questions:

1. Will the user try to achieve the effect that the subtask has?

2. Will the **user** notice that the correct action is available?
   - Signifier? Affordances? Gulf of Execution?*

3. Will the user understand that the wanted subtask can be achieved by the action?

4. Does the **user** get *appropriate* **feedback**

- The first three questions are related to *gulf of execution*, and the last is related to *gulf of evaluation*

#### Pros

- Similar to **heurisitc evaluation**
  - Cost
  - Time
  - Don't need users
  - Can be done internally

#### Cons

- Evaluators ***do*** fumble around confused with the interface *in practice*
- Evaluation is then influenced *by this confusion*, rather than judging the **optimal path** as its laid out

**==Note==: Professors Opinion:** it can be ***very*** time consuming in practice

- Professor spent 4 hours to evaluate 40% of a basic SaaS web application

### Pluralistic Walk-through

- **Pluralistic Walk-through** = A ***group*** stepping through tasks an interface supports and discussing **usability issues** *at each step*
  - Group: multidisciplinary approach (made of *developers, usability experts, and users*)
  - Walk-through is done with **hard-copy panels**
    - either **prototype** or **screen captures**
    - uses **optimal action sequence**
- **Facilitator** leads group through walk-through step-by-step
  - each step is a user action
  - participants play the role of the user individually each step
  - Participants write on the panel the next action they would take to conduct the task
  - Hold a group discussion until asking the group to move on

#### Pros

- Developers gain appreciation for user frustrations
- Re-design ideas incorporate thoughts *of all stakeholders*
- Can produce good usability data early in development

#### Cons

- Very time consuming in practice
  - More so than cognitive walk-throughs
  - Slowest group member determines pace
- Difficult to schedule 
- Nature of the walk-through (optimal path) doesn't allow for learning about browsing and exploring behaviours

### Usability Inspections

- Like usability tests, results from usability inspections can be reported in different formats
  - Formal report, presentations
  - Informal presentations, reports, summaries, etc
- Heuristic evaluations:
  - results might get reported as *per-heuristic* **checklist** with an associated result
- Walk-throughs:
  - results might get reported as a *per-task* checklist with an associated result

### Evaluation During Active Use

- Usability testing and inspection methods 
  - Both still very important and relevant

## Lecture 16 | Geolocation and Geocoding - 2020-10-27

### Geolocation

- **HTML5 Geolocation API** allows us to determine a user's location and use it in our application
  - It's a privacy concern, so all applications which use geolocation will request the user's permissioin before the location information is available
- **Geolocation** information can be determined by the browser / device in a few ways
  - GPS (very accurate, within meters)
  - IP address
  - Wifi signals
- When using the **Geolocation API** all this work is done for us:
  - But we do sometimes care about *how* the user was geolocated
    - GPS more accurate than Wifi
  - Returns lat & long

![image-20201027115423953](images/lecture/image-20201027115423953.png)

```javascript
navigator.geolocation.getCurrentPosition(
	showPositionCallbackFunc
);
```

- getCurrentPosition

### Geocoding 

- **Geocoding** - allows us to take mailing addresses and convert them into latitude and longitude positions
  - Expensive: requires tables of data and other methods

## Lecture 17 - User Interface Types - 2020-10-29

### User Interface Types

- So far we've covered graphical user interfaces operated by keyboard and mouse
  - Point & click
  - Mobile applications are an extension of point & click
- HCI is broader!

### Command Line Interfaces

- **Command Line Interfaces = ** process commands represented as strings
  - **command-line interpreter** = program that implements a commandline interface, i.e. ***the shell***
- Still used when ***user is an expert***
  - Software development
  - Provides continuation of context when SSHing to other systems
- Short term learnability cost is worth it for longer term performance

#### CLI Advantages

- Superior **performance** if the user has memorized the commands they need to perform
- **Scripting** of commands is more straightforward than in GUIs
- Less compute and resources required than GUIs

#### CLI Disadvantages

- ***slower*** performance if the user has not memorized commands
- If commands are typed even slightly inaccurately, they will not function

### Graphical User Interfaces

- **GUI** = allow user to interact with visual graphical elements such as windows, icons, and buttons
  - Leverage real-world analogies / metaphors

#### GUI Advantages

- Learnability - key for beginners
- Visually more appealing
- Allows for input from mice and other devices

#### GUI Disadvantages

- Requires more resources
- Performance can be slower for experts

### Direct Manipulation

- **Direct Manipulations** = an interaction style defined by the follow 3 principles

  1. Continuouse representations of objects and actions of interest with meaningful visual metaphors
  2. Physical actions or presses of labeled interface objects (buttons) instead of complex syntax
  3. Rapid, incremental, reversible actions whose effects on objects of interest are visible immediately

  ***over lap with 4 Norman Principles***

- Metaphor feature of direct manipulation is key to what makes GUI's **intuitive**

- Popularized by Ben Schneiderman in early 1980s

  - response to the **desktop metaphor**

- Goes beyond GUIs

#### Advantages

- Rapid learnability
- Errors are avoided, error messages rarely needed
- Users experiences less anxiety
- Users feel in control

### Disadvantages

- Accessibility may suffer
  - ex. visually impaired users
- If we need to represent objects to act on them, won't that limit the number of objects we can act on at one time?
- Performance: slower, repetitive actions generally not well supported
- Without a good metaphor, rapid learnability may not occur *in practice*

#### Motion Tracking Interfaces

- **Motion Tracking Interfaces** = work by tracking the movement of subjects / objects
  - ex. Xbox Kinect, Nintento Wii
  - Can use Computer Vision or Accelerometer tracking

#### Advantages

- May be even more intuitive than metaphors
  - replicates "Natural" movement
- Movement can be enjoyable 
  - *subjective satisfaction*

#### Disadvantages

- Accessibility may be an issue
- Movement is restricted
- Is accuracy high enough to simulate real situations

### Gesture Interfaces

- Motion tracking interfaces may incorporate gesture recognition
- **Gestures** = visible body actions that communicate messages **non**-**vocally**
- **Gesture Interfaces** = interfaces based on gesture recognition
- A mouse can actually be a form of gesture interface!
  - Tap, doubletap, hold tap, and drag
- Specific gestures can be performed with a mouse to communicate a message
- Smartphone and tablet **multi-touch screens** are capable of recognising multiple screen touches are gestures

#### Advantages

- Intuitive
- Subjective satisfactions
- Help remove need for buttons 

#### Disadvantages

- Fatigue
- Accessibility  - case dependent
- Learnability
- Accuracy

### Touch Interfaces

- **Touch Interfaces** = work based on the sense of touch
  - Touch interfaces generally work by a user touching a touch-sensitive screen
- Touch screens *do not* need to recognize multiple touch

#### Accessibilty

- ex. Braille display
- Accessibility has been cited as a concern with these interfaces
  - when purpose-built for accessiblity, touch interfaces can actually **support** accessibility

## Lecture 18 | Voice User Interfaces - 2020-10-30

### Voice User Interfaces

- **Voice User Interfaces (VUIs)** = Interface that use ***speech*** for interaction and communication

- **Speech Recognition** = process used to translate speech into text

  - Long & interesting history

    - Original hypothesis was that *understanding* would be critical

  - Modern speech recognition done with Markov models, & machine learning (NLP)

  - *modern speech recognition reached parity with human translators in 2017*

    https://www.microsoft.com/en-us/research/blog/microsoft-researchers-achieve-new-conversational-speech-recognition-milestone/

#### Advantages

- Hands-free *and* eye-free operation, at a distance
  - VUIs may be operate *while also doing something else*
  - VUIs can listen for commands across a room
  - form of **ambient computing**
- Performance improvements in some cases
  - Stanford study shows dictation is **3x faster** than typing
- Learnability can be excellent
  - Speech is intuitive 

#### Disadvantages

- Privacy
  - VUI input can be heard by anyone 
- Noise
  - If everyone in a space used a VUI at once, it would be quite loud
- Discomfort
  - Some people are uncomfortable using VUIs, especially in public (privacy aside, people do not want to look awkward / draw undue attention to themselves)
- Error rates
  - Errors in speech recognition can impede usefulness
- Discoverability
  - Difficult for users to discover the full range of commands and capabilities
  - Potential for large ***Gulf of Execution***

#### Designing Voice User Interfaces

- In contrast to GUIs, best practices in terms of design **guidelines**, **principles**, and **theories** are not as well established
  - Newer areas of HCI research
  - https://dlnext.acm.org/doi/abs/10.1145/3236112.3236149
- General guidelines, principles and theories may be applied to VUIs, but will require extra interpretation

- VUI overlaps with the concept of a conversational interface, but are not the same

#### Challenges

- Discoverability is likely the biggest challenge

  - **Lyndon Cerejo**: "Onboard the user and help them get started"
    - https://www.smashingmagazine.com/2017/05/designing-voice-experiences/
    - Thesis on VUI onboarding: https://www.diva-portal.org/smash/get/diva2:1222939/FULLTEXT01.pdf

- Siri example:

  - ![image-20201102135032509](images/lecture/image-20201102135032509.png)
  - Explicitly show / inform the user the most commonly used features

  

#### Onboarding

- One simple and effective method: *provide example utterances for different functionalities*
  - teaches the user how the app works
  - Users will also get a sense of how to command the interface
    - eg. *verb subject* formats : "Call Alan", "Launch Netflex" "Text Susan"
- **Utterance** = spoken statements

#### Discovery

- Siri will display the above screenshot after some specific **utterances**:
  - "Help", "What can you do Siri?"
- We can have a VUI *respond* to a request for help, or similar with guidance
- **Help and other universals**: design guideline by *Cathy Pearl*
  - Include a set of **universals** at every state
    - *repeat, main menu, help, operator, goodbye*

#### Error Prevention

- We can *prevent errors* in a VUI by expecting and acommodating **utterance *variations*** 
  - recall **8 Golden Rules** statements regarding error prevention
  - in other words, if we want to let user launch applications, allow for it to accept variations of the command with the same underlying meaning
    - e.g. "launch Chrome", "run Chrome", "execute Chrome", "start Chrome", etc. 

- NLP-based VUI APIs allow us to *train* the app to recognize **intents** based on a set of sample data for each intent
  - Each intent will have a **response** action
  - An intent is essentially a command, and a response is the action that occurs after the **intent** is recognised
- Several VUI Guidelines recommend similar **prevent error** rules, just as the 8 Golden Rules:
  - Google's Conversational Design Guidance
    - "Prevent errors by expecting variations"
  - Google's Conversation Design Best Practices
    - "Prevent errors by providing help in the moment"
    - "Make the success path more robust to 'disguise' errors"

#### Error Handling and Messages

- **Offer informative feedback**
  - 8 Golden Rules
  - Including for utterances for which no command or response can be provided 
- Let user know the **utterance** was heard by the VUI
  - Otherwise they don't even know the error and may repeat
- Can ask the user to repeat what was said
  - Perhaps the speech wasn't recognized correctly,
  - Perhaps the user will re-phrase the utterance 
- In a conversational UI, ***don't treat the "error" like an error*** given the nature of the interaction
  - Breaks the concept of a conversational VUI
  - Don't tell the user they've committed an error, don't blame the user for the error
- If the VUI is used as a part of customer service, after a threshold # of errors, redirect to a human
  - VUIs might be able to handle 98% of your clients
  - Still need to accommodate the other 2%

### Designing Voice UI Principles

- **Conversation Design**
  - Humans rarely have conversations that only last one turn
  - Design beyond one sentence; *preempt what users might want to do next*
- **Set User Expectations**
  - Don't ask a question if you won't be able to understand the answer
- **Confirmations**
  - Make sure that users *feel* understood, and let them know when they aren't
- **Conversational Markers**
  - Let the user know *where* they're at in the conversation
- **Error Handling**
  - Design for when thing go wrong, because *something will always go wrong*
- **Don't Blame the User**
- **Novice and Expert Users**
  - Adapt to the experience and expertise of the users
- **Keep Track of Context**
  - People don't repeat terms in conversation, they use pronouns like "she" after the subject has been established
  - Make sure your system understands the *context of user input*
- **Help and Other Universals**
  - Include a set of universals at every state
  - Commands that work in *any* scenario
- **Latency**
  - Use audible or visual cues to communicate unavoidable system delays to the user
- **Disambiguation**
  - If a user gives ambiguous information, use contextual clues to make a smart guess or ask for clarity
- **Accessibility**
  - Design experiences for everyone, *no matter their abilities*
  - Make interactions: *time efficient*, *provide context*, *prioritise personaliztion over personality*

#### Interaction Design Foundation's Guidelines for Designing VUIs

1. Provide users with information about *what* they can do
2. Help users understand *where* they are in the system
3. Express intentions *in examples*
4. Limit the amount of information
5. Use visual feedback

#### Designing Voice Experiences: Guiding Principles

1. Onboard the user and help them get started
2. Keep conversational exchanges brief to reduce cognitive load
3. Examples work better than instructions
4. Delight *without* interfering with the task
5. Use explicit confirmations for important actions, and implicit for less risky
6. Design *for failure*
7. Respect the user's privacy and security

#### Basic Guidelines for Successful Voice Design

- **Reincorporation is key**
  - When the customer has given you **data** in their utterance, reincorporate it to confirm recognition
- **GUI parity is *not* the goal**
  - Speech interfaces are good at certain things: 
    - search, frequently repeated actions, sets of unique values
  - Speech interfaces are bad at:
    - Screen-by-screen navigation and data-heavy interactions
- **Brevity is the soul of voice UI**
  - Every word of your response will increase the time your customer must spend listening
  - Be particularly strong-handed with edits on frequent responses
- **Use questions to guide multi-turn interactions**
  - Don't just open up the mic and hope for the best
  - If you don't have enough information to act, give the customer a starting point in the form of a question to set them up for success
- **Choose personality moments wisely**
  - Only inset personality if you believe your customer has time to spare
  - Avoid in repetitive task
  - Best use in response to open-ended questions, i.e, "How are you?"
- **Test drive your sample dialogs in audio form**
  - Your system may mispronounce common words or generate odd intonations
  - Your utterances may be awkward when spoken
  - If possible, generate audio comps with both side of the conversation recorded
- **Consider earcons, but use sparingly**
  - **earcon** = audio icons; beeps and other audio indicators (think RD2D)
  - Can lead to more streamlined interactions, especially for repeated tasks
  - Additional considerations: 
    - Speaker quality
    - cohesion
    - acoustics

### VUI Guidelines & Principles

- Comprehensive list of guidelines and principles:
  - https://www.voiceprinciples.com/
- Active area of research and development

### Conversational VUIs

- Beyond implementation via NLP, there are other more general design issues
  - Mostly related to branding as much as conducting interaction
- Do you give the VUI a name and identity?
  - Does it have a personality
    - ***why*** does it have this personality?
  - Does it have a sense of humour?
    - Is it compatible with the brand? Is it appropriate? Is timing ok?
  - Does it have a gender?
    - Users apply gender stereotypes to VUIs
    - ***Designers*** also apply gender stereotypes when creating VUIs