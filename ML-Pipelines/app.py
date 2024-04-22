import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Feedback Predictor for Online Food Orders",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Feedback Predictor for Online Food Orders")

def load_model():
    with open("feedback.pkl","rb")as f:
        model=pkl.load(f)
    return model
def load_data(path):
    data=pd.read_csv(path)
    return data

data=load_data('onlinefoods.csv')
age=st.number_input("Enter your age: ")
gender=st.selectbox('Gender',data['Gender'].value_counts().index)
status=st.selectbox('Status',data['Marital Status'].value_counts().index)
occupation=st.selectbox('Gender',data['Occupation'].value_counts().index)
income=st.number_input("Enter your income: ")
education=st.selectbox('Education',data['Educational Qualifications'].value_counts().index)
family_size=st.number_input("Enter your family_size: ")
lattitude=st.number_input("Enter lattitude: ")
longitude=st.number_input("Enter longitude: ")
pin=longitude=st.number_input("Enter pin: ")
output=st.selectbox('Output',data['Output'].value_counts().index)

if(st.button('Predict')):
    # Load the model
    model=load_model()
    # Prepare the user data for prediction
    user_data={
        'Age':age,
        'Gender':gender,'Marital Status':status,'Occupation':occupation,
        'Monthly Income':income,'Educational Qualifications':education,
        'Family size':family_size,'latitude':lattitude,'longitude':longitude,
        'Pin code':pin,'Output':output
    }
    df=pd.DataFrame(user_data, index=[0])
    st.dataframe(df)
   
    # Prediction
    result=model.predict(df)[0]
    if(result==1):
        st.success('Feedback is positive')
    else:
        st.error("Feedback is negative")
