import streamlit as st

weight = st.number_input("Enter your weight in kgs: ")


h_format = st.radio("your height in:",("cms","mtr","feet"))

if h_format=="cms":
    height = st.number_input("height in cm: ")
elif h_format=="mtr":
    height = st.number_input("Enter your height in meter: ")
elif h_format=="feet":
    height = st.number_input("enter your height in feet: ")
else:
    st.warning("Please select the height format")

bmi_button = st.button("Calculate BMI")
if bmi_button:
    bmi = weight/height*height
    st.success(f"your bmi index is : {bmi}")
    if bmi>27:
        st.warning("Over weight!")
    else:
        st.success("under weight")


