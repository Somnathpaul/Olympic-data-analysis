import pandas as pd 
import numpy as np
import streamlit as st 


@st.cache(suppress_st_warning=True)
def preprocess(df, df_1):
    
    # merge two dataset in basis of NOC
    df_15 = df.merge(df_1, on='NOC', how='left')
    df_15 = df_15[df_15['Season'] == 'Summer']
    # remove duplicates values
    df_15 = df_15.drop_duplicates()
    df_15 = df_15[df_15['Season'] == 'Summer']
    
    return df