# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 12:54:51 2022

@author: asus
"""


import streamlit as st
import joblib
from PIL import Image


#%%


image = Image.open('deepspatial.jpg')
image_1=image.resize((180,30))
st.image(image_1)


#st.header("DSAI DIGI AGRI PLATFORM")
st.markdown('<div style="text-align: center; font-size:30px; font-weight:bold">DSAI DIGI AGRI PLATFORM</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; font-size:20px;">An SDG Inititative</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; font-size:16px;">&#169 Copyright 2022 DSAI</div>', unsafe_allow_html=True)

st.header("")



page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)



with st.form(key='myform'):
    area=st.number_input("Area (acres)")
    temp=st.number_input("Temperature (Degree Celsius)")
    precip=st.number_input("Precipitation (mm)")
    hum=st.number_input("Humidity (gms/CBM)")
        
        
    submit_button=st.form_submit_button(label='Calculate the Crop Yield')

model = joblib.load("Updated model.sav")

if submit_button:

    prediction=int(model.predict([[area,temp,precip,hum]])[0])
    
    op="The predicted Crop Yield = "+ str(prediction) + " kg/ha"
    st.subheader(op)

















