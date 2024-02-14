import streamlit as st
import pickle as pk
import pandas as pd
import numpy as np
from xgboost import XGBClassifier as XG

pipe = pk.load(open('pipe.pkl','rb'))


home = ['RENT',
'MORTGAGE',
'OWN',
'OTHER']

intent = ['EDUCATION',
'MEDICAL',
'VENTURE',
'PERSONAL',
'DEBTCONSOLIDATION',
'HOMEIMPROVEMENT']

default = ['Yes',
'No']

st.title('Credit Risk Assessment for Loan Approval')

col1, col2 = st.columns(2)

with col1:
    home = st.selectbox('Home',sorted(home))
with col2:
    intent = st.selectbox('Intent', sorted(intent))



col3,col4,col5 = st.columns(3)

with col3:
    age = st.number_input('Age')
with col4:
    amount = st.number_input('Amount Of Loan')
with col5:
    income = st.number_input('Income')



rate = st.number_input('Rate Of Interest')


col7, col8 = st.columns(2)

with col7:
    default = st.selectbox('Default',sorted(default))
    if default=='Yes':
        default = 'Y'
    else:
        default = 'N'
with col8:
    yr_of_emp = st.number_input('Year Of Employeement')

if st.button('Loan Approval'):
    percent_income = round(amount/income,2)

    input_df = pd.DataFrame(
     {'Age':[age], 'Income':[income], 'Home':[home], 'Emp_length':[yr_of_emp], 'Intent':[intent], 'Amount':[amount], 'Rate':[rate], 'Percent_income':[percent_income], 'Default':[default]})
    result = pipe.predict(input_df)
    if str(int(result[0])) == '0':
        st.header("Your Loan Approval Request Has Cancelled")
    else:
        st.header("Your Loan Approval Request Has Accepted")