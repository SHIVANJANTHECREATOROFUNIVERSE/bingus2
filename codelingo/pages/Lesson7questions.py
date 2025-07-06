import streamlit as st
from answer import answers, strans, ttxt, refresh_page

st.title("Lesson 7: File Handling Questions")
st.divider()
st.subheader("THESE QUESTIONS WILL REQUIRE YOU TO OPEN YOUR OWN PYTHON CONSOLE OR IDE TO ASNSWER")
st.divider()
st.subheader("Exercise: Create and Write to a File")
st.write("Create a file named `myfile.txt` and write the following lines to it:")
exercise_code = '''# Create and write to a file
with open('myfile.txt', 'w') as file:
    file.write("This is my first line.\n")
    file.write("This is my second line.\n")
    file.write("This is my third line.\n")
print("File created and written successfully!")  # Confirmation message'''
st.code(exercise_code, language='python')
st.subheader("Exercise: Read and Print the File")
st.write("Read the contents of `myfile.txt` and print each line:")
exercise_read_code = '''# Read and print the file
with open('myfile.txt', 'r') as file:
    lines = file.readlines()  # Read all lines into a list
    for line in lines:
        print(line.strip())  # Print each line without extra spaces'''
st.code(exercise_read_code, language='python')

st.divider()
if st.button("Next lesson"):
    st.switch_page("pages/Lesson8.py")