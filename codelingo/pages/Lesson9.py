import streamlit as st

st.title("Lesson 9: Object-Oriented Programming")
st.write("""
In this lesson, we will explore the principles of Object-Oriented Programming (OOP) in Python. OOP is a programming paradigm that uses objects and classes to structure code in a way that is modular, reusable, and easier to maintain.
We will cover the following topics:
- Classes and Objects
- Attributes and Methods
- Inheritance
- Polymorphism
- Encapsulation
""")
st.subheader("Classes and Objects")
st.write("""
A class is a blueprint for creating objects. An object is an instance of a class. Classes encapsulate data for the object and methods to manipulate that data.
Here's a simple example of a class in Python:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
```
In this example, `Dog` is a class with an `__init__` method that initializes the object's attributes (`name` and `age`). The `bark` method allows the dog to bark.
""")
st.subheader("Attributes and Methods")
st.write("""
Attributes are variables that belong to an object, while methods are functions that belong to a class. You can access attributes and call methods using the dot notation.
Here's how you can create an object of the `Dog` class and access its attributes and methods:
```python
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
print(my_dog.bark())  # Output: Buddy says Woof!
```
""")
st.subheader("Inheritance")
st.write("""
Inheritance allows a class to inherit attributes and methods from another class. This promotes code reuse and establishes a relationship between classes.
Here's an example of inheritance:
```python
class Puppy(Dog):
    def __init__(self, name, age, training_level):
        super().__init__(name, age)
        self.training_level = training_level

    def bark(self):
        return f"{self.name} says Woof! (Training Level: {self.training_level})"
```
In this example, `Puppy` inherits from `Dog`. It can access the attributes and methods of `Dog`, and it can also override the `bark` method to include additional information about the training level.
""")

st.divider()
if st.button("Next page"):
    st.switch_page("pages/Lesson9_2.py")