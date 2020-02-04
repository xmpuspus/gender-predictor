import streamlit as st
import numpy as np
import pandas as pd


months = np.array(['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December'])

melted_data = pd.read_csv('data/melted_table_reference.csv')

age = [18,
 19,
 20,
 21,
 22,
 23,
 24,
 25,
 26,
 27,
 28,
 29,
 30,
 31,
 32,
 33,
 34,
 35,
 36,
 37,
 38,
 39,
 40,
 41,
 42,
 43,
 44,
 45]

st.title('Baby Gender Prediction')
st.write("This web application will try to predict a child's gender based on the mother's age and the expected birth month.")

# Months and Age
month_entry = st.sidebar.selectbox('Expected Birth Month', months)
age_trial = st.sidebar.selectbox("Mother's Age", age)

prediction = melted_data[(melted_data['Month'] == month_entry) & (melted_data['Age'] == int(age_trial))]['Gender'].values[0]

st.subheader('What is the predicted gender?')
if prediction == 'M':
    st.write("The baby's gender is going to be Male.")
elif prediction == 'F':
    st.write("The baby's gender is going to be Female.")

