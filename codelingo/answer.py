import streamlit as st
import time

def _init_answer_store():
    if "answers" not in st.session_state:
        st.session_state.answers = {}

def answers(question_id, options, label= None, py_ex= None):
    _init_answer_store()

    answered_correctly = st.session_state.answers.get(question_id, {}).get("correct", False)

    st.subheader(f"Question: {label or question_id}")
    
    if py_ex:
        st.code(py_ex, language = "python")


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

def strans(question_id, correct_answers, label= None, py_ex = None):
   
    _init_answer_store()

    answered_correctly = st.session_state.answers.get(question_id, {}).get("correct", False)

    st.subheader(f"Question: {label or question_id}")
    if py_ex:
        st.code(py_ex, language = "python")

    if answered_correctly:
        saved = st.session_state.answers[question_id]["user_answer"]
        st.success(f"✅ You already answered correctly: {saved}")
        return True

    user_input = st.text_input("Your answer:", key=f"input_{question_id}")

    if user_input:
        if user_input.strip() in [ans for ans in correct_answers]:
            st.session_state.answers[question_id] = {
                "correct": True,
                "user_answer": user_input.strip()
            }
            st.success("✅ Right answer!")
            refresh_page()
            return True
        else:
            wrong()
    return False

def wrong():
    st.error("❌ Try again.")

def ttxt(tip, second):
    placeholder = st.empty()
    for i in range(second, 0, -1):
        placeholder.info(f"🕒 Your tip will appear in {i} seconds...")
        time.sleep(1)
    placeholder.success(tip)

def refresh_page(delay: float = 0.5):
    time.sleep(delay)
    st.rerun()

# def points(Yes, No, Total):
