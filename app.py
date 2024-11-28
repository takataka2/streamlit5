import streamlit as st

st.write("これはstreamlitアプリです")

answer = st.button('Say hello')

if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')
