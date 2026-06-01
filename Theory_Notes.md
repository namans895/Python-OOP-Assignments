# OOPs Concepts in Python
## Introduction
OOP stands for Object Oriented Programming
It is a programming method in which we use classes and objects to solve real-world problems. OOP helps us organize the code properly and makes it reusable

Python supports OOP concepts such as:
- Class
- Object
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

# 1. Class
A class is a blueprint for creating objects
Example:
```python

class Student:
    pass
```

Here Student is a class

# 2. Object
An object is an instance of a class
Example:
```python
s1 = Student()
```
Here s1 is an object of Student class

# 3. Constructor
A constructor is a special function that runs automatically when an object is created
In Python we use __init__() as constructor
Example:
```python
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Naman")
```
# 4. Encapsulation
Encapsulation means wrapping data and methods into a single unit
It is used to protect data from direct access
Example:
```python
class BankAccount:
    def __init__(self):
        self.__balance = 1000
```
Here __balance is a private variable
Advantages:
- Data security
- Better control on data

# 5. Inheritance

Inheritance allows one class to use properties and methods of another class
Example:
```python
class Employee:
    def work(self):
        print("Working")

class Manager(Employee):
    pass
```
Here Manager inherits Employee.

Advantages:
- Code reuse
- Less coding
- Easy maintenance
- 
# 6. Polymorphism
Polymorphism means one method can have different forms
Example:
```python
class Car:
    def start(self):
        print("Car Starts")

class Bike:
    def start(self):
        print("Bike Starts")
```
The same method start() gives different outputs
Advantages:
- Flexibility
- Reusable code

# 7. Abstraction
Abstraction means hiding unnecessary details and showing only important information
Example:
```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```
Advantages:
- Hides complexity
- Makes code simple

# Difference Between Class and Object
Class-Blueprint,Logical entity ,Used to create objects 
Object-Instance,Physical entity, Created from class 

# Advantages of OOP
1. Code Reusability
2. Easy Maintenance
3. Better Security
4. Easy to Understand
5. Real World Representation

