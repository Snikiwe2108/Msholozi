import streamlit as st 
from streamlit_option_menu import option_menu

st.ste_page_config(page_tittle="Msholozi",page_icon="👑",layout='wide')

st.title('Greatness')

st.sidebar.success('Please choose page above')

st.radio('Please select month here:', options = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Upload", "Tasks", 'Settings'], 
        icons=['house','cloud-upload', "list-task", 'gear'], menu_icon="cast", default_index=1)
    selected

st.write('snikiwe')

st.button('Click Here')
