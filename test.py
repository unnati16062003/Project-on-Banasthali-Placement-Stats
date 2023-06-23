import pandas as pd
import streamlit as st
import pymongo
import plotly.express as px
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client['admin']
collection3=db["PlacementStats"]
df6 = pd.DataFrame(list(collection3.find()))
df6 = df6.drop(['_id'], axis=1)

groupby_year=df6['Total no. of students finally selected'].groupby(df6['Year of placement'])
df7=df6.groupby(['Year of placement']).sum(['Total no. of students finally selected'])
df8=df7.drop('CTC offered(LPA)',axis=1)
df8=df8.drop('index',axis=1)
df9=pd.DataFrame(df8)
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
df10=pd.concat([df1,df2,df3,df4,df5],axis=0)
groupby_year=df10['Total no. of students finally selected'].groupby(df10['Year of placement'])
df11=df10.groupby(['Year of placement']).sum(['Total no. of students finally selected'])
df12=df11.drop('CTC offered(LPA)',axis=1)
df13=pd.DataFrame(df12)    
#fig = px.bar(df13, x=df13.index, y=df13.columns,color=df13.index,color_continuous_scale=['red','yellow','green'])
#fig.show() 
#st.plotly_chart(fig)
print(df9)
print(len(df9.index))
cl=df6['Year of placement'].unique()
print(len(cl))
w=df5
              w=w.dropna()
              groupyr=w['CTC offered(LPA)'].groupby(w['Year of placement'])
              x=w.groupby(['Year of placement']).mean(['CTC offered(LPA)'])
              y=x.drop('Total no. of students finally selected',axis=1)
              z=w.groupby(['Year of placement']).max(['CTC offered(LPA)'])
              y=z.drop('Total no. of students finally selected',axis=1)
              bar_width=0.35
              fig1,ax=plt.subplots()
              bar1=ax.bar(z.index-bar_width/2,z['CTC offered(LPA)'],bar_width,color='pink')
              fig2,ax=plt.subplots()
              bar2=ax.bar(y.index-bar_width/2,y['CTC offered(LPA)'],bar_width,color='purple')
              plt.ylabel('CTC offered(LPA)')
              plt.xlabel('Year of placement')
              st.pyplot(fig1)
              st.pyplot(fig2)