import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px 
import streamlit as st
def plott():
    df1=pd.read_excel('D:\project/unni1.xlsx')
    df1['Total no. of students finally selected'].astype(int)
    df2=pd.read_excel('D:\project/unnat2(1).xlsx')
    df2['Total no. of students finally selected'].astype(int)
                
    df3=pd.read_excel('D:\project/unnat3(1).xlsx')
    df3['Total no. of students finally selected'].astype(int)
    df4=pd.read_excel('D:\project/unnati4(1).xlsx')
    df4['Total no. of students finally selected'].astype(int)
    df5=pd.read_excel('D:\project/unnati5(1).xlsx')
    df5['Total no. of students finally selected'].astype(int)
    df6=pd.concat([df1,df2,df3,df4,df5],axis=0)
    groupby_year=df6['Total no. of students finally selected'].groupby(df6['Year of placement'])
    df7=df6.groupby(['Year of placement']).sum(['Total no. of students finally selected'])
    df8=df7.drop('CTC offered(LPA)',axis=1)
    df9=pd.DataFrame(df8)
    
    fig = px.bar(df8, x=df8.index, y=df8.columns,color=df8.index,color_continuous_scale=['red','yellow','green']) 
    fig.show()
    st.plotly_chart(fig)
