import streamlit as st
st.header("Type Conversion")
st.write("You can convert between different data types using built-in functions. Here are some common conversions:")
st.subheader("1. Converting to Integer")
code_to_int = '''x = 3.14
y = int(x)
print(y)  # Output: 3'''
st.code(code_to_int, language='python')
st.subheader("2. Converting to Float")
code_to_float = '''x = "5.67"
y = float(x)
print(y)  # Output: 5.67'''
st.code(code_to_float, language='python')
st.subheader("3. Converting to String")
code_to_str = '''x = 42
y = str(x)
print(y)  # Output: "42"'''
st.code(code_to_str, language='python')
st.subheader("4. Converting to Boolean")
code_to_bool = '''x = 0
y = bool(x)
print(y)  # Output: False'''
st.code(code_to_bool, language='python')
st.write("You can also use the `type()` function to check the data type of a variable:")
code_type = '''x = 10
print(type(x))  # Output: <class 'int'>'''
st.code(code_type, language='python')
st.write("Now, let's practice what you've learned with some questions.")
if st.button("Questions for Lesson 3"):
    st.switch_page("pages/Lesson3questions.py")
st.write("If you want to review the previous Page, click the button below.")
if st.button("Go back"):
    st.switch_page("pages/Lesson3.py")