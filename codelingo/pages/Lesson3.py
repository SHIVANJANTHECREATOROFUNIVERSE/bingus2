import streamlit as st


st.title("🎓 Lesson 3: Data Types and Type Conversion")
st.write("In this lesson, we will explore different data types in Python and how to convert between them.")
st.header("What are Data Types?")
st.write("Data types are classifications of data that tell the interpreter how to handle the data. Python has several built-in data types, including:")
st.subheader("1. Integers")
st.write("Integers are whole numbers, both positive and negative, without any decimal points.")
code_int = '''x = 10
y = -5
print(x, y)'''
st.code(code_int, language='python')
st.subheader("2. Floats")
st.write("Floats are numbers that contain decimal points.")
code_float = '''pi = 3.14
gravity = 9.81
print(pi, gravity)'''
st.code(code_float, language='python')
st.subheader("3. Strings")
st.write("Strings are sequences of characters enclosed in quotes (single or double).")
code_str = '''name = "Alice"
greeting = 'Hello, World!'
print(name, greeting)'''
st.code(code_str, language='python')
st.subheader("4. Booleans")
st.write("Booleans represent truth values: `True` or `False`.")
code_bool = '''is_active = True
is_logged_in = False
print(is_active, is_logged_in)'''
st.code(code_bool, language='python')

if st.button("Next page"):
    st.switch_page("pages/Lesson3_1.py")
