# My Theory Assignment


## Q.1 How does Object-Oriented Programming differ from Procedural Oriented Programming?

| OOP e.g Python, JavaScript, Ruby, C++, C#                               | POP e.g , VB, FORTRAN, Pascal                                       |
|-------------------------------------------------------------------------|---------------------------------------------------------------------|
| Is a programming paradigm that divides programs into objects            | Is a programming paradigm that is based on functions                |
| It takes a bottom up approach                                           | It takes a top-down approach                                        |
| Is object oriented                                                      | Is structural/ procedural oriented                                  |
| Inheritances is supported in three modes: public, private and protected | Inheritance is not supported                                        |
| Adding in new data and functions is quite easy                          | Expanding data and function is not easy                             |
| The data in each object is controlled on its own                        | All the functions has different data, so there's no control over it |
| Access control is done with access modifiers                            | No access modifiers supported                                       |
| Data can be hidden using encapsulation                                  | No data hiding as data is accessible globally                       |
| The existing code can be reused                                         | No code re-usability                                                |
| This is mainly used for solving big problems                            | This is not suitable for solving big problems                       |
| There is a concept of virtual function                                  | No virtual function                                                 |


## Q.2 What's polymorphism in OOP? 
#### This is from 2 greek words 'poly' and 'morphism' meaning 'many' and 'join'. Simply meaning to represent one thing in many forms. 
A real life example:
* A person --> In the shopping mall, behaves like a customer
* A person --> In school, behaves like a student
* A person --> In the bus, behaves like a passenger
* A person --> At home, behaves like a son/daughter

#### There are two types of polymorphism: Static and Dynamic. 
Static Polymorphism(Compile time). This is also known as early binding or compile time because memory is allocated during the compiling time. 
There are two examples of static morphism: 
* function overloading
* operation overloading
  
Dynamic Polymorphism(runtime). This can also be known as late binding or runtime because memory is allocated during the runtime.
example:
* virtual functions


## Q.3 What's inheritance in OOP? 
It is a method that allows us to create a new class that shares the same attributes (child class) and method with the original function(parent class) and add some extra functionality to the new class. 
It also does not disturb the original class.
example: 
```commandline
class Animal:
    def __init__(self, name, species):
      self.name = name
      self.species = species
      
      def intro(self)
          print(f" I am self.name and my species is self.species)
    
class Dog(Animal):
    def __ini__(self, name, species)
       super().__init__(name, species)

```


## Q.4 If you had to make a program that could vote for the top three funniest people in the office, how  would you do that? How would you make it possible to vote on those people? 
First step is to make a function. I will create 3 empty arrays that will store the top 3, 
then create an if condition that will run only if the items of the array is less than three meaning there should be more than 3 items in the array as it has to find the top 3,
then I will make a for loop that looks for the highest number each time and this will run three times, everytime it finds a number it will knock out the lowest number until it goes through the whole array and therefore will return the top 3. 
```commandline
def vote(array):
    first = array[0]
    second = array[0]
    third = array[0]
    if len(array) >= 3:
        for i in range(len(array)):
            if array[i] > first:
                first = array[i]
        
        for i in range(len(array)):
            if array[i] > second and array[i] < first:
                second = array[i]

        for i in range(len(array)):
            if array[i] > third and array[i] < second:
                third = array[i]
        return[first, second, third]
    else:
        print("make sure your input is more than 3 number")


array = [11, 141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]  #output = [18, 141, 541]
print(vote(array))
```


## Q.5 What's the software development life cycle?
#### Also known as SDLC, is the standardised practice of delivering software applications, and it is done through 7 steps:
#### 1.Planning
The planning phase will establish project objectives and a high-level plan for the intended project i.e a project plan.

#### 2.Requirements
During this phase,the end-user business requirements are analysed. 
Project goals are converted into the defined system functions that the organization intends to develop and are broken down into tickets/ tasks
This requirement does not specify how the system will implement the requirement, but rather what the system must do in relation to the business.

#### 3.Design
During the design phase, we describe the system's desired features and operations. This phase includes business rules, pseudo-code, screen layouts, and any other documentation that is required.
The specialist recommends the clients and servers required on a cost and time basis and the system’s technical feasibility. 
The organization also creates user interaction interfaces, data models, and entity relationship diagrams (ERDs) in this phase.
The two important activities are:

* Designing the IT infrastructure
* Designing the system model

#### 4.Build
In contrast to the design phase, the build phase will involve the organisation to purchase and install the necessary software and hardware to support the IT infrastructure. 
Following that, the database and actual code can be created to finish the system according to the specifications.
The following are the primary activities involved in the development phase:

* Development of IT infrastructure
* Development of database and code
#### 5.Test
During the testing phase, all pieces of code are integrated and deployed in the testing environment. 
Testers then go through the Software Testing Life Cycle activities to ensure the system is free of errors, bugs, and defects and that its functionalities work as expected. 
The following are the two primary activities involved in the testing phase:

* Making test cases
* Test case execution
#### 6.Deploy
During the following phase, the system is deployed to a real-world (client) environment where actual users can begin operating the system. 

