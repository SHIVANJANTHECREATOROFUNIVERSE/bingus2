import streamlit as st
from answer import answers, strans, ttxt, refresh_page

st.title("Lesson 2: Data Types and Expressions")

# --- Tip State ---
if "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if "tip_q2" not in st.session_state:
    st.session_state.tip_q2 = False

# --- Question 1 ---
st.write("What is the data type of: `x = 3.14`?")
q1 = answers("q1_datatype_float", [
    ("1. int", False),
    ("2. string", False),
    ("3. float", True),
    ("4. bool", False),
])

if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("3.14 has a decimal — that's a float.", 3)
        st.session_state.tip_q1 = True

# --- Question 2 ---
st.write("What is the result of this expression: `5 + 3 * 2`?")
q2 = strans("q2_expression", ["11"])

if not st.session_state.tip_q2:
    if st.button("Want a tip for Q2?"):
        ttxt("Remember: multiplication comes before addition!", 3)
        st.session_state.tip_q2 = True

# --- Question 3 ---
st.write("Which statement is True?")
q3 = answers("q3_logic", [
    ("1. 10 > 5 and 3 < 1", False),
    ("2. 2 * 2 == 4", True),
    ("3. '5' == 5", False),
    ("4. None of the above", False),
])

# --- Final Gate ---
st.divider()
if q1 and q2 and q3:
    st.success("🎉 All questions correct! You may proceed.")
    st.page_link("pages/Lesson4.py", label="Go to Next Lesson")
else:
    st.warning("⏳ Please answer all questions correctly to continue.")
