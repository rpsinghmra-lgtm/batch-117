import streamlit as st
st.set_page_config(page_title="Number Addition",page_icon="🎯",layout="centered")
st.title(" Addition of two number")
st.caption("enter two number and it will return addtion of them")

form=st.form("ad_form")
num1=form.number_input("first number")
num2=form.number_input("second number")
submitted=form.form_submit_button("Calculate sum")

if submitted:
    result=num1+num2
    st.divider()
    st.success(F"Sum{result}")
    st.metric(label="Result",value=result)

for i in range(1,11):
    st.write(2,"x",i,"=",2*i)

for i in range(1,11):
    if i%2==0:
        st.write(i)
 
