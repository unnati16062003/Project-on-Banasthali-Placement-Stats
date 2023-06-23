import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pymongo
import streamlit as st
df1=pd.read_excel("D:/projectff/unni1.xlsx")
df2=pd.read_excel("D:/projectff/unnat2(1).xlsx")
df3=pd.read_excel("D:/projectff/unnat3(1).xlsx")
df4=pd.read_excel("D:/projectff/unnati4(1).xlsx")
df5=pd.read_excel("D:/projectff/unnati5(1).xlsx")
df6 = pd.concat([df1, df2, df3,df4,df5], axis=0)
df8=df6.groupby(['Year of placement','Branch']).sum("Total no. of students finally selected")
df8=df8.drop(['CTC offered(LPA)'],axis=1)
df8 = df8.reset_index()
df8=df8[df8['Year of placement'] != 2022]
X = pd.get_dummies(df8[["Year of placement", "Branch"]])
y = df8["Total no. of students finally selected"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=68)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2=r2_score(y_test,y_pred)

def predictt(yop,br,X):
    new_data = pd.DataFrame({"Year of placement": [yop], "Branch": [br]})
    new_data = pd.get_dummies(new_data,)
    X = X.append(new_data, ignore_index=True)
    X = X.fillna(0)
    res=X.tail(1)
    X=X.drop(40)
    new_y = model.predict(res)
    print(new_y)
    print(X)
    return round(new_y[0])

