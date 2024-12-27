import streamlit as st
from PIL import Image

st.title("WELCOME TO MY FIRST APP")
st.header("WELCOME TO MY FIRST APP")
st.write("WELCOME TO MY FIRST APP")
st.subheader("WELCOME TO MY FIRST APP")
st.text("WELCOME TO MY FIRST APP")
st.markdown("@@WELCOME TO MY FIRST APP")
st.success("correct answer!")
st.error("error!")
st.warning("please enter correct answer")
st.info("information")
st.write(range(0,19))
img= Image.open("image.png")
st.image(img, width=200)

if st.checkbox("correct/incorrect"):
    st.text("you are selected")

radio = st.radio("national bird: ",("parrot","peacock"))
if radio == "parrot":
    st.success("correct")
else:
    st.error("wrong answer, it's peacock")

slect = st.selectbox("selection",("digital","analog"))
st.text(f"you love {slect}")
s=st.multiselect("multiselection:",("watch","shoe"))
st.text(f"you selected {s}")
if st.button("click this"):
    st.text("Welcome")
name= st.text_input("enter your name here..")
if st.button("submit"):
    result = name.title()
    st.success(result)

level = st.slider("select the level;", 1, 5)
st.text("selected level; ".format(2))
