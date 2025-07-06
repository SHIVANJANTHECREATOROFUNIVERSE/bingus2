import streamlit as st
from answer import answers, strans, ttxt, refresh_page

st.title("Lesson 6: Modules and Packages Questions")
if "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if "tip_q2" not in st.session_state:
    st.session_state.tip_q2 = False
if "tip_q3" not in st.session_state:
    st.session_state.tip_q3 = False
if "tip_q4" not in st.session_state:
    st.session_state.tip_q4 = False

q1 = answers("q1_import", [
    ("1. import math", False),
    ("2. from math import sqrt", True),
    ("3. math.sqrt(16)", False),
    ("4. import math.sqrt", False),
], "What is the correct way to import the math module and use its sqrt function? given that math is already imported.")
if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("Use 'import' or 'from ... import' to bring in modules.", 3)
        st.session_state.tip_q1 = True

q2 = strans("q2_create_module", ["santa.py", ".py", "py"], "What is the file extension for a Python module named 'santa'?")
if not st.session_state.tip_q2:
    if st.button("Want a tip for Q2?"):
        ttxt("Python modules are typically saved with a .py extension.", 3)
        st.session_state.tip_q2 = True

q3 = answers("q3_package", [
    ("my_package/\\_\\_init_\\_\\.py", True),
    ("my_package.py", False),
    (" \\_\\_init_\\_\\.py", False),
    (" package.py", False),
], "What is the correct way to create a package in Python?")
if not st.session_state.tip_q3:
    if st.button("Want a tip for Q3?"):
        ttxt("Packages are directories with an __init__.py file.", 3)
        st.session_state.tip_q3 = True

q4 = strans("q4_use_package", ["from package import greet"], "How do you use a function named as greet from a module named package?")
if not st.session_state.tip_q4:
    if st.button("Want a tip for Q4?"):
        ttxt("Use 'from ... import' or 'import' to access package functions.", 3)
        st.session_state.tip_q4 = True

st.divider()
if not (q1 and q2 and q3 and q4):
    st.warning("⏳ Please answer all questions correctly to continue.")
else:
    st.success("🎉 All questions correct! You may proceed.")
    if st.button("Next lesson"):
        st.switch_page("pages/Lesson7.py")