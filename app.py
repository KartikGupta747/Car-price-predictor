import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved model
with open('LinearRegressionModel.pkl', 'rb') as f:
    model = pickle.load(f)

data=pd.read_csv("cleaned_data.csv")

years=range(1990,2026)
fules=sorted(data['fuel_type'].unique())

# App Title
st.title("Welcome To Car Price Predictor")
st.header('This app predicts the price of car you want to sell.')
st.subheader('Try filling the details below:')

Companies=sorted(data['company'].unique())
company=st.selectbox('Select the Company:',Companies)

Models=sorted(data[data['company']==company]['name'].unique())
name=st.selectbox("Select the Model:",Models)

year=st.selectbox("Select the Year of Purchase:",years)

fule=st.selectbox("Select the Fule Type:",fules)

distance=st.number_input("Enter the number of Kilometres that the car has travelled:",0,step=1000)

input_df=pd.DataFrame([[name,company,year,distance,fule]],columns=['name','company','year','kms_driven','fuel_type'])

if st.button('Predict Selling Price'):
    prediction=model.predict(input_df)
    st.success(f"Estimated Selling Price: ₹{round(prediction[0], 2)}")
