import streamlit as st

st.set_page_config(layout="wide",
                   initial_sidebar_state="collapsed")

st.title("INDEX FOR CODING LESSONS")
st.write("Welcome to the index page for coding lessons. Here you can navigate to different lessons and their respective questions.")
st.subheader("Available Lessons:")

lesson = [ 
    ("Lesson 1: Basics of Python", "pages/Lesson1.py"),
    ("Lesson 2: Variables", "pages/Lesson2.py"),
    ("Lesson 3: Data Types", "pages/Lesson3.py"),
    ("Lesson 4: Control Structures", "pages/Lesson4.py"),
    ("Lesson 5: Functions", "pages/Lesson5.py"),
    ("Lesson 6: Modules and Packages", "pages/Lesson6.py"),
    ("Lesson 7: File Handling", "pages/Lesson7.py"),
    ("Lesson 8: Error Handling", "pages/Lesson8.py"),
    ("Lesson 9: Object-Orientation", "pages/Lesson9.py"),
    ("Lesson 10: Advanced Topics", "pages/Lesson10.py"),
    ("Lesson 11: Final Project", "pages/FinalProject.py")
]
column = st.columns(3)

for index, (name, path) in enumerate(lesson):
    with column[index % 3]:
        if st.button(f"{name}"):
            st.switch_page(path)