#!/usr/bin/env python
# coding: utf-8

# In[1]:


from telnetlib import BM
from turtle import width
import numpy as np
import pickle


# In[4]:


filename="trained_model.sav"
load_model=pickle.load(open(filename,"rb"))


# In[ ]:


def diabetes_prediction(input_data):
 print("Given data")
 print(input_data)
 numpy_data=np.array(input_data)
 data=numpy_data.reshape(1,-1)
 #std_data=scaler.transform(data)
 prediction=load_model.predict(data)
 print("Outcome predicted: ",end="")
 print(prediction[0])
 if(prediction[0]==1):
    return "The patient is having diabetes"
 else:
    return "The patient is non diabetic"
    


# using streamlit library

# In[5]:


import streamlit as st

from PIL import Image
# In[7]:


def main():
    st.title("Diabetes_predictor")
    image = Image.open('diabetes_detected.jpg')
    st.image(image,width=250)
#getting inputs from the user
    Pregnancies=st.text_input("No of Pregnancies")
    if(Pregnancies.strip()==""):
        st.info("please enter the no of Pregnancies")
    Glucose=st.text_input("Glucose level")
    if(Glucose.strip()==""):
        st.info("please enter Glucose level")
    BloodPressure=st.text_input("Bloodpressure level")
    if(BloodPressure.strip()==""):
        st.info("please enter the BloodPressure")
    SkinThickness=st.text_input("SkinThickness value")
    if(SkinThickness.strip()==""):
        st.info("please enter the SkinThickness")
    Insulin=st.text_input("Insulin level")
    if(Insulin.strip()==""):
        st.info("please enter the Insulin level")
    BMI=st.text_input("BMI value")
    if(BMI.strip()==""):
         st.info("Please enter the BMI value")
    DiabetesPedigreeFunction=st.text_input("DiabetesPredigreeFunction")
    if(DiabetesPedigreeFunction.strip()==""):
        st.info("please enter the value of DiabetesPedigreeFunction")
    Age=st.text_input("Age of the person")
    if(Age.strip()==""):
        st.info("please enter the age of the person")
         
#code for prediction 
    diagnosis=""
    if(st.button("Diabetes_test_result")):
        if(Pregnancies=="" or Glucose=="" or BloodPressure=="" or SkinThickness=="" or Insulin=="" or BMI=="" or DiabetesPedigreeFunction=="" or Age==""):
         st.info("please fill all the fields")
        else:
         diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
         if(diagnosis== "The patient is having diabetes"):
            st.warning(diagnosis +"🥹")
         else:
            st.success(diagnosis +"😊")
if __name__ == '__main__':
    main()


# In[ ]:




