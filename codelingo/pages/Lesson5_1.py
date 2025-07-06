import streamlit as st

st.subheader("Loop Control Statements")
code_control_statements = '''for i in range(5):
    if i == 2:
        continue  # Skips the rest of the loop when i is 2
    print(i)  # Prints numbers except 2

for i in range(5):
    if i == 3:
        break  # Exits the loop when i is 3
    print(i)  # Prints numbers until 3'''
st.code(code_control_statements, language='python')

# --- Combining Functions and Loops ---
st.subheader("Combining Functions and Loops")
code_combined = '''def print_numbers(n):
    for i in range(n):
        print(i)

print_numbers(5)  # Calls the function to print numbers from 0 to 4'''
st.code(code_combined, language='python')

# --- Recursion ---
st.subheader("Recursion")
code_recursion = '''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)  # Computes 5! (factorial of 5)
print(result)  # Outputs: 120'''
st.code(code_recursion, language='python')

# --- Lambda Functions ---
st.subheader("Lambda Functions")
code_lambda = '''add = lambda x, y: x + y
result = add(5, 3)  # Calls the lambda function to add 5 and 3
print(result)  # Outputs: 8'''
st.code(code_lambda, language='python')


# --- Navigation ---
st.divider()
st.write("Want to return to the previous page?")
if st.button("Last Page"):
    st.switch_page("pages/Lesson5.py")
st.write("Want to proceed to next page?")
if st.button("Next Page"):
    st.switch_page("pages/Lesson5_2.py")

