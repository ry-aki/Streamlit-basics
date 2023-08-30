import streamlit as st 
st.title("WIDGETS")

if st.button("Subcribe"):
    st.write("Subscribed!!")

name = st.text_input("Name")
st.write(name)

address = st.text_area("Address")
st.write(address)

date = st.date_input("Enter date")
time = st.time_input("Enter time")

if st.checkbox("Accept the terms", value = False):
    st.write("THANK YOU!!")


st.radio("Colours", ['r','b','g'], index = 0)
st.selectbox("Colours", ['r','b','g'], index = 0)

st.multiselect("Colours", ['r','b','g'])
st.slider("age", min_value = 18, max_value = 60, value = 30, step = 5)
st.number_input("age", min_value = 18, max_value = 60, value = 30, step = 5)
st.file_uploader("Upload a file")