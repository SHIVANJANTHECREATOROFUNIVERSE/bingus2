import streamlit as st

st.title("🎓 Lesson 1: Basics of python")
st.write("Lets learn the basics of python")
st.subheader("Python is like the lego blocks of coding. They stick with other code peices without even glue")
st.write("Lets see some example of python codes")

st.markdown("#### Simple print code")
code_example = '''print("Hello world")'''
st.code(code_example, language='python')

st.markdown("#### Simple variable input code")
code_example2 = '''x = "Hello, Friend" '''
st.code(code_example2, language = 'python')


st.caption("Tip: The functions and statements in python are all case sensitive")
st.caption("Example: print✅ and Print❌")

st.write("Want to try some questions now?")
st.page_link("pages/Lesson1questions.py", label="Questions for Lesson 1")