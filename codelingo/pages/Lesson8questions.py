import streamlit as st
from answer import answers, strans, ttxt, refresh_page

st.title("Lesson 8: Error Handling Questions")

if tip_q1 := "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if tip_q2 := "tip_q2" not in st.session_state:
    st.session_state.tip_q2 = False
if tip_q3 := "tip_q3" not in st.session_state:
    st.session_state.tip_q3 = False
if tip_q4 := "tip_q4" not in st.session_state:
    st.session_state.tip_q4 = False

q1 = answers("q1_try_except", [
    ("1. It allows you to ignore errors", False),
    ("2. It lets you handle errors gracefully", True),
    ("3. It stops the program from running", False),
    ("4. It is used for debugging only", False),
], "What is the purpose of using try and except in Python?")

if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("It helps you handle errors without crashing the program.", 3)
        st.session_state.tip_q1 = True

q2 = answers("q2_finally", [
    ("1. It runs only if an error occurs", False),
    ("2. It always runs, regardless of errors", True),
    ("3. It is used to define functions", False),
    ("4. It is optional in error handling", False),
], "What does the finally block do in a try-except structure?")
if not st.session_state.tip_q2:
    if st.button("Need a tip for Q2?"):
        ttxt("It runs no matter what happens in the try-except.", 3)
        st.session_state.tip_q2 = True

q3 = answers("q3_multiple_exceptions", [
    ("1. It allows you to catch multiple errors in one block", True),
    ("2. It is used to ignore all errors", False),
    ("3. It can only catch one type of error", False),
    ("4. It is not recommended in Python", False),
], "What is the benefit of handling multiple exceptions together?")
if not st.session_state.tip_q3:
    if st.button("Need a tip for Q3?"):
        ttxt("You can handle different errors in one place.", 3)
        st.session_state.tip_q3 = True
q4 = strans("q4_custom_exception", ["CustomError", "MyError", "Exception"], "What is the name of the custom exception defined in the example?",''' class MyError(Exception):
    pass

def risky():
    raise MyError("Something specific went wrong!")

try:
    risky()
except MyError as e:
    print(e) ''')
if not st.session_state.tip_q4:
    if st.button("Need a tip for Q4?"):
        ttxt("It's present in the first line of code", 3)
        st.session_state.tip_q4 = True

st.divider()
if not (q1 and q2 and q3 and q4):
    st.warning("⏳ Please answer all questions correctly to continue.")
else:
    st.success("🎉 All questions correct! You may proceed.")
    if st.button("Next lesson"):
        st.switch_page("pages/Lesson9.py")