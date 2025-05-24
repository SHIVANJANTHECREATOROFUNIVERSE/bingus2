import streamlit as st
import time

def _init_answer_store():
    if "answers" not in st.session_state:
        st.session_state.answers = {}

def refresh_page(delay: float = 0.5):
    """
    Forces a rerun after an optional delay.
    """
    time.sleep(delay)
    st.experimental_rerun()

def answers(question_id, options):
    """
    Multiple-choice question widget with answer validation and storage.
    """
    _init_answer_store()

    answered_correctly = st.session_state.answers.get(question_id, {}).get("correct", False)

    st.subheader(f"Question: {question_id}")

    if answered_correctly:
        selected = st.session_state.answers[question_id]["user_answer"]
        st.success(f"✅ You already answered correctly: {selected}")
        return True

    cols = st.columns(len(options))
    for i, (label, is_correct) in enumerate(options):
        with cols[i]:
            if st.button(label, key=f"{question_id}_{i}"):
                if is_correct:
                    st.session_state.answers[question_id] = {
                        "correct": True,
                        "user_answer": label
                    }
                    st.success("✅ Right answer!")
                    refresh_page()
                    return True
                else:
                    wrong()
    return False

def strans(question_id, correct_answers):
    """
    Text input question with multiple valid answers.
    """
    _init_answer_store()

    answered_correctly = st.session_state.answers.get(question_id, {}).get("correct", False)

    st.subheader(f"Question: {question_id}")

    if answered_correctly:
        saved = st.session_state.answers[question_id]["user_answer"]
        st.success(f"✅ You already answered correctly: {saved}")
        return True

    user_input = st.text_input("Your answer:", key=f"input_{question_id}")

    if user_input:
        if user_input.strip().lower() in [ans.lower() for ans in correct_answers]:
            st.session_state.answers[question_id] = {
                "correct": True,
                "user_answer": user_input.strip()
            }
            st.success("✅ Right answer!")
            refresh_page()
            return True
        else:
            st.error("❌ Try again.")
    return False

def wrong():
    st.error("❌ Try again.")

def ttxt(tip, second):
    """
    Displays a timed tip with countdown.
    """
    placeholder = st.empty()
    for remaining in range(second, 0, -1):
        placeholder.info(f"🕒 Your tip will appear in {remaining} seconds...")
        time.sleep(1)
    placeholder.success(tip)
