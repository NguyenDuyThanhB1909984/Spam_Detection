from cProfile import label
from urllib import response
import streamlit as st
import requests
import json
import pandas as pd


url = 'http://localhost:8000/prediction'

st.header("Spam detection")

label = ['Spam email', 'non spam']


with st.form(key="predict_spam_email",clear_on_submit=True):
    data_email = st.text_input("Subject and body of the mail: ")
    submited = st.form_submit_button("Predict")
   


if submited:
    data = {"data": data_email}
    res = requests.post(url,json= data)
    st.write("This content: " + "\""+data_email+"\"")
    
    st.write("Result: " +"<b>"+label[res.json()] + "</b>",unsafe_allow_html=True)

