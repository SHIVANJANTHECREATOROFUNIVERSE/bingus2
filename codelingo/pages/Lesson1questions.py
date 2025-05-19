import streamlit as st

def wrong():
    st.write("Try again")

def answers(options):
    for label, is_correct in options:
        if st.button(label):
            if is_correct:
                st.success("✅ Right answer!")
            else:
                wrong()


st.write("What is the correct way to assign a value to a variable?")
options1 = [("1. x='10'", False),
    ("2. x==10", False),
    ("3. x-10", False),
    ("4. x=10", True),]
answers(options1)

st.write("What will be the value of x after x = 5?")
options2 = [
    ("1. x", False),
    ("2. 5", True),
    ("3. null", False),
    ("4. idk", False),
]
answers(options2)