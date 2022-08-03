#streamlit run ui/demo_dataanalytics.py
from sqlalchemy import true
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import dtale as 
@st.cache
def load_dataset():
    df = pd.read_excel('ui/Canada.xlsx',
            sheet_name='Canada by Citizenship',
            skiprows=20,skipfooter=2)
             
    return df

def  preprocess(df):
  
    # step 1:drop columns
    cols_to_drop =['type','converage','area','reg','dev']
    df.drop(columns=cols_to_drop,inplace= True)
  
    #step 2:rename columns
    df.rename({
    'Odname':'country',
    'areaname':'continent',
    'regname':'region',
    'devname':'status'
    },axis=1,inplace=true)
   
    #step3 :col as string
    df.columns =df.columns.astype(str)
   
    # step 4:add a total column
    years =list(map(str,range(1980,2014)))
    df['total']=df[years].sum(axis=1)
   
    #step5: set country as index
    df.set_index('country',inplace= true)
    return df  
    

# loading the data
Canadadf = load_dataset()
if st.checkbox("view raw dataset"):
    st.write(Canadadf)
