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
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management

conn = sqlite3.connect('project.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(Username TEXT PRIMARY KEY NOT NULL,Password TEXT NOT NULL,Name TEXT NOT NULL ,Gender TEXT NOT NULL,Date TEXT NOT NULL)')


def add_userdata(Username,Password,Name,Gender,Date):
	c.execute('INSERT INTO userstable(Username,Password,Name,Gender,Date) VALUES (?,?,?,?,?)',(Username,Password,Name,Gender,Date))
	conn.commit()

def login_user(Username,Password):
	c.execute('SELECT * FROM userstable WHERE Username =? AND Password = ?',(Username,Password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def isuser(Username):
	cursor =c.execute("select username from userstable ")
	for entry in cursor:
		if entry==Username:
			return 1
	return 0	



#st.set_page_config(page_title="Sharone's Streamlit App Gallery", page_icon="", layout="wide")

# sysmenu = '''
# <style>
# #MainMenu {visibility:hidden;}
# footer {visibility:hidden;}
# '''
#st.markdown(sysmenu,unsafe_allow_html=True)

#Add a logo (optional) in the sidebar
#logo = Image.open(r'C:\Users\13525\Desktop\Insights_Bees_logo.png')
#profile = Image.open(r'C:\Users\13525\Desktop\medium_profile.png')
url="E:/python files/first.py"

#with st.sidebar:
choose = option_menu(menu_title="PlacementStats Gallery", options=["Home", "Login", "Register", "Admin", "PlacementStats"],
                        icons=['house-door-fill', 'person-circle', 'journal-plus', 'person','graph-up-arrow'],
                        menu_icon="app-indicator", default_index=1,orientation="horizontal",
                        styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
     },
     )


#image = Image.open('bm.jpg')
#st.image(image, width=800 )
if choose==None:
    st.subheader('welcome to placementStats of Banasthali...')
    st.markdown("The Placement Process begins with the extension of the formal invitation from the Industry Interaction Cell (IIC) to the organizations, which in turn share the job description and other details back with the IIC. Nominations from interested students are collected and shared with the organisations. Subsequently, a usual process of campus hiring is followed wherein the shortlisted students undergo the following steps: discussion during pre-hiring talk, test, rounds of interview, offer, acceptance & joining.")
    image = Image.open('gr.webp')
    st.image(image, width=450)
if choose=="PlacementStats":
    df=pd.read_excel("E:\data.xlsx")
    yr=df['Year of placement'].unique().tolist()
    st.sidebar.image('logo.jpg', width=170)
    user_menu=st.sidebar.radio('Select an option',('Overall data preview','Overall analysis','Year-wise analysis','Branch-wise analysis','Company-wise analysis'))
    if user_menu == 'Overall data preview':
        years,company,branch,CTC_range = helper.company_year_branch_ctc(df)
        selected_year = st.sidebar.selectbox("Select Year",years)
        selected_company = st.sidebar.selectbox("Select Company name", company)
        selected_branch = st.sidebar.selectbox("Select Btech branch", branch)
        selected_CTC = st.sidebar.selectbox("Select CTC-range", CTC_range)
        temp_df=helper.show_df(df,selected_year,selected_company,selected_branch,selected_CTC)

        if selected_year == 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            sr1="Overall data of last "+str(len(yr))+' years'
            st.title(sr1)
        if  selected_year == 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            st.title("")
        if  selected_year == 'Overall' and selected_company == 'Overall' and selected_branch !='Overall' and selected_CTC =='Overall':
            st.title("")
        if  selected_year == 'Overall' and selected_company == 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            st.title("")
        if  selected_year == 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            sr4="Data preview of students hired by "+str(selected_company)
            st.title(sr4)
        if  selected_year == 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            st.title("")
        if  selected_year == 'Overall' and selected_company != 'Overall'and selected_branch !='Overall'and selected_CTC =='Overall':
            st.title("") 
        if  selected_year == 'Overall' and selected_company != 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            st.title("")
        if  selected_year != 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            sr3="Data preview of year "+str(selected_year)
            st.title(sr3)
        if  selected_year != 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            sr2="Data preview of year "+str(selected_year)+' with CTC '+str(selected_CTC)
            st.title(sr2) 
        if  (selected_year != 'Overall') and (selected_company == 'Overall') and (selected_branch !='Overall') and (selected_CTC =='Overall'):
            st.title("")
        if  selected_year != 'Overall' and selected_company == 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            sr5="Data preview of students of  "+str(selected_branch)+' branch with CTC '+str(selected_CTC)+ ' for '+str(selected_year)
            st.title(sr5)
        if  selected_year != 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            st.title("")  
        if  selected_year != 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            st.title("")
        if  selected_year != 'Overall' and selected_company != 'Overall' and selected_branch !='Overall' and selected_CTC =='Overall':
            st.title("")
        if  selected_year != 'Overall' and selected_company != 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            st.title("")
        st.table(temp_df)
    if user_menu=="Overall analysis":
        a=df['Name of the company'].unique()
        tot_company=a.size 
        b=df['Total no. of students finally selected'].sum()
        yr=df['Year of placement'].unique().tolist()

        col1,col2=st.columns(2)
        with col1:
            st.header("Companies visited the campus")
            st.title(a.size) 
        with col2:
            str=str(len(yr))
            st.header("Total no. of students placed in last "+str+" years")
            st.title(b) 
        a1=list(df['Year of placement'].unique())        
        l=[]
        for i in a:
            df2=df.loc[df['Year of placement']==i,'Total no. of students finally selected']
            b=list(df2)
            l.append(sum(b))
        fig=plt.bar(a,l,color='maroon',width=0.4) 
    #st.plotly_chart(fig) 
   # st.subheader('Total number of student selected per year')
    #image = Image.open('bar.png')
    #st.image(image, width=750)
if choose=="Login":
    st.subheader("Login Section")
    username = st.sidebar.text_input("User Name")
	password = st.sidebar.text_input("Password",type='password')
	if st.sidebar.checkbox("Login"):
			# if password == '12345':
		#create_usertable()
        hashed_pswd = make_hashes(password)
        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:
            st.success("Logged In as {}".format(username))
            task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
            if task == "Add Post":
                st.subheader("Add Your Post")

			elif task == "Analytics":
                st.subheader("Analytics")
			elif task == "Profiles":
				st.subheader("User Profiles")
				user_result = view_all_users()
				clean_db = pd.DataFrame(user_result,columns=["Username","Password","Name","Gender","Date"])
				st.dataframe(clean_db)
		else:
			st.warning("Incorrect Username/Password")
elif choice == "Register":
	st.subheader("Create New Account")
	new_user = st.text_input("Username")
	new_password = st.text_input("Password",type='password')
	new_name=st.text_input("Name")
	new_gender=st.text_input("Gender")
	new_date=st.date_input("Date of birth",min_value=datetime.date(1950,1,1))

	if st.button("Signup"):
		create_usertable()
		if isuser(new_user):
			st.warning("Username taken")
		else:
			add_userdata(new_user,make_hashes(new_password),new_name,new_gender,new_date)
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")    
               
    
