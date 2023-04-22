import streamlit as st
import requests

st.set_page_config(
    page_title="Quote App - By Raghavendra Deshmukh",
    page_icon="👋",
)

st.write("# Welcome to the QuoteApp! 👋")

st.sidebar.success("Select an action above")

st.markdown(
    """
    My name is Raghavendra Deshmukh - a Software Rookie who is trying to learn a few new things about building software.
    
    I live in :blue[Bangalore, India].  I am enthusiastic about Indian Music, Cricket, Software, Leadership, People development and Blockchain.

    I have been motivated by a lot of good Quotes that are available via various sources.
    I am building this app to load Quotes and make them available for consumption. 
    ### What can we do with this App
    - Get a Random Quote
    - Add a New Quote
    - Get a Quote for a Chosen Author
    """
)
st.write("")

url = 'http://localhost:5000/getBasicDetails'
url = 'https://rdeshmukh73.pythonanywhere.com/getBasicDetails'
response = requests.get(url)
if response.status_code != 200:
    st.error("Unable to load Basic details")
else:
    data = response.json()
    totalQuotes = data['TotalQuotes']    
    totalAuthors = data['UniqueAuthors']
    printStr = f"Total Quotes: {totalQuotes} and Unique Authors: {totalAuthors} in the Quote Database"
    custom_style = """
        <style>
        .custom {
        color: blue;
        font-size: 20px;
        font-weight: bold;
        border: 1px solid black;
        padding: 10px
    }
    </style>
    """
    my_string = printStr
    styled_string = f'<span class="custom">{my_string}</span>'
    st.markdown(custom_style + styled_string, unsafe_allow_html=True)   