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

  

