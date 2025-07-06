import streamlit as st
from answer import answers, strans, refresh_page, ttxt

st.title("Lesson 10: Advanced Python Topics Questions")
if tip_q1 := "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if tip_q2 := "tip_q2" not in st.session_state:
    st.session_state.tip_q2 = False
if tip_q3 := "tip_q3" not in st.session_state:
    st.session_state.tip_q3 = False
if tip_q4 := "tip_q4" not in st.session_state:  
    st.session_state.tip_q4 = False

q1 = answers("q1_decorators", [
    ("1. A way to modify the behavior of a function or class", True),
    ("2. A type of variable", False),
    ("3. A function that returns an object", False),
    ("4. A way to store data in a list", False),
], "What is a decorator in Python?")
if not st.session_state.tip_q1:
    if st.button("Need a answer for Q1?"):
        ttxt("A decorator is a way to modify the behavior of a function or class.", 3)
        st.session_state.tip_q1 = True
q2 = answers("q2_generators", [
    ("1. A way to create iterators in Python", True),
    ("2. A type of variable", False),
    ("3. A function that returns an object", False),
    ("4. A way to store data in a list", False),
], "What is a generator in Python?")    
if not st.session_state.tip_q2:
    if st.button("Need a answer for Q2?"):
        ttxt("A generator is a way to create iterators in Python.", 3)
        st.session_state.tip_q2 = True
q3 = answers("q3_context_managers", [
    ("1. Used to manage resources like files or network connections", True),
    ("2. A type of variable", False),
    ("3. A function that returns an object", False),
    ("4. A way to store data in a list", False),
], "What is a context manager in Python?")
if not st.session_state.tip_q3:
    if st.button("Need a answer for Q3?"):
        ttxt("A context manager is used to manage resources like files or network connections.", 3)
        st.session_state.tip_q3 = True
q4 = strans("q4_decorator_example", ["@decorator_function", "@generator_function", "@context_manager"], "What is the correct way to apply a decorator in Python?", '''def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print("Display function executed")
display()''')
if not st.session_state.tip_q4:
    if st.button("Need a answer for Q4?"):
        ttxt("The correct way to apply a decorator is using the @ symbol followed by the decorator function name.", 3)
        st.session_state.tip_q4 = True

st.divider()
if not q1 and not q2 and not q3 and not q4:
    st.warning("⏳ Please answer all questions correctly to continue.")
else:
    st.success("✅ All questions answered correctly! You can now proceed to the final project.")
    if st.button("Go to Final Project"):
        st.switch_page("pages/FinalProject.py")