import streamlit as st
st.set_page_config(page_title="Multiplication",page_icon="⨝",layout="centered")
st.title("Multiplication of numbers")
st.caption("enter two number and it will return multiply of them")
form=st.form("add_form")
num1=form.number_input("enter first number")
num2=form.number_input("enter second number")
submitted=form.form_submit_button("calculate multiplication")
if submitted:
    result=num1*num2
    st.metric(label="result",value=result)