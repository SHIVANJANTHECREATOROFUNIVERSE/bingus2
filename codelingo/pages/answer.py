import streamlit as st


def answers(options):
    for label, is_correct in options:
        if st.button(label):
            if is_correct:
                st.success("✅ Right answer!")
            else:
                wrong()

def wrong():
    st.write("Try again")


def strans(b):
    a = st.text_input("Your answer:")
    if a == b:
        st.success("Correct!")
    elif a != b :
        st.write("wrong answer")
