import streamlit as st

st.set_page_config(
    page_title="Lesson 8: Error Handling",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Lesson 8: Error Handling")

# --- Try & Except ---
st.subheader("Try and Except")
code_try_except = '''try:
    value = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")'''
st.code(code_try_except, language='python')

st.write("""
The `try` and `except` block in Python is used to catch and handle errors during program execution.

- Code inside the `try` block is attempted first.
- If an error occurs (like trying to convert a non-number to `int()`), Python stops executing the `try` block and jumps to the `except` block.
- This prevents the program from crashing and allows you to respond to the error gracefully.

In the example above, if the user enters something that can't be converted to a number (like "abc"), the program catches the `ValueError` and prints a friendly message.
""")

# --- Finally Block ---
st.subheader("Finally Block")
code_finally = '''try:
    file = open("data.txt")
    # Do something with the file
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleaning up...")'''
st.code(code_finally, language='python')

st.write("""
The `finally` block is used to define code that should run **no matter what happens** in the `try` and `except` blocks.

- If no error occurs, the `finally` block still runs.
- If an error **does** occur, and it's caught by an `except`, the `finally` block runs **after** the exception handling.
- It's commonly used for **cleanup tasks**, such as closing files or releasing resources.

In this example, whether or not the file is found, the message `"Cleaning up..."` will always be printed.
""")


# --- Multiple Exceptions ---
st.subheader("Handling Multiple Exceptions")
code_multi_exceptions = '''try:
    risky_code()
except (TypeError, ValueError) as e:
    print("An error occurred:", e)'''
st.code(code_multi_exceptions, language='python')

st.write("""
Sometimes, a block of code might raise **more than one type of exception**. Instead of writing separate `except` blocks for each, you can group them using a tuple.

- `(TypeError, ValueError)` means this block will catch **either** type of error.
- Using `as e` gives access to the actual error object, so you can print or log it.

In this example, if `risky_code()` raises a `TypeError` or `ValueError`, the error will be caught and displayed without crashing the program.
""")


# --- Custom Exceptions ---
st.subheader("Custom Exceptions")
code_custom_exception = '''class MyError(Exception):
    pass

def risky():
    raise MyError("Something specific went wrong!")

try:
    risky()
except MyError as e:
    print(e)'''
st.code(code_custom_exception, language='python')

st.write("""
Python lets you define your **own exception types** by creating a class that inherits from `Exception`.

- Custom exceptions are useful when you want to handle specific errors in your own way.
- They make your code cleaner, especially in larger projects.

In this example, `MyError` is a custom exception. The `risky()` function raises it, and it’s caught by the `except` block to display a custom message.
""")

# --- Navigation ---
st.divider()

st.write("Now, let's test your understanding of error handling with some questions.")
if st.button("Questions for Lesson"):
    st.switch_page("pages/Lesson8questions.py")
