import streamlit as st
from answer import answers, strans, ttxt, refresh_page


st.title("Lesson 1: Questions for python Basics")

if "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if "tip_q2" not in st.session_state:
    st.session_state.tip_q2 = False
if "tip_q2_1" not in st.session_state:
    st.session_state.tip_q2_1 = False
if "tip_q3" not in st.session_state:
    st.session_state.tip_q3 = False




q1 = answers("q1_assignment", [
    ("1. Display'", False),
    ("2. Print", False),
    ("3. open", False),
    ("4. print", True),
], "What is missing here?", '''___(Hello, World!)''')

if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("All the functions/statements in python are case sensitive", 3)
        st.session_state.tip_q1 = True

code2 = ''' print(2 + 3 * 4)
'''
st.code(code2, language = "python")

q2 = answers("q2_assignment", [
    ("1. 20", False),
    ("2. 14", True),
    ("3. 24", False),
    ("3. It's not possible", False)
], "What will the following code output?")



if not st.session_state.tip_q2:
    if st.button("Need a tip for Q2?"):
        ttxt("Equations in a print statement are performed as suggested", 3)
        st.session_state.tip_q2 = True

if not st.session_state.tip_q2_1:
    if st.button("Need another tip for Q2?"):
        ttxt("Multiplications comes before addition", 3)
        st.session_state.tip_q2_1 = True

q3 = strans("q3_string", ["""print("ninety nine dogs")""" , "print('ninety nine dogs')"], "How will you print 'ninety nine dogs'")

if not st.session_state.tip_q3:
    if st.button("Need a tip for Q3?"):
        ttxt("Be careful of the capitalization", 5)
        st.session_state.tip_q3 = True
        



st.divider()
if not (q1 and q2 and q3):
    st.warning("⏳ Please answer all questions correctly to continue.")
else:
    st.success("🎉 All questions correct! You may proceed.")
    if st.button("Next lesson"):
        st.switch_page("pages/Lesson2.py")