#### 7.Maintain
During the maintenance phase, any necessary enhancements, corrections, and changes are made to ensure that the system continues to function and remains up to date to meet business objectives.
To adapt to future needs, the system must be maintained and upgraded on a regular basis.

## Q.6 What's the difference between agile and waterfall?
#### The waterfall methodology came first, where tasks are executed in phases. Progress flows in one direction like a waterfall whereas the agile is a step ahead, the main differences are:

| Agile                                                                        | Waterfall                                                                              |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Divides the project development lifecycle into sprints                       | Divides the software development process into distinct phases                          |
| Follows an incremental approach                                              | Follows a linear sequential approach                                                   |
| It is a flexible methodology                                                 | It is a rigid structural approach                                                      |
| Agile can be considered as a collection of various small projects            | It will be done as one single project                                                  |
| It is easy to make changes because of its flexibility                        | It is difficult to make changes                                                        |
| The test plan is discussed after the completion of each sprint               | The test plan is done during the testing phase                                         |
| Project requirements are subject to change                                   | This method is suitable for projects with defined requirements as changes are not easy |
| A fixed project budget is not suitable here as there may be some flexibility | Since all the requirement is well defined, the project budget does not change much     |
| High communication and collaboration among the team members                  | Low communication and collaboration among team members                                 |

## Q.7 What is a reduced function used for?
A reduced function is used when we want to perform a mathematical technique called folding or reduce. It is useful when you need to reduce a list into a single value. the syntax is reduce(funct, list)
```commandline(example of a normal function to find the sum of all the items in a list called grades)
grades = [75, 65, 80, 95, 50]

total = 0

for grade in grades:
    total += grades
    
    
print(total) #output is 365
```
```commandline(example of a reduced function)
from functools import reduce


grades = [75, 65, 80, 95, 50]
def sum(a, b):
    return a + b


total = reduce(sum, grades)
print(total) #output 365
```

* from the above reduce function, it takes two arguments and adds them together from left to right and reduces the whole list into a single value, e.g:
* a(75) + b(65) = 140 then
* a(140) + b(80) = 220 until...
* a(315) + b(50) = 365
## Q.8 How does merge sort work
By using a technique called divide and conquer, a merge sort will divide a list into two, as it is recursive,
it will be called again and again until all the items in a list is standing single. Once this is achieved, sorting takes place then merging: the elements are compared in pairs, placed into order
and combined once again. The process is repeated by tackling one branch at a time rather than one layer (of sub-arrays) at a time. 

* It has a O(n log n) = quasilinear time along with _quicksort_ and _heapsort_
* When working with large data, mergesort has a space complexity of O(n) and is faster than insertion sort, selection sort and bubble sort but on the other hand, it used more space than these as we need to create sub-arrays to store the elements


## Q.9 Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it  can be used in a for loop. What is the use case? 
Firstly, an iterator is an object that enables you to loop through a sequence of data without having to store the sequence in memory whereas, a generator is a new form of syntax, from python 3 that does the same thing without having you store the data in the memory.

For example, when working with a large data set that requires a lot of memory, we would use a generator.
A generator function is written like regular functions, it utilizes the yield keyword and returns a lazy iterator which means contents are not stored in memory.

```(example of regular function) - to find the words containing "i"
some_words = ["potatoes", "certainly", shallow", "voice", "conversation", "more", "thirty", "needle"]


def contains_i(words):
    i_words = []
    for word in words:
        if "i" in word:
            i_words.append(word)
    return i_words
 
     
print(contains_i(some_words))
 
```

```(example of the same function but as a generator
some_words = ["potatoes", "certainly", shallow", "voice", "conversation", "more", "thirty", "needle"]


def contains_i(words):
    for word in words:
        if "i" in word:
            yeild word
            
       
print(list(contains_i(some_words)))
```
* we no longer need the empty list to hold
* we no longer need the return either, and we will need to convert the results to a list to view it when we print.
* Now we can save memory and reduce the number of lines of code


## Q.10 Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator? 
Firstly a decorator is a callable same way a function, methods and classes are callable therefore a decorator is a callable that takes another function as
an argument, extending the behaviour of that function without explicitly modifying that function.   


A good use of decorators will be to measure the time it takes for a function to run:
```commandline
def time_dec(func):

  def wrapper(*arg):
      t = time.time()
      result = func(*arg)
      print func.func_name, time.time()-t
      return result

  return wrapper


@time_dec
def myFunction(n):

   
# myFunction = time_dec(myFunction)

```

* the decorator allows us to modify the function
* It also allows us to write a more simple syntax using the add symbol which has been commented out
#### Some people abuse decorators as having one makes things very readable and simple and so people just use them all the time because of the fact in contrast decorators should be used when:
* Checking arguments type at runtime
* Benchmarking function calls
* Caching function results
* Counting function calls
* Checking metadata (permissions, roles, etc.)
* Metaprogramming

Decorators can be used with arguments, return values, classes and Python also has built-in decorators:
* @property – a decorator from builtins, which lets you define getters and setters for class properties
* @lru_cache – a decorator from the functools module. It memorizes function arguments and return values, handy for pure functions, like the factorial.
* @abstractmethod – a decorator from the abc module. Indicates that the method is abstract and implementation details are missing.

