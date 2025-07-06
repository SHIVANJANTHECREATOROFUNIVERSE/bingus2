import streamlit as st

st.title("Lesson 10: Advanced topics in Python")
st.write("This lesson covers advanced topics in Python, including decorators, generators, and context managers.")

st.subheader("1. Decorators")
st.write("Decorators are a way to modify the behavior of a function or class. They are often used for logging, access control, and caching.")
st.code("""
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print("Display function executed")
display()
""", language='python')
st.subheader("2. Generators")
st.write("Generators are a way to create iterators in Python. They allow you to iterate over a sequence of values without storing them all in memory at once.")
st.code("""
def generator_function():
    for i in range(5):
        yield i * 2
gen = generator_function()
for value in gen:
    print(value)
""", language='python')
st.subheader("3. Context Managers")
st.write("Context managers are used to manage resources, such as files or network connections, ensuring they are properly cleaned up after use.")
st.code("""
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
""", language='python')


if st.button("Questions for the lesson"):
    st.switch_page("pages/Lesson10questions.py")