import streamlit as st

st.title("Lesson 4: Control Structures")
st.write("In this lesson, we will explore control structures in Python, which allow us to control the flow of our programs based on certain conditions.")
st.header("What are Control Structures?")
st.write("Control structures are constructs that dictate the order in which statements are executed in a program. They include conditional statements and loops.")
st.subheader("1. Conditional Statements")
st.write("Conditional statements allow us to execute certain blocks of code based on whether a condition is true or false.")
code_if = '''x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")'''
st.code(code_if, language='python')
st.subheader("2. Loops")
st.write("Loops allow us to repeat a block of code multiple times. The two main types of loops in Python are `for` loops and `while` loops.")
code_for = '''for i in range(5):
    print(i)  # Prints numbers from 0 to 4'''
st.code(code_for, language='python')
code_while = '''count = 0
while count < 5:
    print(count)
    count += 1  # Increments count by 1 each iteration'''
st.code(code_while, language='python')
st.subheader("3. Nested Control Structures")
st.write("You can nest control structures within each other to create more complex logic.")
code_nested = '''x = 10
if x > 5:
    for i in range(3):
        print(f"x is greater than 5, iteration {i}")'''
st.code(code_nested, language='python')

if st.button("Questions for Lesson 4"):
    st.switch_page("pages/Lesson4questions.py")
