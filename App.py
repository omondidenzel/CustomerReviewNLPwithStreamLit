import streamlit as st
import pickle
import pandas as pd 

st.header("Customer review predictor" ,divider='rainbow')

st.write("""This apps predicts **reviews** by customers.""")

review = st.text_input("Review input","Type in your review")

#Load model
file_name = "LogisticRegressionModel.pkl"
loadfile = open(file_name, 'rb')
loadedModel = pickle.load(loadfile)
value = loadedModel.predict([review])


st.subheader('Prediction')
st.write(value)
