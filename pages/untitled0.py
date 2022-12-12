# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:14:18 2022

@author: User
"""

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
from streamlit_option_menu import option_menu
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

df = pd.read_csv("https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv")


st.write(df)


# Fill NAs with 0s and create GDP per capita column
df = df.fillna(0)
df['gdp_per_capita'] = np.where(df['population']!= 0, df['gdp']/ df['population'], 0)

year_slider = st.slider('Year slider', min_value=1750, max_value=2020, step=5, value=1850)

yaxis_co2 = st.radio('Y axis', options=['co2', 'co2_per_capita',],horizontal=True)

continents = ['World', 'Asia', 'Oceania', 'Europe', 'Africa', 'North America', 'South America', 'Antarctica']

co2_pipeline = (df[(df.year <= year_slider) & (df.country.isin(continents))].groupby(['country', 'year'])[yaxis_co2].mean()
    .to_frame()
    .reset_index()
    .sort_values(by='year')  
    .reset_index(drop=True)
)

dt.write(co2_pipeline)

