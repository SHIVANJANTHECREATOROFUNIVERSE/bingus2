import streamlit as st
from answer import answers, strans, ttxt, refresh_page

st.set_page_config(initial_sidebar_state="collapsed")


st.title("Lesson 2: Variable Basics")

# --- Tip State Init ---
if "tip_q1" not in st.session_state:
    st.session_state.tip_q1 = False
if "tip_q3_1" not in st.session_state:
    st.session_state.tip_q3_1 = False
if "tip_q3_2" not in st.session_state:
    st.session_state.tip_q3_2 = False


q1 = answers("q1_assignment", [
    ("1. x='10'", False),
    ("2. x==10", False),
    ("3. x-10", False),
    ("4. x=10", True),
], "What is the correct way to assign a value to a variable?")

if not st.session_state.tip_q1:
    if st.button("Need a tip for Q1?"):
        ttxt("Use '=' for assignment, '==' for comparison.", 3)
        st.session_state.tip_q1 = True


q2 = answers("q2_value", [
    ("1. x", False),
    ("2. 5", True),
    ("3. null", False),
    ("4. idk", False),
], "What is the value of x after `x = 5`?")


q3 = strans("q3_type", ["str", "string", "String", "Str"], "What is the data type of x = 'Hello'?")

if not st.session_state.tip_q3_1:
    if st.button("Want a tip for Q3?"):
        ttxt("It's a text data type.", 3)
        st.session_state.tip_q3_1 = True

elif not st.session_state.tip_q3_2:
    if st.button("Want the answer for Q3?"):
        ttxt("It's 'string' or 'str'.", 5)
        st.session_state.tip_q3_2 = True



st.divider()
if not (q1 and q2 and q3):
    st.warning("⏳ Please answer all questions correctly to continue.")
else:
    st.success("🎉 All questions correct! You may proceed.")
    if st.button("Next lesson"):
        st.switch_page("pages/Lesson3.py")
