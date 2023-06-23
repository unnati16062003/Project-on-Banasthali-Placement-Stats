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
from matplotlib import pyplot as plt
import helper
import sqlite3 
import datetime
import hashlib
import streamlit.components.v1 as components
import pymongo
import streamlit_authenticator as stauth
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import hydralit_components as hc
#import plot
import re
from statistics import mean
import predict
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
#with st.sidebar:
st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)
#with hc.HyLoader('Please wait',hc.Loaders.standard_loaders,index=[3]):
 #   time.sleep(3)


# Using "with" notation


# specify the primary menu definition
visited=0
menu_data = [
    
    {'icon':"far fa-address-book",'label':"Register"},
    {'icon': "	fas fa-user-circle",'label':"Login"},

    
    {'icon': "f	fas fa-chart-line", 'label':"View Placement Stats"},
    
    
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
#image = Image.open('bm.jpg')
#st.image(image, width=800 )
if "aut" not in st.session_state:
    st.session_state.aut=False
if __name__== "__main__":
 client=pymongo.MongoClient("mongodb://localhost:27017/")
 if menu_id==None or menu_id=="Home":
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
    with st.sidebar:
      img = Image.open("grp.png")
      st.image(img, width=150)
      components.html("""
      <html>
      <head></head>
      <body style="background: linear-gradient(to bottom, rgba(209, 59, 59, 0.827) 0%, rgba(115, 148, 209, 0.5) 100%);">
      <h1 style="color:#06326e;" >PlacementStats</h1>
      <div><h2>Welcome to Banasthali PlacementStats:<br>
      </h2>
      <h3>you should follow the below steps to completely analyse the site...</h3>
      <ul>
      <li>If you are a new user then Register first.</li>
      <li>If you already a registered user then you need to login to view PlacementStats</li>
      <li>After login you can use different options</li>
      <li>If you want to Add any review so you must enter your Banasthali smart card id if have.</l1>
      </ul>
      </div>
      </body>
      </html>
      
      
      
      
      
      """,height=400)






    components.html('''
  <html>
  <head>

  <style >

  #slider {
    overflow: hidden;
    
    width:500%
    align-items: center;

  }
  #slider figure {
    
      position: relative;
    width: 500%;
    
    margin: 0%;
    left: 0;
    animation: 20s slider infinite;
  }
  #slider figure img {
    
    
      float: left;
    width: 20%;
    
  }
  .abc{
                  height:500px;
                  width: 1256px;
                  background-color:rgba(0,0,0, 0.6530);
                  position:absolute;
                  top:0px;
                  
                  z-index:1;
          }
  .abc h1{

                  font-size: 80px;
                  font-family: 'Showcard Gothic';
                  color:rgb(201, 243, 253);
                  margin-left: 23%;
                  margin-top: 1%;

  }  
  .abc img{
  height:200px;
  width:200px;
  margin-top:5%;
  margin-left:38%;
  }      




  @keyframes slider {
    0% {
      left: 0;
    }
    20% {
      left: 0;
    }
    25% {
      left: -100%;
    }
    45% {
      left: -100%;
    }
    50% {
      left: -200%;
    }
    70% {
      left: -200%;
    }
    75% {
      left: -300%;
    }
    95% {
      left: -300%;
    }
    100% {
      left: -400%;
    }
  }

  </style>
  </head>
  <body>

    <div id="slider">
          <div class="abc">
          <img src="http://localhost:8501/media/465f1d283aae5b8b68ef8a2bab4769a6e1f664aaa142ca58fc814e6a.png" />
          <h1> Placement<b style="color:rgb(158, 255, 155);">Stats</b></h1>
          
          </div>
              <figure>
                  
                  <img src="data:image/jpeg;base64,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" >
                  <img src="https://images.collegedunia.com/public/image/0c4da18ea11febe2b4dbad68e31b748b.jpeg?tr=w-809,h-531,c-force">
                  <img src="https://images.shiksha.com/mediadata/images/1531982986phpEf4bTz.jpeg">
                  <img src="https://www.admissionfever.com/Media/clgimg/gallery/3486_img8185756666876590.jpg">
                  <img src="https://www.admissionfever.com/Media/clgimg/gallery/3486_img8266856589697467.jpg">
                  
        
              </figure>
          
    </div>


  </body>
  </html>



  ''',height=500)

    components.html("""

  <html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
  .big{
  display:flex;
  }
  .card1 {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 35%;
    height:390px;
    display:flex;

    
    background-color: rgb(208, 245, 153);
  }

  .card1:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    background-color: rgb(69, 219, 69);
    color:white;
  }

  .card2 {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 35%;
    display:flex;

    
    background-color:rgb(252, 250, 145);
  }

  .card2:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    background-color: orange;
    color:white;
  }
  .card3 {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 35%;
    display:flex;

    
    background-color: rgb(208, 245, 153);
  }

  .card3:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    background-color: rgb(69, 219, 69);
    color:white;
  }

  .card4 {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 35%;
    display:flex;

    
    background-color:rgb(252, 250, 145) ;
  }

  .card4:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    background-color: orange;
    color:white;
  }

  .container1 {
    padding: 2px 16px;
  }
  .container2 {
    padding: 2px 16px;
  }
  .container3 {
    padding: 2px 16px;
  }
  .container4 {
    padding: 2px 16px;
  }
  span >img{
  width:90px;
  height:90px;
  margin-left:90px;
  margin-top:40px;
  }
  h2 {
  margin-left:50px;
  }
  </style>
  </head>
  <body>
  <div class="big">
  <div class="card1">
    
    <div class="container1">
    <span><img src="https://cdn-icons-png.flaticon.com/512/1995/1995539.png" ></span>
      <h2><b>Certified Teachers</b></h2> 
      <p>Banasthali Vidyapeeth  has faculties in various fields such as Arts, Science, Management, Education, Design, Law, and more. The faculty members at Banasthali Vidyapeeth are experienced and knowledgeable in their respective fields and provide quality education to the students.</p> 
    </div>
    </div>
    <div class="card2">
    <div class="container2">
    <span><img src="https://cdn-icons-png.flaticon.com/512/4366/4366867.png" ></span>
      <h2><b>Special Education</b></h2> 
      <p>Banasthali Vidyapeeth follows a well-structured education system that emphasizes both theoretical and practical learning. The university offers undergraduate and postgraduate, programs in various disciplines and has a rigorous curriculum that prepares students for their professional careers and  focuses on character-building  in the students.</p> 
    </div>
    </div>
    <div class="card3">
    <div class="container3">
    <span><img src="https://cdn-icons-png.flaticon.com/512/2232/2232688.png" ></span>
      <h2><b>Book & Library</b></h2> 
      <p>Banasthali Vidyapeeth has a well-equipped library with a vast collection of books, journals, and other resources in various disciplines. The library has a peaceful and conducive environment for reading and research. The university also provides online access to various e-resources and databases for the convenience of the students and faculty.</p> 
    </div>
    </div>
    <div class="card4">
    <div class="container4">
    <span><img src="https://cdn-icons-png.flaticon.com/512/7870/7870706.png" ></span>
      <h2><b>Placements </b></h2> 
      <p>Banasthali Vidyapeeth has a dedicated placement cell that works towards providing career guidance and job opportunities to its students. The university has a good track record of placing its students in reputed organizations across various sectors. Many top companies such as Infosys, Wipro, TCS, Amazon, and more visit the campus for recruitment.</p> 
    </div>
  </div>
  </div>
  </body>
  </html> 



  """,height=400)

    components.html("""

  <html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
  * {
    box-sizing: border-box;
  }

  /* Create three equal columns that floats next to each other */
  .column {
    float: left;
    width: 33.33%;
    padding: 30px;
    height: 300px; /* Should be removed. Only for demonstration */
  }

  /* Clear floats after the columns */
  .row:after {
    content: "";
    display: table;
    clear: both;
  }
  span > img{
  width:60px;
  height:60px;

  }
  p{
  font-size:20px;
  color:#585858;
  }
  h3{
  font-size:25px;
  }
  </style>
  </head>
  <body>

  <br><br><br>
  <div id="offer"><h1>What We offer</h1></div>
  <p>Banasthali Vidyapeeth offers undergraduate, postgraduate, and doctoral programs in various fields such as arts, science, commerce, engineering, management, and education, along with a strong emphasis on women's education and empowerment.</p>
  <br>
  <br>
  <br>




  <div class="row">
    
    
    
    <div class="column" >
      <h3><span><img src="https://cdn-icons-png.flaticon.com/128/2433/2433596.png"</span>safety first</h3>
      <p>Banasthali Vidyapeeth is an all-girls university and takes the safety and security of its female students very seriously. The campus is equipped with 24/7 security personnel, CCTV surveillance, and strict entry protocols to ensure the safety and well-being of all students. </p>
    
    <h3><span><img src="https://cdn-icons-png.flaticon.com/512/3108/3108243.png"</span>Regular Classes</h3>
    <p>Banasthali Vidyapeeth follows a rigorous academic schedule, with regular classes held throughout the week. The university emphasizes a hands-on approach to learning and encourages active student participation in class discussions and practical activities.</p>

    <h3><span><img src="https://cdn-icons-png.flaticon.com/512/4628/4628680.png"</span>Certified Teachers</h3>
    <p>Banasthali Vidyapeeth has a highly qualified and experienced faculty, who are dedicated to providing quality education to their students. The university encourages a student-centric approach to teaching, with faculty members regularly engaging with students both inside and outside the classroom.</p>









  </div>


    <div class="column" >
      
      <h3><span><img src="https://cdn-icons-png.flaticon.com/512/1043/1043730.png"</span>Creative Lessons</h3>
      <p>Banasthali Vidyapeeth places a strong emphasis on creative and innovative teaching methods, with faculty members utilizing various techniques such as role-plays, simulations, case studies, and group projects to make their lessons engaging and interactive. </p>
      <h3><span><img src="https://cdn-icons-png.flaticon.com/128/3492/3492098.png"</span>Sufficient Classrooms</h3>
      <p>Banasthali Vidyapeeth classrooms are equipped with modern teaching aids and technology to facilitate a holistic learning experience for students. The classrooms are designed to provide a comfortable and conducive environment for effective learning and intellectual growth</p>
      <h3><span><img src="https://cdn-icons-png.flaticon.com/512/404/404621.png"</span>Placements</h3>
      <p>Banasthali Vidyapeeth has a dedicated placement cell that works tirelessly to ensure that its B.Tech students get placed in top companies like Amazon, Microsoft, IBM, TCS, Wipro, Infosys, etc., with an average package ranging from 4 to 6 LPA, and the highest package offered is around 18 LPA. The university also provides internships and training programs to prepare their students for the industry and make them employable.</p>
    </div>
    <div class="column" >
      <img src="https://images.livemint.com/rf/Image-621x414/LiveMint/Period2/2018/03/10/Photos/Processed/womenpilots-k0S--621x414@LiveMint.jpg"  height="270px",width="50px">
      <img src="https://d.newsweek.com/en/full/326811/banasthali-vidyapith.jpg?w=790&f=1be3211569697c8d07a693b42205131d"  height="170px",width="50px">
      <img src="https://d.newsweek.com/en/full/325736/banasthali-vidyapith.jpg?w=1600&h=1200&q=88&f=f0460eebf3fe43becd1a3ec987ae34c2" height="300px",width="50px" >
      
    </div>
  </div>


  </body>
  </html>



  """,height=1250)













    components.html("""
  <html>
  <head>
  <style>
  .adi1{
                  height:100%;
                  width: 102%;
                  background-color:rgba(255, 132, 132, 0.3);
                  position:absolute;
                  top:40%;
                  left:76%;
                  z-index:1;
                  
              }


              
              
  #contact{
                  position:absolute;
                  top:30px;
                  left:30px;
                  font-size: 13px;
                  color: white;
              }
              #contact:hover{
              color: black;
              
              }
              #contact font{
              color: rgb(34, 173, 127);
              font-size:24px;
              font-family:Cooper Black;
              margin-left:37px;
              }

              .adi{
                  height:500px;
                  width: 397px;
                  background-color:rgba(162, 49, 49, 0.988);
                  position:absolute;
                  bottom:100%;
                  right:70%;
                  
                  z-index:1;
              }
              .adi > p{
                  color: white;
                  position:absolute;
                  top:210px;
                  left:40px;
                  right:90px;
                  z-index:2;
                  font-size:30px;
                  
              }
              .b3{
                  position:absolute;
                  top:400px;
                  left: 90px;
                  height:50px;
                  width:150px;
                  background-color:rgb(197, 101, 117);
                  color:white;
                  border-color:rgb(65, 5, 15);
              }
            .b3 {
    cursor: pointer;
    border-radius: 15px;
    color: white;
    background-color: rgb(228, 141, 156);
    box-shadow: 0 2px rgb(224, 198, 202) ;
  }

  .b3:hover {background-color: white;
  color:rgba(162, 49, 49, 0.988);}

  .b3:active {
    background-color: rgb(228, 141, 156);
    box-shadow: 0 5px rgb(224, 198, 202);
    transform: translateY(4px);
    }
    .place{
    display:flex;
    }

  .place {
    position: relative;
  }
      .place::before{
          content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 75.5%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(209, 59, 59, 0.827) 0%, rgba(115, 148, 209, 0.8) 100%);
    z-index: 1;
      }     
      

  .iss{

  z-index:3;
  right:899px;
  top:55px;
  position:absolute;
  }
  p{
  left:460px;
  float:right;
  padding:20px;
  z-index:8;
  position:absolute;
  top:5px;

  font-size:20px;
  color:white;

  }
  h2{
  bottom:458px;
  left:500px;
  position:absolute;
  font-size:28px;
  color:white;


  }

              
  </style>
  </head>
  <body>
  <br>
  <br>
  <br>

  <br>
  <div class="place">

  <img src="https://images.shiksha.com/mediadata/images/articles/1673260344phpi84lFN.jpeg"  height="549px" >
  <div class="iss" >

  <img src=" data:image/png;base64,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"  height="470px" >
  <h2 style="width:80%;">Banasthali Placements</h2>
  <br><br>
  <p style="width:100%;"><b>Banasthali Vidyapeeth has a dedicated placement cell that assists students in securing job opportunities in various reputed organizations. Over the years, the university has maintained an impressive placement record, with students getting placed in top companies across diverse sectors such as IT, finance, healthcare, and education. Some of the companies that have recruited students from Banasthali Vidyapeeth include Infosys, TCS, Wipro, Accenture, Deloitte, IBM, Capgemini, HDFC Bank, ICICI Bank, Cognizant, and many more.</b> </p>
  </div>

  <div class="adi1">
              <p id="contact"><font>CONTACT US</font><br><br>
              <b>Banasthali Vidyapith<br><br>
              Admission Enquiry:- <br><br>
              Phone:</b> 01438-228384, 228990<br>
              <b>Mobile: </b>+91- 93528 79844, 93528 79855<br><br>
              <b>E-Mail:<br>
              Higher Education:</b>- admissions@banasthali.in<br>
              <b>School Education:-</b><br>
              (a) For IX & XI :-       shardamandir@banasthali.in<br>
              (b) For VI :-            saraswatimandir@banasthali.in  <br>


              <b>Toll Free No:</b> 1800-270-5855<br><br>

              <b>Postal Address:</b><br>

              Banasthali Vidyapith,<br>
              P.O. Banasthali Vidyapith-304022 (Rajasthan)</p>

  <div class="cont2">
                  <div class="adi">
                      <p>"  Education is not merely for career but for life .  "
                      </p><br><br>
                     

                  </div>
              </div>            
          </div>
  </div>

          <body>
          </html>
  """, height=700,width=1310)


    components.html("""
  <html>
  <head>

  </head>
  <body>

  <div class="a" style="display:flex;" >
  <span><img src="https://cdn-icons-png.flaticon.com/512/1484/1484615.png" height=100px; ></span>
  <h1 style="color: #06326e; font-size:70px;">What Students Say......</h1>
  </div>
  </body>
  </html>




  """)




    components.html("""


  <!DOCTYPE html>
  <html lang="en">
  <!--divinectorweb.com-->
  <head>
      <meta charset="UTF-8">
      <title>Responsive Testimonial Slider</title>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.2.1/assets/owl.carousel.min.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.2.1/assets/owl.theme.default.min.css">
      <style>
  body {
    background-image:url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHYfmng8EbYWrIULmMrah4_dDoj2rP__numLjd4pVo6HUYhOEtibsYzLLOTDwnCIAkAyA&usqp=CAU");
      
      
  }
  #testimonial_area {
    padding: 0% 0% 0% 0%;
  }
  .box-area {
    padding: 30px;
    position: relative;
    display: block;
    background: #fff;
    color: #000;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
    margin: 40px 0;
  }
  .box-area h5 {
    font-size: 16px;
    font-weight: 700;
    color: #0a69ed;
    margin-top: 30px;
    margin-bottom: 5px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  .box-area span {
    color: #262626;
    display: block;
    font-size: 13px;
    margin: 0 0 10px;
    font-weight: 400;
  }
  .box-area .content {
    color: #262626;
  }
  .box-area .img-area {
    width: 90px;
    height: 90px;
    position: absolute;
    top: -40px;
    left: 0;
    bottom: 0;
    margin: 0 auto;
    right: 0;
    z-index: 1;
    border: 5px solid #fff;
    border-radius: 50%;
    box-shadow: 0 5px 4px rgba(0, 0, 0, 0.5);
  }
  .box-area .img-area img {
    width: 100%;
    height: auto;
    border-radius: 50%;
  }
  .socials {
    margin-top: 30px;
  }
  .socials i {
    margin: 0 10px;
    color: #0a69ed;
    font-size: 18px;
  }
  #testimonial_area .owl-nav {
    position: absolute;
    top: 50%;
    width: 100%;
  }
  #testimonial_area .owl-prev, #testimonial_area .owl-next {
    width: 40px;
    height: 40px;
    line-height: 40px;
    color: #0a69ed;
    border-radius: 50%;
    text-align: center;
    background: #fff;
    position: absolute;
  }
  #testimonial_area .owl-prev {
    left: -60px;
    top: -30px;
  }
  #testimonial_area .owl-next {
    right: -60px;
    top: -30px;
  }




      </style>
  </head>
  <body>

      
        <section id="testimonial_area" class="section_padding">
          <div class="container" id="review">
            <div class="row">
              <div class="col-md-12">
                <div class="testmonial_slider_area text-center owl-carousel">
                  <div class="box-area">	
                    <div class="img-area">
                      <img src="https://cdn-icons-png.flaticon.com/128/6997/6997662.png" alt="">
                    </div>	
                    <h5>Simran</h5>
                    <span><b>(Btech IT 3rd year)</b></span>									
                    <p class="content">
                    Banasthali Vidyapith has a good placement record with companies like TCS, Infosys, Wipro, Accenture, and IBM visiting the campus for recruitment.
                    </p>
                    <h6 class="socials">
                        
                        <i class="fa fa-linkedin"></i>
                        
                    </h6>
                  </div> 
                
                  <div class="box-area">	
                    <div class="img-area">
                      <img src="https://cdn-icons-png.flaticon.com/512/6833/6833605.png" alt="">
                    </div>	
                    <h5>Anushka</h5>
                    <span><b>(Btech CS 3rd year)</b></span>									
                    <p class="content">
                      Banasthali Vidyapith has a dedicated placement cell that works towards providing placement opportunities to its students. The college has tie-ups with various companies from different sectors, including IT, Finance, Marketing, and more.
                    </p>
                    <h6 class="socials">
                        
                        <i class="fa fa-linkedin"></i>
                      
                    </h6>
                  </div> 
                
                  <div class="box-area">	
                    <div class="img-area">
                      <img src="https://cdn-icons-png.flaticon.com/512/4721/4721796.png" alt="">
                    </div>	
                    <h5>Rachna</h5>
                    <span><b>(Btech IT 3rd year)</b></span>									
                    <p class="content">
                      Overall, Banasthali Vidyapith has a good placement record, and students are provided with ample opportunities to kickstart their careers.
                    </p>
                    <h6 class="socials">
                        
                        <i class="fa fa-linkedin"></i>
                        
                    </h6>
                  </div> 
                
                  <div class="box-area">	
                    <div class="img-area">
                      <img src="https://cdn-icons-png.flaticon.com/512/4139/4139967.png" alt="">
                    </div>	
                    <h5>Unnati</h5>
                    <span><b>(Btech CS 3rd year)</b></span>									
                    <p class="content">
                      The college also offers internship opportunities to its students, which helps them gain practical experience and exposure to the industry. 
                    </p>
                    <h6 class="socials">
                      
                        <i class="fa fa-linkedin"></i>
                        
                    </h6>
                  </div> 
                
                  <div class="box-area">	
                    <div class="img-area">
                      <img src="https://cdn-icons-png.flaticon.com/512/6833/6833605.png" alt="">
                    </div>	
                    <h5>Shelly</h5>
                    <span><b>(Btech IT 3rd year)</b></span>									
                    <p class="content">
                      The average salary package offered to the students is around 4-5 lakhs per annum, with some students getting offers as high as 10-12 lakhs per annum. 
                    </p>
                    <h6 class="socials">
                        
                        <i class="fa fa-linkedin"></i>
                        
                    </h6>
                  </div> 
                
                  <div class="box-area">	
                    <div class="img-area">
                      <img src="https://cdn-icons-png.flaticon.com/512/2922/2922565.png" alt="">
                    </div>	
                    <h5>Priyangana</h5>
                    <span><b>(Btech CS 3rd year)</b></span>									
                    <p class="content">
                      Banasthali Vidyapith has a dedicated placement cell that works towards providing placement opportunities to its students. The college has tie-ups with various companies from different sectors, including IT, Finance, Marketing, and more.
                    </p>
                    <h6 class="socials">
                        
                        <i class="fa fa-linkedin"></i>
                        
                    </h6>
                  </div> 
                                  <div class="box-area">	
                    <div class="img-area">
                      <img src="https://cdn-icons-png.flaticon.com/128/2922/2922561.png" alt="">
                    </div>	
                    <h5>shreya</h5>
                    <span><b>(Btech IT 3rd year)</b></span>									
                    <p class="content">
                      Banasthali Vidyapith has a good placement record with companies like TCS, Infosys, Wipro, Accenture, and IBM visiting the campus for recruitment.
                    </p>
                    <h6 class="socials">
                        
                        <i class="fa fa-linkedin"></i>
                        
                    </h6>
                  </div> 




                </div>
              </div>
            </div>
          </div>
        </section>
      
      
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.2.1/owl.carousel.min.js"></script>
      <script>
          $(".testmonial_slider_area").owlCarousel({
          autoplay: true,
          slideSpeed:1000,
          items : 3,
          loop: true,
          nav:true,
          navText:['<i class="fa fa-arrow-left"></i>','<i class="fa fa-arrow-right"></i>'],
          margin: 30,
          dots: true,
          responsive:{
            320:{
              items:1
            },
            767:{
              items:2
            },
            600:{
              items:2
            },
            1000:{
              items:3
            }
          }
          
        });
      </script>
  </body>
  </html>






  """,height=350)









    components.html("""
  <html>
      <head>
          <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

          <style>
  body {
    padding: 0;
    
    min-height: 100vh;
    display: flex;
    align-items: flex-end;
  }
  footer {
    background-color: black;
    color: white;
    bottom: 80%;
    width: 100vw;
    font-size: 16px;
  }
  footer * {
    box-sizing: border-box;
    border: none;
    outline: none;
  }
  .row {
    padding: 1em 1em;
  }
  .row.primary {
    display: grid;
    grid-template-columns: 3fr 2fr 4fr;
    align-items: stretch;
    
  }
  .column {
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: 0 2em;
    min-height: 15em;
  }
  h3 {
    width: 100%;
    text-align: left;
    color: white;
    font-size: 1.4em;
    white-space: nowrap;
  }
  ul {
    list-style: none;
    display: flex;
    flex-direction: column;
    padding: 0;
    margin: 0;
  }
  li:not(:first-child) {
    margin-top: 0.8em;
  }
  ul li a {
    color: #a7a7a7;
    text-decoration: none;
  }
  ul li a:hover {
    color: #c7940a;
  }
  .about p {
    text-align: justify;
    line-height: 2;
    margin: 0;
  }
  input,
  button {
    font-size: 1em;
    padding: 1em;
    width: 100%;
    border-radius: 5px;
    margin-bottom: 5px;
  }
  .submit {
    background-color: #c7940a;
    color: #ffffff;
  }
  div.social {
    display: flex;
    justify-content: space-around;
    font-size: 2.4em;
    flex-direction: row;
    margin-top: 0.5em;
  }
  .social i {
    color: #bac6d9;
  }
  .copyright {
    padding: 0.3em 1em;
    background-color: #25262e;
  }
  .footer-menu{
    float: left;
      margin-top: 10px;
  }
  .footer-menu a{
    color: #cfd2d6;
    padding: 6px;
    text-decoration: none;
  }
  .footer-menu a:hover, .social i:hover{
    color: #c7940a;
  }
  .copyright p {
    font-size: 0.9em;
    text-align: right;
  }
  @media screen and (max-width: 850px) {
    .row.primary {
      grid-template-columns: 1fr;
    }
  }




          </style>
      </head>
      <body>

          <footer>

              <div class="row primary">
                  <div class="column about">
                      <h3>Follow us:</h3>
                      
                      <div class="social" id="rww">
                          <i class="fa fa-facebook-square"></i>
                          <i class="fa fa-twitter-square"></i>
                          <i class="fa fa-linkedin-square"></i>
                          <i class="fa fa-instagram"></i>
                      </div>
                  </div>
              
                  <div class="column link">
                      <h3>Links</h3>
                      <ul>
                          <li><a href="#slider">Home</a></li>
                          <li><a href="#offer">what we offer</a></li>
                          <li><a href="#review">Reviews</a></li>
                          <li><a href="#rww">Support</a></li>
                      </ul>
                  </div>
              
                  <div class="column subscribe">
                      <h3>Ask query</h3>
                      <div>
                          <input type="text" placeholder="Your name" />
                          <input type="email" placeholder="Your email id here" />
                          <br>
                          <textarea placeholder="enter query"></textarea>
                          <br>
                          <button class="submit">Submit </button>
                        
                      </div>
                  </div>
                  
              </div>
              <div class="row copyright">
                  <div class="footer-menu">
                
                  <a href="">Home</a>
                  <a href="">F.A.Q</a>
                  <a href="">Cookies Policy</a>
                  <a href="">Terms Of Service</a>
                  <a href="">Support</a>
                
                  </div>
                  <p>Copyright &copy; 2022</p>
                </div>
                

              
          </footer>
          




      </body>
  </html>




  """,height=500)








    
    


 if menu_id=="View Placement Stats":
  if st.session_state.aut==True:
    st.subheader(f'Welcome *{st.session_state.nm}*')
        #authenticator.logout("Logout","sidebar")
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
    db=client['admin']
    collection3=db["PlacementStats"]
    df = pd.DataFrame(list(collection3.find()))
    df = df.drop(['_id'], axis=1)
  
    #df=pd.read_excel("E:\data.xlsx")

    yr=df['Year of placement'].unique().tolist()
    with st.sidebar:
        img = Image.open("grp.png")
        st.image(img, width=200)
    user_menu=st.sidebar.radio('Select an option',('Overall data preview','Overall analysis','Year-wise visualization','Branch-wise visualization','Add reviews','View Reviews and Public sentiment','Predict Placement Stats'))
    years,company,branch,CTC_range = helper.company_year_branch_ctc(df)
    if user_menu == 'Overall data preview':
        
        selected_year = st.sidebar.selectbox("Select Year",years)
        selected_company = st.sidebar.selectbox("Select Company name", company)
        selected_branch = st.sidebar.selectbox("Select Btech branch", branch)
        selected_CTC = st.sidebar.selectbox("Select CTC-range", CTC_range)
        temp_df=helper.show_df(df,selected_year,selected_company,selected_branch,selected_CTC)
        if selected_year == 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            sr1="Overall data of "+str(len(yr))+' years'
            st.title(sr1)
        if selected_year == 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            st.title("")
        if selected_year == 'Overall' and selected_company == 'Overall' and selected_branch !='Overall' and selected_CTC =='Overall':
            st.title("")
        if selected_year == 'Overall' and selected_company == 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            st.title("")
        if selected_year == 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            sr4="Data preview of students hired by "+str(selected_company)
            st.title(sr4)
        if selected_year == 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            st.title("")
        if selected_year == 'Overall' and selected_company != 'Overall'and selected_branch !='Overall'and selected_CTC =='Overall':
            st.title("") 
        if selected_year == 'Overall' and selected_company != 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            st.title("")
        if selected_year != 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            sr3="Data preview of year "+str(selected_year)
            st.title(sr3)
        if selected_year != 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            sr2="Data preview of year "+str(selected_year)+' with CTC '+str(selected_CTC)
            st.title(sr2) 
        if (selected_year != 'Overall') and (selected_company == 'Overall') and (selected_branch !='Overall') and (selected_CTC =='Overall'):
            st.title("")
        if selected_year != 'Overall' and selected_company == 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            sr5="Data preview of students of  "+str(selected_branch)+' branch with CTC '+str(selected_CTC)+ ' for '+str(selected_year)
            st.title(sr5)
        if selected_year != 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            st.title("")  
        if selected_year != 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            st.title("")
        if selected_year != 'Overall' and selected_company != 'Overall' and selected_branch !='Overall' and selected_CTC =='Overall':
            st.title("")
        if selected_year != 'Overall' and selected_company != 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            st.title("")
        temp_df=temp_df.drop('index',axis=1)    
        st.table(temp_df)
    if user_menu=="Overall analysis":
        a=df['Name of the company'].unique()
        tot_company=a.size
        #df['Total no. of students finally selected'].astype(int)
        b=df['Total no. of students finally selected'].sum()
        yr=df['Year of placement'].unique().tolist()
        db=client['admin']
        collection3=db["PlacementStats"]
        df = pd.DataFrame(list(collection3.find()))
        df5 = df.drop(['_id'], axis=1)
        v=df5["CTC offered(LPA)"]
        f=v.apply (pd.to_numeric,errors='coerce')
        v=v.dropna()
        average=mean(v)
        average=round(average,3)
        maximum=max(v)
        lowest=min(v)
        col1,col2=st.columns(2)
        with col1:
            st.header("Companies visited the campus")
            st.title(a.size)
            st.header("Mean CTC offered in "+str(len(yr))+" Years")
            st.title(average)
            st.header("Highest CTC offered in "+str(len(yr))+" Years")
            st.title(maximum)
        with col2:
            stre=str(len(yr))
            st.header("Total no. of students placed in last "+stre+" years")
            st.title(b)
            st.header("Lowest CTC offered in "+str(len(yr))+" Years")
        st.title(lowest)
        dictionary={}
        if 'Tata Consultancy Services' not in dictionary:
            dictionary['Tata Consultancy Services']=0
            for i in df5['Name of the company']:
                if i.startswith('Tata'):
                    dictionary['Tata Consultancy Services']+=1
                else:
                    if i not in dictionary:
                        dictionary[i]=1
                    else:
                        dictionary[i]+=1    
        l=[]
        for j in dictionary:
            if dictionary[j]>=5*len(yr):
                l.append(j)
        st.header("Frequent recruiters:")
        for k in l:
            st.subheader(k)                          
                         

    if user_menu=='Year-wise visualization':
        #st.subheader("Hello")
        db=client['admin']
        collection3=db["PlacementStats"]
        df6 = pd.DataFrame(list(collection3.find()))
        df6 = df6.drop(['_id'], axis=1)
        groupby_year=df6['Total no. of students finally selected'].groupby(df6['Year of placement'])
        df7=df6.groupby(['Year of placement']).sum(['Total no. of students finally selected'])
        df8=df7.drop('CTC offered(LPA)',axis=1)
        df8=df8.drop('index',axis=1)
        df9=pd.DataFrame(df8)
        fig = px.bar(df9, x=df9.index, y='Total no. of students finally selected',color='Total no. of students finally selected',color_continuous_scale=['red','yellow','green'])
        st.header("Total number of students placed per year") 
        st.plotly_chart(fig)
        fig2 = px.pie(df9, values='Total no. of students finally selected', names=df9.index)
        st.header("Share of each year in total number of students placed in "+str(len(df9.index))+" years")
        st.plotly_chart(fig2)
        w=df6
        w=w.dropna()
        groupyr=w['CTC offered(LPA)'].groupby(w['Year of placement'])
        x=w.groupby(['Year of placement']).mean(['CTC offered(LPA)'])
        y=x.drop('Total no. of students finally selected',axis=1)
        y=y.reset_index()
        fig3=px.scatter(y,x="Year of placement",y="CTC offered(LPA)")
        st.header("Mean salary offered per year")
        st.plotly_chart(fig3)
        z=w.groupby(['Year of placement']).max(['CTC offered(LPA)'])
        a=z.drop('Total no. of students finally selected',axis=1)
        a=a.reset_index()
        fig4=px.scatter(a,x="Year of placement",y="CTC offered(LPA)")
        st.header("Highest salary offered per year")
        st.plotly_chart(fig4)
        df14=df6.groupby(['Year of placement','Branch']).sum("Total no. of students finally selected")
        df14=df14.drop(['CTC offered(LPA)'],axis=1)
        df14 = df14.reset_index()
        fig5=px.scatter(df14,x="Year of placement",y="Total no. of students finally selected")
        st.subheader("Yearwise,branchwise,Total number of students selected")
        st.plotly_chart(fig5)
    if user_menu=='Branch-wise visualization':
        db=client['admin']
        collection3=db["PlacementStats"]
        df6 = pd.DataFrame(list(collection3.find()))
        df6 = df6.drop(['_id'], axis=1)
        groupby_branch=df6['Total no. of students finally selected'].groupby(df6['Branch'])
        df7=df6.groupby(['Branch']).sum(['Total no. of students finally selected'])
        df8=df7.drop('CTC offered(LPA)',axis=1)
        df8=df8.drop('Year of placement',axis=1)
        #df8=df8.drop('CS ',axis=0)
        df8=df8.drop('index',axis=1)
        df9=pd.DataFrame(df8)
        fig = px.bar(df9, x=df9.index, y='Total no. of students finally selected',color='Total no. of students finally selected',color_continuous_scale=['red','yellow','green'])
        st.header("Total number of students placed per year") 
        st.plotly_chart(fig)
        fig2 = px.pie(df9, values='Total no. of students finally selected', names=df9.index)
        st.header("Share of each year in total number of students placed in "+str(len(df9.index))+" branches")
        st.plotly_chart(fig2)
        df14=df6.groupby(['Year of placement','Branch']).sum("Total no. of students finally selected")
        df14=df14.drop(['CTC offered(LPA)'],axis=1)
        df14 = df14.reset_index()
        fig5=px.scatter(df14,x="Branch",y="Total no. of students finally selected")
        st.subheader("Branchwise,yearwise,Total number of students selected")
        st.plotly_chart(fig5)       
    if user_menu=="Add reviews":
        collection4=db["BanasthaliID"]
        text_input_value = st.session_state.get('text_input_value', '')
        review_form = st.form(key='review_form', clear_on_submit=False)
        banasthalite =review_form.text_input("Enter Banasthali ID",value=text_input_value)
        #check = review_form.form_submit_button(label='Submit')
        st.session_state['text_input_value'] = banasthalite
        allIDs=collection4.find()
        ID=[]
        for data in allIDs:
            ID.append(data["_id"])
        if "buttonclicked" not in st.session_state:
            st.session_state.buttonclicked=False
        def callback():
            st.session_state.buttonclicked=True
                      #st.session_state.il=banasthalite
        if (review_form.form_submit_button("Submit",on_click=callback) or st.session_state.buttonclicked):
                  #st.write(st.session_state.il)
                  #st.session_state["Submit"]=True
            if banasthalite in ID:
                collection5=db["Review"]
                student=collection4.find({"_id":banasthalite})
                for s in student:
                        statement=s["Name"]
                        statement1=s["StudentsYear"]
                        intst=str(statement1)
                        statement2=s["Btech Branch"]
                st.success("Verified as a student of Banasthali")
                st.subheader("Add review as "+statement)
                st.subheader("Year :"+intst)
                st.subheader("Btech Branch \:"+statement2)
                txt=st.text_area("Write your review")
                if "buttonclicked1" not in st.session_state:
                    st.session_state.buttonclicked1=False
                def callback1():
                    st.session_state.buttonclicked1=True
                    st.session_state.il=banasthalite
                if (st.button("Add review") or st.session_state.buttonclicked1):
                        #st.write(st.session_state.il)
                    reviewer={"Name":statement,"Year":statement1,"Btech Branch":statement2,"Review":txt}
                        #reviewer=list(reviewer)
                    collection5.insert_one(reviewer)
                    st.success("Review recorded successfully")
            else:
                st.error("Not a student of Banasthali")
    if user_menu=="View Reviews and Public sentiment":
          def get_sentiment_score(text):
              sia=SentimentIntensityAnalyzer()
              sentiment=sia.polarity_scores(text)
              return sentiment['compound']
                      
              
          collection5=db["Review"]
          alldocs=collection5.find()
          tot_score=0
          count=0
          po_count=0
          for s in alldocs:
              count=count+1
              statement3=s['Review']
              score=get_sentiment_score(statement3)
              tot_score=tot_score+score
              if(score>0):
                  po_count=po_count+1
          tot_score=tot_score/count
          po_percent=(po_count/count)*100
          po_percent=round(po_percent,3)
          po_percent=str(po_percent)
          with open('projectstyle.css') as f:
                st.markdown(f'<style>{f.read()}<style>',unsafe_allow_html=True)    
                if tot_score>0:
                  st.title("Overall public sentiment for Banasthali is POSITIVE..")
                  st.title("About "+po_percent+"\% of reviewers liked the Banasthali university")
                elif tot_score<0:
                  st.write("Overall public sentiment for Banasthali is NEGATIVE..")
                  st.write("About "+po_percent+"\% of reviewers liked the Banasthali university")
                else:
                  st.header("Overall public sentiment for Banasthali is NEUTRAL..")
                  st.header("About "+po_percent+"\% of reviewers liked the Banasthali university") 
          alldocs1=collection5.find()
          with open('projectstyle.css') as f:
            for s1 in alldocs1:
                st.markdown(f'<style>{f.read()}<style>',unsafe_allow_html=True)
                statement=s1["Name"]
                statement1=str(s1["Year"])
                statement2=s1["Btech Branch"]
                statement3=s1['Review']
                score=get_sentiment_score(statement3)
                st.subheader("  ")
                st.subheader("Review by "+ "  " +statement)
                if statement1=='1':
                    st.subheader("Course \:"+" " +"Btech"+"  " +statement2 +"  "+statement1+"rd year")
                if statement1=='2':
                    st.subheader("Course \:"+" " +"Btech"+"  " +statement2 +"  "+statement1+"nd year") 
                if statement1=='3':
                    st.subheader("Course \:"+" " +"Btech"+"  " +statement2 +"  "+statement1+"rd year")
                if statement1=='4':
                    st.subheader("Course \:"+" " +"Btech"+"  " +statement2 +"  "+statement1+"th year")           
                if score>0:
                    st.title(" :blue[Student Review] \:"+statement3)
                elif score<0:
                    st.write(" :blue[Student Review] \:"+statement3)
                else:
                    st.header(" :blue[Student Review] \:"+statement3) 
    if user_menu=="Predict Placement Stats":
          be=['CS','IT','EC','EE','BT','CE']
          st.header("Want to predict placements in banasthali in future...? ")
          yop=st.text_input("Enter year of Placement for which you want to predict:") 
          br = st.selectbox("Enter Btech Branch for which ypu want predict placements", be)  
          sub=st.button("Predict placements !!")  
          if sub:
             yopint=int(yop)
             sta=predict.predictt(yopint,br,predict.X)
             ans="As predicted,Total number of students of Btech branch : "+br+" ,placed in Banasthali in year "+yop+" could be around : "+str(sta)  
             st.subheader(ans)                      
  else:
    page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]
{
background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHYfmng8EbYWrIULmMrah4_dDoj2rP__numLjd4pVo6HUYhOEtibsYzLLOTDwnCIAkAyA&usqp=CAU");
background-size: 180%;
background-repeat: no-repeat;
background-attachment: local;

</style>'''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    db=client['admin']
    collection=db["userDetails"]
#st.subheader("Login")
    alldocs=collection.find()
    names=[]
    passwords=[]
    usernames=[]
    for item in alldocs:  
        usernames.append(item["_id"])
        passwords.append(item["Password"])
        names.append(item["Name"])
    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate( names,usernames, hashed_passwords,"App", "abcdef", cookie_expiry_days=30)
    name, authentication_status, username = authenticator.login("Please Login first...", "main")
#st.text(name)
#st.text(username)
#st.text(authentication_status)
    if username not in usernames and authentication_status != None:
      st.warning("No such username exists!!")
    else:
      if authentication_status == False:
        st.error("Username/password is incorrect")
      elif authentication_status == None:
        st.session_state.clear()
    #authentication_status=True
        st.warning("Please enter your username and password")
      elif authentication_status:
        st.subheader(f'Welcome *{name}*')
        authenticator.logout("Logout","sidebar")
        db=client['admin']
        collection3=db["PlacementStats"]
        df = pd.DataFrame(list(collection3.find()))
        df = df.drop(['_id'], axis=1)
  
    #df=pd.read_excel("E:\data.xlsx")

        yr=df['Year of placement'].unique().tolist()
        with st.sidebar:
          img = Image.open("grp.png")
          st.image(img, width=200)
        user_menu=st.sidebar.radio('Select an option',('Overall data preview','Overall analysis','Year-wise visualization','Branch-wise visualization','Add reviews','View Reviews and Public sentiment','Predict Placement Stats'))
        years,company,branch,CTC_range = helper.company_year_branch_ctc(df)
        if user_menu == 'Overall data preview':
          
          selected_year = st.sidebar.selectbox("Select Year",years)
          selected_company = st.sidebar.selectbox("Select Company name", company)
          selected_branch = st.sidebar.selectbox("Select Btech branch", branch)
          selected_CTC = st.sidebar.selectbox("Select CTC-range", CTC_range)
          temp_df=helper.show_df(df,selected_year,selected_company,selected_branch,selected_CTC)
          if selected_year == 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            sr1="Overall data of last "+str(len(yr))+' years'
            st.title(sr1)
          if selected_year == 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            st.title("")
          if selected_year == 'Overall' and selected_company == 'Overall' and selected_branch !='Overall' and selected_CTC =='Overall':
            st.title("")
          if selected_year == 'Overall' and selected_company == 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            st.title("")
          if selected_year == 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            sr4="Data preview of students hired by "+str(selected_company)
            st.title(sr4)
          if selected_year == 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            st.title("")
          if selected_year == 'Overall' and selected_company != 'Overall'and selected_branch !='Overall'and selected_CTC =='Overall':
            st.title("") 
          if selected_year == 'Overall' and selected_company != 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            st.title("")
          if selected_year != 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            sr3="Data preview of year "+str(selected_year)
            st.title(sr3)
          if selected_year != 'Overall' and selected_company == 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            sr2="Data preview of year "+str(selected_year)+' with CTC '+str(selected_CTC)
            st.title(sr2) 
          if (selected_year != 'Overall') and (selected_company == 'Overall') and (selected_branch !='Overall') and (selected_CTC =='Overall'):
            st.title("")
          if selected_year != 'Overall' and selected_company == 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            sr5="Data preview of students of  "+str(selected_branch)+' branch with CTC '+str(selected_CTC)+ ' for '+str(selected_year)
            st.title(sr5)
          if selected_year != 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC =='Overall':
            st.title("")  
          if selected_year != 'Overall' and selected_company != 'Overall' and selected_branch =='Overall' and selected_CTC !='Overall':
            st.title("")
          if selected_year != 'Overall' and selected_company != 'Overall' and selected_branch !='Overall' and selected_CTC =='Overall':
            st.title("")
          if selected_year != 'Overall' and selected_company != 'Overall' and selected_branch !='Overall' and selected_CTC !='Overall':
            st.title("")
          st.table(temp_df)
        if user_menu=="Overall analysis":
          a=df['Name of the company'].unique()
          tot_company=a.size 
          b=df['Total no. of students finally selected'].sum()
          yr=df['Year of placement'].unique().tolist()
          db=client['admin']
          collection3=db["PlacementStats"]
          df = pd.DataFrame(list(collection3.find()))
          df5 = df.drop(['_id'], axis=1)
          v=df5["CTC offered(LPA)"]
          f=v.apply (pd.to_numeric,errors='coerce')
          v=v.dropna()
          average=mean(v)
          average=round(average,3)
          maximum=max(v)
          lowest=min(v)
          col1,col2=st.columns(2)
          with col1:
            st.header("Companies visited the campus")
            st.title(a.size)
            st.header("Mean CTC offered in "+str(len(yr))+" Years")
            st.title(average)
            st.header("Highest CTC offered in "+str(len(yr))+" Years")
            st.title(maximum)
          with col2:
            stre=str(len(yr))
            st.header("Total no. of students placed in last "+stre+" years")
            st.title(b)
            st.header("Lowest CTC offered in "+str(len(yr))+" Years")
            st.title(lowest)
          dictionary={}
          if 'Tata Consultancy Services' not in dictionary:
            dictionary['Tata Consultancy Services']=0
          for i in df5['Name of the company']:
            if i.startswith('Tata'):
              dictionary['Tata Consultancy Services']+=1
            else:
              if i not in dictionary:
                dictionary[i]=1
              else:
                dictionary[i]+=1    
          l=[]
          for j in dictionary:
            if dictionary[j]>=5*len(yr):
              l.append(j)
          st.header("Frequent recruiters:")
          for k in l:
            st.subheader(k)
        if user_menu=='Year-wise visualization':
          db=client['admin']
          collection3=db["PlacementStats"]
          df6 = pd.DataFrame(list(collection3.find()))
          df6 = df6.drop(['_id'], axis=1)
          groupby_year=df6['Total no. of students finally selected'].groupby(df6['Year of placement'])
          df7=df6.groupby(['Year of placement']).sum(['Total no. of students finally selected'])
          df8=df7.drop('CTC offered(LPA)',axis=1)
          df8=df8.drop('index',axis=1)
          df9=pd.DataFrame(df8)
          fig = px.bar(df9, x=df9.index, y='Total no. of students finally selected',color='Total no. of students finally selected',color_continuous_scale=['red','yellow','green'])
          st.header("Total number of students placed per year") 
          st.plotly_chart(fig)
          fig2 = px.pie(df9, values='Total no. of students finally selected', names=df9.index)
          st.header("Share of each year in total number of students placed in "+str(len(df9.index))+" years")
          st.plotly_chart(fig2)
          w=df6
          w=w.dropna()
          groupyr=w['CTC offered(LPA)'].groupby(w['Year of placement'])
          x=w.groupby(['Year of placement']).mean(['CTC offered(LPA)'])
          y=x.drop('Total no. of students finally selected',axis=1)
          y=y.reset_index()
          fig3=px.scatter(y,x="Year of placement",y="CTC offered(LPA)")
          st.header("Mean salary offered per year")
          st.plotly_chart(fig3)
          z=w.groupby(['Year of placement']).max(['CTC offered(LPA)'])
          a=z.drop('Total no. of students finally selected',axis=1)
          a=a.reset_index()
          fig4=px.scatter(a,x="Year of placement",y="CTC offered(LPA)")
          st.header("Highest salary offered per year")
          st.plotly_chart(fig4)
          df14=df6.groupby(['Year of placement','Branch']).sum("Total no. of students finally selected")
          df14=df14.drop(['CTC offered(LPA)'],axis=1)
          df14 = df14.reset_index()
          fig5=px.scatter(df14,x="Year of placement",y="Total no. of students finally selected")
          st.subheader("Yearwise,branchwise,Total number of students selected")
          st.plotly_chart(fig5)
        if user_menu=='Branch-wise visualization':
          db=client['admin']
          collection3=db["PlacementStats"]
          df6 = pd.DataFrame(list(collection3.find()))
          df6 = df6.drop(['_id'], axis=1)
          groupby_branch=df6['Total no. of students finally selected'].groupby(df6['Branch'])
          df7=df6.groupby(['Branch']).sum(['Total no. of students finally selected'])
          df8=df7.drop('CTC offered(LPA)',axis=1)
          df8=df8.drop('Year of placement',axis=1)
         # df8=df8.drop('CS ',axis=0)
          df8=df8.drop('index',axis=1)
          df9=pd.DataFrame(df8)
          fig = px.bar(df9, x=df9.index, y='Total no. of students finally selected',color='Total no. of students finally selected',color_continuous_scale=['red','yellow','green'])
          st.header("Total number of students placed per year") 
          st.plotly_chart(fig)
          fig2 = px.pie(df9, values='Total no. of students finally selected', names=df9.index)
          st.header("Share of each year in total number of students placed in "+str(len(df9.index))+" branches")
          st.plotly_chart(fig2)
          df14=df6.groupby(['Year of placement','Branch']).sum("Total no. of students finally selected")
          df14=df14.drop(['CTC offered(LPA)'],axis=1)
          df14 = df14.reset_index()
          fig5=px.scatter(df14,x="Branch",y="Total no. of students finally selected")
          st.subheader("Branchwise,yearwise,Total number of students selected")
          st.plotly_chart(fig5)
  
        if user_menu=="Add reviews":
          collection4=db["BanasthaliID"]
            
          text_input_value = st.session_state.get('text_input_value', '')
          review_form = st.form(key='review_form', clear_on_submit=False)
          banasthalite =review_form.text_input("Enter Banasthali ID",value=text_input_value)
          #check = review_form.form_submit_button(label='Submit')
          st.session_state['text_input_value'] = banasthalite
          allIDs=collection4.find()
          ID=[]
          for data in allIDs:
            ID.append(data["_id"])
          if "buttonclicked" not in st.session_state:
            st.session_state.buttonclicked=False
          def callback():
            st.session_state.buttonclicked=True
                  #st.session_state.il=banasthalite
          if (review_form.form_submit_button("Submit",on_click=callback) or st.session_state.buttonclicked):
              #st.write(st.session_state.il)
              #st.session_state["Submit"]=True
            if banasthalite in ID:
              collection5=db["Review"]
              student=collection4.find({"_id":banasthalite})
              for s in student:
                statement=s["Name"]
                statement1=s["StudentsYear"]
                intst=str(statement1)
                statement2=s["Btech Branch"]
              st.success("Verified as a student of Banasthali")
              st.subheader("Add review as "+statement)
              st.subheader("Year :"+intst)
              st.subheader("Btech Branch \:"+statement2)
              txt=st.text_area("Write your review")
              if "buttonclicked1" not in st.session_state:
                st.session_state.buttonclicked1=False
              def callback1():
                st.session_state.buttonclicked1=True
                st.session_state.il=banasthalite
              if (st.button("Add review") or st.session_state.buttonclicked1):
                #st.write(st.session_state.il)
                reviewer={"Name":statement,"Year":statement1,"Btech Branch":statement2,"Review":txt}
                #reviewer=list(reviewer)
                collection5.insert_one(reviewer)
                st.success("Review recorded successfully")
            else:
              st.error("Not a student of Banasthali") 
        if user_menu=="View Reviews and Public sentiment":
          def get_sentiment_score(text):
            sia=SentimentIntensityAnalyzer()
            sentiment=sia.polarity_scores(text)
            return sentiment['compound']
                    
              
          collection5=db["Review"]
          alldocs=collection5.find()
          tot_score=0
          count=0
          po_count=0
          for s in alldocs:
            count=count+1
            statement3=s['Review']
            score=get_sentiment_score(statement3)
            tot_score=tot_score+score
            if(score>0):
              po_count=po_count+1
          tot_score=tot_score/count
          po_percent=(po_count/count)*100
          po_percent=round(po_percent,3)
          po_percent=str(po_percent)
          with open('projectstyle.css') as f:
            st.markdown(f'<style>{f.read()}<style>',unsafe_allow_html=True)    
            if tot_score>0:
              st.title("Overall public sentiment for Banasthali is POSITIVE..")
              st.title("About "+po_percent+"\% of reviewers liked the Banasthali university")
            elif tot_score<0:
              st.write("Overall public sentiment for Banasthali is NEGATIVE..")
              st.write("About "+po_percent+"\% of reviewers liked the Banasthali university")
            else:
              st.header("Overall public sentiment for Banasthali is NEUTRAL..")
              st.header("About "+po_percent+"\% of reviewers liked the Banasthali university") 
          alldocs1=collection5.find()
          with open('projectstyle.css') as f:
            st.markdown(f'<style>{f.read()}<style>',unsafe_allow_html=True)
            for s1 in alldocs1:
              statement=s1["Name"]
              statement1=str(s1["Year"])
              statement2=s1["Btech Branch"]
              statement3=s1['Review']
              score=get_sentiment_score(statement3)
              st.subheader("  ")
              st.subheader("Review by "+ "  " +statement)
              if statement1=='1':
                st.subheader("Course \:"+" " +"Btech"+"  " +statement2 +"  "+statement1+"st year")
              if statement1=='2':
                st.subheader("Course \:"+" " +"Btech"+"  " +statement2 +"  "+statement1+"nd year")
              if statement1=='3':
                st.subheader("Course \:"+" " +"Btech"+"  " +statement2 +"  "+statement1+"rd year")
              if statement1=='4':
                st.subheader("Course \:"+" " +"Btech"+"  " +statement2 +"  "+statement1+"th year")            
              if score>0:
                st.title(" :blue[Student Review] \:"+statement3)
              elif score<0:
                st.write(" :blue[Student Review] \:"+statement3)
              else:
                st.header(" :blue[Student Review] \:"+statement3)
        if user_menu=="Predict Placement Stats":
          be=['CS','IT','EC','EE','BT','CE']
          st.header("Want to predict placements in banasthali in future...? ")
          yop=st.text_input("Enter year of Placement for which you want to predict:") 
          br = st.selectbox("Enter Btech Branch for which ypu want predict placements", be)  
          sub=st.button("Predict placements !!")  
          if sub:
             yopint=int(yop)
             sta=predict.predictt(yopint,br,predict.X)
             ans="As predicted,Total number of students of Btech branch : "+br+" ,placed in Banasthali in year "+yop+" could be around : "+str(sta)  
             st.subheader(ans)                                       
 if menu_id=="Login":
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
    db=client['admin']
    collection=db["userDetails"]
    #st.subheader("Login")
    alldocs=collection.find()
    names=[]
    passwords=[]
    usernames=[]
    for item in alldocs:  
        usernames.append(item["_id"])
        passwords.append(item["Password"])
        names.append(item["Name"])
        hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate( names,usernames, hashed_passwords,
        "App", "abcdef", cookie_expiry_days=30)
    name, authentication_status, username = authenticator.login("Login", "main")
    #st.text(name)
    #st.text(username)
    #st.text(authentication_status)
    if username not in usernames and authentication_status != None:
        st.warning("No such username exists!!")
    else:
        if authentication_status == False:
            st.error("Username/password is incorrect")
        elif authentication_status == None:
            st.session_state.clear()
        #authentication_status=True
            st.warning("Please enter your username and password")
        elif authentication_status:
            st.session_state.aut=True
            if "nm" not in st.session_state:
              st.session_state.nm=name
            st.subheader(f'Welcome *{name}*')
            st.success("You have  successfully logged in...")
            st.title("You can now view Placement Stats..")
            authenticator.logout("Logout","main")
            
                
                #st.session_state.il=banasthalite
 if menu_id == "Register":

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
    if st.session_state.aut==True:
        st.header("You are already logged in")
    else:
            
      db=client['admin']
      collection1=db["userDetails"]
      st.subheader("Create New Account")   
      signup_form = st.form(key='signup_form', clear_on_submit=True)
      new_user = signup_form.text_input("Username")
      new_password = signup_form.text_input("Password",type='password')
      #passlist=list(new_password)
      #hashed_password_list = stauth.Hasher(passlist).generate()
      #hashed_password=hashed_password_list 
      new_name=signup_form.text_input("Name")
      new_gender=signup_form.radio("Gender",("Male","Female","Other"),horizontal=True)
      new_date=signup_form.date_input("Date of birth",min_value=datetime.date(1950,1,1))
      new_date=str(new_date)
      #signup = signup_form.form_submit_button(label='Sign Up', on_click=isuser,args=(new_user,))
      signup = signup_form.form_submit_button(label='Sign Up')
      if signup:
          flag=0
          for character in new_user:
              if character.isdigit():
                  flag=1
                  break
          if new_user=="" or new_password=="" or new_name=="" or new_gender=="" or new_date=="":
              st.warning("Fill out all fields")
          elif(len(new_user)<5 or len(new_user)>8):
              st.warning("Length of username must have 5 to 8 characters")
          elif not new_user[0].isalpha():
              st.warning("Username must start with an alphabet")
          elif flag==0:
              st.warning("Username must contain atleast one digit")
          elif len(new_password)<5 or len(new_password)>8:
              st.warning("Password must contain 5 to 8 characters")       
          else:
              allID1=collection1.find({"_id":new_user},{"_id":1})
              ID=[]
              for i in allID1:
                  for j in i.values():
                      ID.append(j)
              if (new_user in ID):
                  st.warning("Username already taken")
              else:
                  user={"_id":new_user,"Password":new_password,"Name":new_name,"Gender":new_gender,"Date of birth":new_date}
                  collection1.insert_one(user)
                  #add_userdata(new_user,make_hashes(new_password),new_name,new_gender,new_date)
                  st.success("You have successfully created a valid Account")
                  st.info("Go to Login Menu to login")
 


                        
                        


                        

