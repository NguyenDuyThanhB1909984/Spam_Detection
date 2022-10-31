# File phía client dùng để phân loại email


from cProfile import label
from urllib import response
import streamlit as st
import requests
import json
import pandas as pd

# link hoạt động của api đã viết ở file main.py
url = 'http://localhost:8000/prediction'

# Header của website
st.header("Spam detection")


# Nhãn của email
label = ['Spam email', 'non spam']

# Tạo form để người dùng nhập, gởi dữ liệu phân loại email 
with st.form(key="predict_spam_email",clear_on_submit=True):
    data_email = st.text_input("Subject and body of the mail: ")
    submited = st.form_submit_button("Predict")
   

# Gởi dữ liệu lên api để xử lý
if submited:
    data = {"data": data_email}
    res = requests.post(url,json= data)
    st.write("This content: " + "\""+data_email+"\"")
    
    st.write("Result: " +"<b>"+label[res.json()] + "</b>",unsafe_allow_html=True)

