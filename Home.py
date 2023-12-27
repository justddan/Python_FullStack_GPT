import streamlit as st
from langchain.prompts import PromptTemplate

a = [1,2,3,4]

d = {"x":1}

a

d

st.selectbox("Choose your model", ("GPT-3","GPT-4"),)