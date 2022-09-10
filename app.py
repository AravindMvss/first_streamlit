import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit
import streamlit as st
import plotly.express as px

@streamlit.cache
def read_frame():
    df=pd.DataFrame(columns=['first','second'])
    df['first']=[i for i in range(20)]
    df['second']= [i*i for i in range(20)]
    return df

st.title('Displaying data frame')
df=read_frame()
disp=st.sidebar.radio("Select chart type",['with x-axis','default'],index=1)
cols=st.sidebar.selectbox("select columns",["all","first","Second"],index=0)

if cols is "all":
    st.write(df)
if cols is "first":
    st.write(df[['first']])
if cols is "Second":
    st.write(df[['second']])

if disp == 'default':
    fig=px.line(data_frame=df,title="Denemma Graph")
    st.plotly_chart(fig)
if disp == "with x-axis":
    fig = px.line(data_frame=df,x='first',y='second', title="Denemma Graph")
    st.plotly_chart(fig)

lay1,lay2=st.columns(2)

lay1.line_chart(df)
lay1.write("Accuracy: 65")
lay2.line_chart(df)
lay2.write("Accuracy: 65")

