import streamlit as st
import pandas as pd
import numpy as np 
import time

a = [1,2,3,4,5,6]
n = np.array(a)
nd = n.reshape(2,3)

dic = {
    1 : "abcd",
    2 : "qwert",
    3 : "sfsdv"
}

data = pd.read_csv("data\Salary_Data.csv")
print(data)

st.dataframe(data, height=500, width=500)
st.table(nd)
st.table(data)
st.json(dic)
st.write(data)

@st.cache_data
def return_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(return_time(1))
if st.checkbox("2"):
    st.write(return_time(2))

