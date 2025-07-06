import streamlit as st

st.title("Lesson 5: Functions and loops")
st.write("In this lesson, we will explore functions and loops in Python, which are essential for writing reusable and efficient code.")
st.header("What are Functions?")
st.write("Functions are reusable blocks of code that perform a specific task. They allow you to encapsulate logic and call it multiple times without rewriting the code.")
st.subheader("Defining a Function")
code_function = '''def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  # Calling the function with an argument'''
st.code(code_function, language='python')
st.subheader("Returning Values")
code_return = '''def add(a, b):
    return a + b
    result = add(5, 3)
print(result)  # Outputs: 8'''
st.code(code_return, language='python')
st.subheader("Function Parameters and Arguments")
code_params = '''def multiply(x, y=2):  # y has a default value
    return x * y
    result = multiply(5)  # Uses default value for y
print(result)  # Outputs: 10
result = multiply(5, 3)  # Overrides default value
print(result)  # Outputs: 15'''
st.code(code_params, language='python')
st.header("What are Loops?")
st.write("Loops allow you to execute a block of code multiple times. The two main types of loops in Python are `for` loops and `while` loops.")
st.subheader("For Loops")
code_for_loop = '''for i in range(5):
    print(i)  # Prints numbers from 0 to 4'''
st.code(code_for_loop, language='python')
st.subheader("While Loops")
code_while_loop = '''count = 0
while count < 5:
    print(count)
    count += 1  # Increments count by 1 each iteration'''
st.code(code_while_loop, language='python')
st.subheader("Nested Loops")
code_nested_loops = '''for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")  # Prints combinations of i and j'''
st.code(code_nested_loops, language='python')

st.divider()
st.write("Want to proceed to next page?")
if st.button("Next Page"):
    st.switch_page("pages/Lesson5_1.py")

