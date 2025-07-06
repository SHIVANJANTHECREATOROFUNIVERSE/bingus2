import streamlit as st
from answer import answers, strans, ttxt, wrong, refresh_page
st.title("Questions for Lesson 4: Control Structures")

if "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if "tip_q2" not in st.session_state:
    st.session_state.tip_q2 = False
if "tip_q3" not in st.session_state:
    st.session_state.tip_q3 = False



q1 = answers("q1_if", [
    ("1. if x > 5:", True),
    ("2. elf x < 5:", False),
    ("3. candice x == 5:", False),
    ("4. santa_clause x != 5:", False),
], "What is the syntax for a conditional statement in Python?")

if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("Python uses 'if', 'elif', and 'else' for conditional statements.", 3)
        st.session_state.tip_q1 = True

q2 = answers("q2_loop", [
    ("1. for i in range(5):", True),
    ("2. while i < 5:", False),
    ("3. loop i from 0 to 5:", False),
    ("4. repeat i until 5:", False),
], "What is the correct syntax for a 'for' loop in Python?")

if not st.session_state.tip_q2:
    if st.button("Need a tip for Q2?"):
        ttxt("Use 'for' followed by a variable and 'in range()' for loops.", 3)
        st.session_state.tip_q2 = True

q3 = strans("q3_nested", ["nested loops", "nested control structures"], "What do we call control structures inside other control structures?")

if not st.session_state.tip_q3:
    if st.button("Want a tip for Q3?"):
        ttxt("Think about how you can put one control structure inside another.", 3)
        st.session_state.tip_q3 = True

st.divider()
if not (q1 and q2 and q3):
    st.warning("⏳ Please answer all questions correctly to continue.")
else:
    st.success("🎉 All questions correct! You may proceed.")
    if st.button("Next lesson"):
        st.switch_page("pages/Lesson5.py")