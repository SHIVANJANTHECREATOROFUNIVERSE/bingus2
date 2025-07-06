import streamlit as st
from answer import answers, strans, ttxt, refresh_page

if "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if "tip_q2" not in st.session_state:
    st.session_state.tip_q2 = False
if "tip_q3" not in st.session_state:
    st.session_state.tip_q3 = False
if "tip_q4" not in st.session_state:
    st.session_state.tip_q4 = False

q1 = answers("q1_function", [
    ("1. def my_function():", True),
    ("2. function my_function():", False),
    ("3. my_function() = def:", False),
    ("4. def my_function[]:", False),
], "What is the correct way to define a function in Python?")

if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("Use 'def' followed by the function name and parentheses.", 3)
        st.session_state.tip_q1 = True

q2 = strans("q2_return", ["return", "yield"], "What keyword is used to return a value from a function?")
if not st.session_state.tip_q2:
    if st.button("Want a tip for Q2?"):
        ttxt("Think about how you send a value back from a function.", 3)
        st.session_state.tip_q2 = True

q3 = answers("q3_call", [
    ("1. my_function()", True),
    ("2. call my_function()", False),
    ("3. my_function[]", False),
    ("4. my_function:", False),
], "How do you call a function named `my_function`?")
if not st.session_state.tip_q3:
    if st.button("Want a tip for Q3?"):
        ttxt("Use the function name followed by parentheses.", 3)
        st.session_state.tip_q3 = True

q4 = strans("q4_parameters", ["parameters", "args", "arguments"], "What do you call the values passed to a function?")
if not st.session_state.tip_q4:
    if st.button("Want a tip for Q4?"):
        ttxt("These are the inputs you provide to a function.", 3)
        st.session_state.tip_q4 = True

st.divider()
if not (q1 and q2 and q3 and q4):
    st.warning("⏳ Please answer all questions correctly to continue.")
else:
    st.success("🎉 All questions correct! You may proceed.")
    if st.button("Next lesson"):
        st.switch_page("pages/Lesson6.py")