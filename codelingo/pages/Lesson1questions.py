import streamlit as st
from pages.answer import answers, strans, wrong

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

st.write("What is the data type of x = 'Hello'?")
strans(["str", "String", "string"])
