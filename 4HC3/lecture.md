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

- **==Retention==** - When users *return* to the design after a period of time, how easily can they **re-stalish proficiency**
  - Can call this goal ***memorability***

- **==Performance==** - Once users have learned the design, **how quickly** can they perform tasks?
- **==Error Rates==** - **How many** errors do users make? **How severe** are these errors? **How easily** can they *recover* from the errorrs?
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

- Wireframes accurately represent interface page layout and organization of content
  - But lack colour, typography, images and graphics
  - i.e. ***blueprints***
- Increased *precision* over sketeches and use of software makes wireframes less accessible than sketches
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

1. **Define task being analyzed:** as well as the purpose of the **task analysis**

2. **Conduct data collection**: Pay particular attention to areas such as *technology*, *machine* and *team member* iteraction, decision making, and *task constraints* to better understand the **process*

3. **Determine the overall goal of the task**: This should be in place at the top of the **task hierarchy**

4. **Determine Task Sub-Goals**: Decompose the overall goal into *corresponding* **sub-goals**. Together, these subgoals should comprise the tasks necessary to accomplsih the overall goal

5. **Perform Sub-Goal decomposition**: Subgoals should be further broken down into *additional* **subgoals** and **operations**.  Continue this process until you reach an appropriate operation, which specifies the action that actually needs to be done to accomplish the goal. There should always be an operation at the bottom level of *any* branch in a **HTA**

6. **Develop Plan Analysis**: After describing all the subgoals and operations, add the plans. Plans explain how a goal should be accomplsihed. These may be in the format "do A, do B, do C"

   

### Divergent & Convergent Thinking

- **==Divergent Thinking==** = Thought process or method used to *generate* creative ideas by exploring many possible solutions

  - Quantity over quality
  - Novel ideas
  - Creating choices

  Similar to **brain storming**

  - "Right-Brain"
    - Creative, Artistic, Solution generating

- **==Convergent Thinking==** = Though process or method to make a *deliberate* and *conscious* choice. We purposefully apply criteria as we screen, select, evaluate, and refine options

  - Analyze and filter
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
  - Classic undirected brainstorming, just write down whatever you think
- **Journal**
  - Keep a journal of ideas to write them as they occur
- **Freewriting**
  - Write freely without structure or stopping 

- **Mindset**
  - Research shows we think divergently best when we are *happy, feel less pressue, less anxiety, well-rested*

- **Oxymoron**
  - Explore what happens when you remove what's most essential about a product or concept to generate new ideas
- **Arbitrary Contraints**
  - Set constraints and create designs within them
  - Forces more creative thinking
- **Brainwriting**
  - Have everyone write down their own brainstorm, then share together afterwards
  - Helps negate groupthink or going down a suboptimal path
- **Lateral Thinking** - solving illogically
  - Random entry idea generating tool
  - Provocation
    - Say something provocative to motivate ideas
  - Disproving
    - Take a popular idea and try to disprove it
- **Scamper**
  - **Substitute**: come up with another topic that is equivalent to present the topics
  - **Combine**: adds information to the original topic
  - **Adjust**: identifies ways to contruct the topic in a more flexible and adjusted material
  - **Modify**: Magnify,minify, creatively changes the topic or makes a feature/idea bigger or smaller
  - **Put**: to other uses uses identifies the possible scenaries and situations where this topic can be used/implemented
  - **Eliminate**: removes ideas or elements from the topic that are not valuebale
  - **Reverse**: rearrange, evolves a new concept from the orignal concept

#### Inspiration

- Search for solutions similar to the problem you are solving
- Note and categorize the different design features that the solutions are using
- Attempt to combine these design features in new ways relevant to your problem