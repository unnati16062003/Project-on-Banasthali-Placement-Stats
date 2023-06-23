import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import cv2
#from  PIL import ImageChops
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px
import io 
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
import helper
import sqlite3 
import datetime
import hashlib
import streamlit.components.v1 as components
import pymongo
import streamlit_authenticator as stauth

import hydralit_components as hc
st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)
menu_data = [
    
    
    {'icon': "	fas fa-user-circle",'label':"Upload Placement Data"},
    
    {'icon': "f	fas fa-chart-line", 'label':"Delete Placement Data"},
    {'icon': "	fas fa-user-circle",'label':"Upload Student Data"},
    {'icon': "	fas fa-user-circle",'label':"Delete Student Data"},
    
    
]
over_theme = {'txc_inactive': 'white','menu_background':'#1c3c84','txc_active':'black','option_active':'white'}


#over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    

    
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='sticky',
)
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]
{
background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHYfmng8EbYWrIULmMrah4_dDoj2rP__numLjd4pVo6HUYhOEtibsYzLLOTDwnCIAkAyA&usqp=CAU");
background-size: 180%;
background-repeat: no-repeat;
background-attachment: local;

</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
if "aut" not in st.session_state:
    st.session_state.aut=False
if __name__== "__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client['admin']
    if menu_id=="Home":
         img = Image.open("grp.png")
         st.image(img, width=200)
         if __name__== "__main__":
            client=pymongo.MongoClient("mongodb://localhost:27017/")
            db=client['admin']
            collection2=db["Details"]
            #st.subheader("Login")
            alldocs=collection2.find()
            names=[]
            passwords=[]
            usernames=[]
            for item in alldocs:
                usernames.append(item["_id"])
                passwords.append(item["Password"])
                names.append(item["Name"])
            hashed_passwords = stauth.Hasher(passwords).generate()
            authenticator = stauth.Authenticate( names,usernames, hashed_passwords,
                "App1", "abcdef1", cookie_expiry_days=30)
            name, authentication_status, username = authenticator.login("Admin Login", "main")
        #st.text(name)
        #st.text(username)
        #st.text(authentication_status)
            if username not in usernames and authentication_status != None:
                st.warning("No such username exists!!")
            else:
                if authentication_status == False:
                    st.session_state.aut=False
                    st.error("Username/password is incorrect")
                elif authentication_status == None:
                    st.session_state.aut=False
            #authentication_status=True
                    st.warning("Please enter your username and password")
                elif authentication_status:
                    st.session_state.aut=True
                    db=client['admin']
                    collection3=db["PlacementStats"]
                    st.subheader(f'Welcome *{name}*')
                    authenticator.logout("Logout","main")
    if menu_id=="Upload Placement Data":
        if st.session_state.aut==True:
            img = Image.open("grp.png")
            st.image(img, width=200)
            collection3=db["PlacementStats"]
            st.title("Choose a placement data file:")
            uploaded_file = st.file_uploader("")
            if uploaded_file is not None:
                dataframe = pd.read_excel(uploaded_file)
                st.table(dataframe)
                dataframe.reset_index(inplace=True)
                data_dict = dataframe.to_dict("records")
                # Insert collection
                collection3.insert_many(data_dict)
                st.success("Placement data uploaded successfully..")
        else:
            st.subheader("Please login first")        
    if menu_id=="Delete Placement Data":
        if st.session_state.aut==True:
            img = Image.open("grp.png")
            st.image(img, width=200)
            collection3=db["PlacementStats"]
            alldata=collection3.find()
            yrs=[]
            for item in alldata:
                if item["Year of placement"] not in yrs:
                    yrs.append(item["Year of placement"])
            #yr = st.text_input('Enter the year whose placement data is to be deleted')
            st.title("Enter the year whose placement data is to be deleted:")
            delete_form = st.form(key='delete_form', clear_on_submit=True)
            yr = delete_form.text_input("")
            #dell=st.button("Submit")
            dell = delete_form.form_submit_button(label='Delete records')
            if dell:
                yrin=int(yr)
                if yrin not in yrs:
                    st.warning("Records of no such year are present!!")
                else:
                    collection3=db["PlacementStats"]
                    rec={"Year of placement":yrin}
                    up=collection3.delete_many(rec)
                    if up.deleted_count >0:
                        st1="Placement data for the year "+yr+" is deleted successfully"
                        st.success(st1)
        else:
            st.subheader("Please login first")                
    if menu_id=="Upload Student Data":
        if st.session_state.aut==True:
            img = Image.open("grp.png")
            st.image(img, width=200)
            st.title("Choose a student data file:")
            uploaded_file = st.file_uploader("")
            if uploaded_file is not None:
                dataframe = pd.read_excel(uploaded_file)
                st.table(dataframe)
                dataframe.reset_index(inplace=True)
                data_dict = dataframe.to_dict("records")
                collection4=db["BanasthaliID"]
                collection4.insert_many(data_dict)
                st.success("Placement data uploaded successfully..")
        else:
            st.subheader("Please login first")        
    if menu_id=="Delete Student Data":
        if st.session_state.aut==True:
            img = Image.open("grp.png")
            st.image(img, width=200)
            collection4=db["BanasthaliID"]
            alldata=collection4.find()
            yrs=[]
            for item in alldata:
                if item["StudentsYear"] not in yrs:
                    yrs.append(item["StudentsYear"])
            #yr = st.text_input('Enter the year whose placement data is to be deleted')
            st.title("Enter the year for which placement has to be deleted:")
            delete_form = st.form(key='delete_form', clear_on_submit=True)
            yr = delete_form.text_input("")
            #dell=st.button("Submit")
            dell = delete_form.form_submit_button(label='Delete records')
            if dell:
                yrin=int(yr)
                if yrin not in yrs:
                    st.warning("Records of no such year are present!!")
                else:
                    collection3=db["BanasthaliID"]
                    rec={"StudentsYear":yrin}
                    up=collection3.delete_many(rec)
                    if up.deleted_count >0:
                        st1="Student data for the year "+yr+" is deleted successfully"
                        st.success(st1)
        else:
            st.subheader("Please login first")                     