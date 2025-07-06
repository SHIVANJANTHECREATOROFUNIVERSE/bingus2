import streamlit as st

st.title("Lesson 7: File Handling in Python")
st.write("In this lesson, we will learn how to handle files in Python, including reading from and writing to files.")
st.header("What is File Handling?")
st.write("File handling is the process of reading from and writing to files on your computer. Python provides built-in functions to handle files easily.")
st.subheader("Opening a File")
code_open_file = '''# Open a file in read mode
file = open('example.txt', 'r')  # 'r' for read mode
content = file.read()  # Read the entire content of the file
file.close()  # Close the file after reading
print(content)  # Print the content of the file'''
st.code(code_open_file, language='python')
st.subheader("Writing to a File")
code_write_file = '''# Open a file in write mode
file = open('output.txt', 'w')  # 'w' for write mode
file.write("Hello, World!\n")  # Write a line to the file
file.write("This is a new line.\n")  # Write another line
file.close()  # Close the file after writing
print("File written successfully!")  # Confirmation message'''
st.code(code_write_file, language='python')
st.subheader("Appending to a File")
code_append_file = '''# Open a file in append mode
file = open('output.txt', 'a')  # 'a' for append mode
file.write("This line is appended to the file.\n")  # Append a line to the file
file.close()  # Close the file after appending
print("Line appended successfully!")  # Confirmation message'''
st.code(code_append_file, language='python')
st.subheader("Reading a File Line by Line")
code_read_lines = '''# Open a file in read mode
file = open('example.txt', 'r')  # 'r' for read mode
lines = file.readlines()  # Read all lines into a list
for line in lines:
    print(line.strip())  # Print each line without extra spaces
file.close()  # Close the file after reading'''
st.code(code_read_lines, language='python')
st.subheader("Using 'with' Statement for File Handling")
code_with_statement = '''# Using 'with' statement for file handling
with open('example.txt', 'r') as file:  # Automatically closes the file
    content = file.read()  # Read the entire content of the file
    print(content)  # Print the content of the file'''
st.code(code_with_statement, language='python')

st.divider()
st.write("Now, let's test your understanding of file handling with some questions.")
if st.button("Questions for Lesson"):
    st.switch_page("pages/Lesson7questions.py")