import streamlit as st 
st.title("Registration Form")

first, last = st.columns(2)

first.text_input("First Name")
last.text_input("Last Name")

email, mob = st.columns([2,1])
email.text_input("Email")
mob.text_input("Mobile Number")

user, pw, pw2 = st.columns(3)
user.text_input("Username")
pw.text_input("Password", type = "password")
pw2.text_input("Retype password", type = "password")

chck, blnk, sub = st.columns(3)
chck.checkbox("I Agree")
sub.button("Submit")