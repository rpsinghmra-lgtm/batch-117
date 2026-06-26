import streamlit as st
st.set_page_config(page_title="Subtraction",page_icon="◀—▶",layout="centered")
st.title("Subtraction of two numbers")
st.caption("Enter two numbers and it will return subtraction of them")
form=st.form("add_form")
num1=form.number_input("enter a number")
num2=form.number_input("enter another number")
submitted=form.form_submit_button("calculate subtraction")
if submitted:
    result=num1-num2
    st.success(F"Sub{result}")
    st.metric(label="Result",value=result)
