import streamlit as st
from answer import answers, strans, refresh_page, ttxt

st.title("Lesson 9: Object-Oriented Programming Questions")

if tip_q1 := "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False 
if tip_q2 := "tip_q2" not in st.session_state:
    st.session_state.tip_q2 = False
if tip_q3 := "tip_q3" not in st.session_state:  
    st.session_state.tip_q3 = False
if tip_q4 := "tip_q4" not in st.session_state:
    st.session_state.tip_q4 = False

q1 = answers("q1_class_definition", [
    ("1. A blueprint for creating objects", True),
    ("2. A type of variable", False),
    ("3. A function that returns an object", False),
    ("4. A way to store data in a list", False),
], "What is a class in Python?")
if not st.session_state.tip_q1:
    if st.button("Need a answer for Q1?"):
        ttxt("A class is like a blueprint for creating objects.", 3)
        st.session_state.tip_q1 = True  

q2 = answers("q2_inheritance", [
    ("1. It allows a class to inherit attributes and methods from another class", True),
    ("2. It is used to create new variables", False),
    ("3. It is a way to define functions", False),
    ("4. It is not supported in Python", False),
], "What is inheritance in object-oriented programming?")
if not st.session_state.tip_q2:
    if st.button("Need a answer for Q2?"):
        ttxt("Inheritance allows one class to use the properties of another.", 3)
        st.session_state.tip_q2 = True  

q3 = answers("q3_polymorphism", [
    ("1. It allows methods to do different things based on the object that calls them", True),
    ("2. It is a way to create new classes", False),
    ("3. It is used to store data in a class", False),
    ("4. It is not supported in Python", False),
], "What is polymorphism in object-oriented programming?")
if not st.session_state.tip_q3:
    if st.button("Need a answer for Q3?"):
        ttxt("Polymorphism allows methods to behave differently based on the object.", 3)
        st.session_state.tip_q3 = True
q4 = strans("q4_encapsulation", ["Private attributes", "Public methods", "Protected variables"], "What is encapsulation in object-oriented programming?", '''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."

    def get_balance(self):
        return self.__balance  # Public method to access private attribute''')
if not st.session_state.tip_q4:
    if st.button("Need a answer for Q4?"):
        ttxt("Encapsulation restricts access to certain attributes and methods.", 3)
        st.session_state.tip_q4 = True  

st.divider()
if not (q1 and q2 and q3 and q4):
    st.warning("⏳ Please answer all questions correctly to continue.")
else:
    st.success("✅ All answers are correct! You can now proceed to the next lesson.")
    if st.button("Next Lesson"):
        st.switch_page("pages/Lesson10.py")