
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu
import pip
pip.main(["install", "openpyxl"])


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
st.title('Greatness')

@st.cache
def get_data_from_excel():
         df =  pd.read_excel('supermarkt_sales.xlsx',engine="openpyxl",sheet_name="Sales",skiprows=3,usecols="B:R",nrows=1000)
         df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
         return df

df = get_data_from_excel()

with st.sidebar:
         selected = option_menu("Main Menu", ["Home", "Upload", "Tasks", 'Settings'],icons=['house','cloud-upload', "list-task", 'gear'], menu_icon="cast", default_index=1)
         selected
         
# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type ==@customer_type & Gender == @gender"
)
   
st.radio('Please select month here:', options = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec'],horizontal=True)
st.write(df)
st.button('click here')
