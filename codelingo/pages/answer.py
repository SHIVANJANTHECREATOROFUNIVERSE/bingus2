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


def strans(correct_answers):
    answer = st.text_input("Your answer:")
    if not answer.strip():
        st.warning("Please enter something")
    elif answer.strip().lower() in [x.lower() for x in correct_answers]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Wrong answer")
