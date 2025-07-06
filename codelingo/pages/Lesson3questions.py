import streamlit as st
from answer import answers, strans, ttxt, refresh_page

st.title("Questions for Lesson 3: Data Types and Expressions")

# --- Tip State ---
if "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if "tip_q2" not in st.session_state:
    st.session_state.tip_q2 = False
if "tip_q3" not in st.session_state:
    st.session_state.tip_q3 = False
if "tip_q4" not in st.session_state:
    st.session_state.tip_q4 = False

q1 = answers("q1_datatype_float", [
    ("1. int", False),
    ("2. string", False),
    ("3. float", True),
    ("4. bool", False),
],"What is the data type of: `x = 3.14`?")

if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("3.14 has a decimal — that's a float.", 3)
        st.session_state.tip_q1 = True


q2 = strans("q2_expression", ["11"], "What is the result of this expression: `5 + 3 * 2`?")

if not st.session_state.tip_q2:
    if st.button("Want a tip for Q2?"):
        ttxt("Remember: multiplication comes before addition!", 3)
        st.session_state.tip_q2 = True


q3 = answers("q3_logic", [
    ("1. 10 > 5 and 3 < 1", False),
    ("2. 2 * 2 == 4", True),
    ("3. '5' == 5", False),
    ("4. None of the above", False),
],"Which statement is True?")

if not st.session_state.tip_q3:
    if st.button("Want a tip for Q3?"):
        ttxt("Check each statement carefully.", 3)
        st.session_state.tip_q3 = True

q4 = answers("q4_boolean", [
    ("1. string", False),
    ("2. boolean", False),
    ("3. integer", False),
    ("4. float", True),
], "What is the data type of the y", "x = 3.1459 \ny = float(x)")

if not st.session_state.tip_q4:
    if st.button("Need a tip for Q4?"):
        soap =("**floats** are numbers with decimal  **string** are characters from abphabet **bool** is true and false **integer** is the number line")
        ttxt(soap, 3)
        st.session_state.tip_q4 = True
st.divider()
if not( q1 and q2 and q3 and q4):
    st.warning("⏳ Please answer all questions correctly to continue.")
else:
    st.success("🎉 All questions correct! You may proceed.")
    if st.button("next lesson"):
        st.switch_page("pages/Lesson4.py")
