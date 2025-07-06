import streamlit as st

st.title("🎓 Lesson 2: Variables")
st.write("Let's learn how to use variables in Python.")
st.header("What is a Variable?")
st.write("A variable is a name that refers to a value. It allows you to store data and manipulate it later in your code.")
st.header("Creating a Variable")
st.write("To create a variable, you simply assign a value to a name using the `=` operator. For example:")
code = '''x = 5
print(x)'''

st.code(code, language='python')
st.caption("<b>In this example, we created a variable `x` and assigned it the value `5`. We then printed the value of `x`.</b>", unsafe_allow_html = True)
st.header("Variable Naming Rules")
st.write("1. Variable names can contain letters, numbers, and underscores (_).")
st.write("2. Variable names must start with a letter or an underscore.")
st.write("3. Variable names are case-sensitive (e.g., `myVar` and `myvar` are different variables).")
st.header("Examples of Variables")
st.write("Here are some examples of valid variable names:")
st.code('''my_variable = 10
anotherVariable = "Hello"
_var123 = 3.14
myVar = True''', language='python')
st.write("Try questions now?")
if st.button("Questions for Lesson 2"):
    st.switch_page("pages/Lesson2questions.py")