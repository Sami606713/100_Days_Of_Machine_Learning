import streamlit as st
import pickle as pkl

st.set_page_config(
    page_title="Flower Classification",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Flower Classification")
def load_model():
    with open("iris.pkl","rb")as f:
        model=pkl.load(f)
    return model


sp_length=st.number_input("Enter Sepal Length")
sp_width=st.number_input("Enter Sepal Width")
pt_length=st.number_input("Enter Petal Length")
pt_width=st.number_input("Enter Petal Width")

if(st.button('Predict')):
    model=load_model()

    # Prepare the user data for prediction
    user_data=[[sp_length,sp_width,pt_length,pt_width]]
    result=model.predict(user_data)[0]
    if(result==0):
        st.success('Flower is setosa')
    elif(result==1):
        st.success('Flower is versicolor')
    elif(result==2):
        st.success('Flower is virginica')
