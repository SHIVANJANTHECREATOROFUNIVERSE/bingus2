import streamlit as st

st.title("Lesson 6: Modules and Packages")
st.write("In this lesson, we will learn about modules and packages in Python, which allow us to organize our code into reusable components.")
st.header("What are Modules and Packages?")
st.write("Modules are files containing Python code that can define functions, classes, and variables. Packages are a way of organizing related modules into a directory hierarchy.")
st.subheader("1. Importing Modules")
code_import = '''import math
print(math.sqrt(16))  # Outputs: 4.0'''
st.code(code_import, language='python')
st.subheader("2. Creating a Module")
code_create_module = '''# my_module.py
def greet(name):
    return f"Hello, {name}!"'''
st.code(code_create_module, language='python')
st.subheader("3. Using Packages")
code_package = '''# my_package/__init__.py
from .my_module import greet
# my_package/my_module.py
def greet(name):
    return f"Hello from the package, {name}!"'''
st.code(code_package, language='python')

st.divider()
if st.button("Questions for Lesson 6"):
    st.switch_page("pages/Lesson6questions.py")