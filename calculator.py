import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.radio("Operation",["Add","Subtract","Multiplication","Divide"])

result = None
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2
else:
    result = None

if result:
    st.success(f"Result:{result}")


