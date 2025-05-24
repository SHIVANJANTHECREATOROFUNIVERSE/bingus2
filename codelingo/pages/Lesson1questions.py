import streamlit as st
from answer import answers, strans, ttxt, refresh_page

st.title("Lesson 1: Questions for python Basics")

if "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if "tip_q3_1" not in st.session_state:
    st.session_state.tip_q3_1 = False

st.write("What is missing here?")
code_ex = '''___(Hello, World!)'''
st.code(code_ex , language  = "python")

q1 = answers("q1_assignment", [
    ("1. Display'", False),
    ("2. Print", False),
    ("3. open", False),
    ("4. print", True),
])

if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("All the functions/statements in python are case sensitive", 3)
        st.session_state.tip_q1 = True
