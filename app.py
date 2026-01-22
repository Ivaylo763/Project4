import streamlit as st
name = st.text_input("Въведи име")
age = st.number_input("Въведи възраст")
grade = st.number_input("Въведи оценка")

if age >= 18:
  st.write("Ти си пълнолетен")
else:
  st.write("Ти си непълнолетен")
