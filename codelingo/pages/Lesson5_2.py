import streamlit as st

# --- List Comprehensions ---
st.subheader("List Comprehensions")
code_list_comprehension = '''squares = [x**2 for x in range(10)]  # Creates a list of squares from 0 to 9
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'''
st.code(code_list_comprehension, language='python')

# --- Decorators ---
st.subheader("Decorators")
code_decorators = '''def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()  # Calls the decorated function'''
st.code(code_decorators, language='python')

# --- Generators ---
st.subheader("Generators")
code_generators = '''def generator_function():
    for i in range(5):
        yield i  # Yields a value each time the generator is called

gen = generator_function()
for value in gen:
    print(value)  # Prints values from 0 to 4'''
st.code(code_generators, language='python')


st.divider()
st.write("Want to return to the previous page?")
if st.button("Last page"):
    st.switch_page("pages/Lesson5_1.py")
st.write("Want to practice with some questions now?")
if st.button("Questions for Lesson 5"):
    st.switch_page("pages/Lesson5questions.py")
