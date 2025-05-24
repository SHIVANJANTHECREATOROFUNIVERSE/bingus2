import streamlit as st
from answer import answers, strans, ttxt, refresh_page

st.title("Lesson 1: Variable Basics")

# --- Tip State Init ---
if "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if "tip_q3_1" not in st.session_state:
    st.session_state.tip_q3_1 = False
if "tip_q3_2" not in st.session_state:
    st.session_state.tip_q3_2 = False

# --- Question 1 ---
st.write("What is the correct way to assign a value to a variable?")
q1 = answers("q1_assignment", [
    ("1. x='10'", False),
    ("2. x==10", False),
    ("3. x-10", False),
    ("4. x=10", True),
])

if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("Use '=' for assignment, '==' for comparison.", 3)
        st.session_state.tip_q1 = True

# --- Question 2 ---
st.write("What is the value of x after `x = 5`?")
q2 = answers("q2_value", [
    ("1. x", False),
    ("2. 5", True),
    ("3. null", False),
    ("4. idk", False),
])

# --- Question 3 ---
st.write("What is the data type of x = 'Hello'?")
q3 = strans("q3_type", ["str", "string", "String"])

if not st.session_state.tip_q3_1:
    if st.button("Want a tip for Q3?"):
        ttxt("It's a text data type.", 3)
        st.session_state.tip_q3_1 = True
        refresh_page(2)
elif not st.session_state.tip_q3_2:
    if st.button("Want the answer for Q3?"):
        ttxt("It's 'string' or 'str'.", 5)
        st.session_state.tip_q3_2 = True
refresh_page(2)
# --- Next Lesson Logic ---
st.divider()
if q1 and q2 and q3:
    st.success("🎉 All questions correct! You may proceed.")
    st.page_link("pages/Lesson3.py", label="Go to Next Lesson")
else:
    st.warning("⏳ Please answer all questions correctly to continue.")
    refresh_page(2)
