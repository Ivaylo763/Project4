import streamlit as st
name = st.text_input("Въведи име")
age = st.number_input("Въведи възраст")
grade = st.number_input("Въведи оценка")

if age >= 18:
  st.write("Ти си пълнолетен")
else:
  st.write("Ти си непълнолетен")

  if grade < 3:
    st.write("Слаб(2)")
  if grade >= 3 && <3.5:
    st.write("Среден(3)")
  if grade >= 3.5 && grade < 4.5:
    st.write("Добър(4)")
  if grade >= 4.5 && grade < 5.5:
    st.write("Много добър(5)")
  if grade >= 5.5:
    st.write("Отличен(6)")

  
