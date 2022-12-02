
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

with st.sidebar:
         selected = option_menu("Main Menu", ["Home", "Upload", "Tasks", 'Settings'],icons=['house','cloud-upload', "list-task", 'gear'], menu_icon="cast", default_index=1)
         selected
st.radio('Please select month here:', options = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec'])
st.button('click here')
