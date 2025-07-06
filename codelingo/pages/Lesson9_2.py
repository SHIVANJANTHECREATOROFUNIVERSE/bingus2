import streamlit as st

st.subheader("Polymorphism")
st.write("""
Polymorphism allows methods to do different things based on the object that calls them. This is often achieved through method overriding in subclasses.
Here's an example of polymorphism using the `Dog` and `Puppy` classes:
```python
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Meow!"
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"
def animal_sound(animal):
    print(animal.speak())
dog = Dog("Buddy")
cat = Cat("Whiskers")
animal_sound(dog)  # Output: Buddy says Woof!
animal_sound(cat)  # Output: Whiskers says Meow!
```
In this example, both `Dog` and `Cat` classes have a `speak` method. The `animal_sound` function can accept any object that has a `speak` method, demonstrating polymorphism.
""")
st.subheader("Encapsulation")
st.write("""
Encapsulation is the concept of restricting access to certain components of an object. This is typically done by using private attributes and methods, which are not accessible from outside the class.
Here's an example of encapsulation:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."

    def get_balance(self):
        return self.__balance  # Public method to access private attribute
```
In this example, the `__balance` attribute is private and cannot be accessed directly from outside the `BankAccount` class. The `deposit` method allows adding funds to the account, and the `get_balance` method provides access to the balance.
""")


st.divider()
if st.button("Questions for the Lesson"):
    st.switch_page("pages/Lesson9questions.py")