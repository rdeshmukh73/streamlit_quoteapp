import requests
import streamlit as st
import json

st.markdown("# Add a New Quote for an existing or new Author")
st.sidebar.header("Add a New Quote for an existing or new Author")
st.write(
    """Add a new Quote for an existing or new Author using this page
    """
)

def validateQuote(newQuote):
    #Implement a profanity check for the Quotes
    if newQuote == "":
        return 'Empty Quote'
    return 'OK'

def addNewQuote(author, newQuote, source, tags, likes):
    #Validate the author
    if author == "":
        st.error("Author should not be Empty")
        return

    status = validateQuote(newQuote)
    if status != 'OK':
        st.error(f'Quote has a problem - {status}')   
        return

    #Form the Quote JSON
    data = {
        'Quote': newQuote,
        'Author': author,
        'Source': source,
        'Tags': tags,
        'Likes': likes
    }
    url = 'http://localhost:5000/addQuote'
    url = "https://rdeshmukh73.pythonanywhere.com/addQuote"
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code != 200:
        st.error(f'Unable to Add New Quote: {response.status_code}')
        return
    return

#Main Logic
isnewAuthor = st.checkbox('Add a New Author')
author = ""
if isnewAuthor:
    author = st.text_input('New Author')
else:
    API_URL = "http://localhost:5000/getAuthorList"
    API_URL = "https://rdeshmukh73.pythonanywhere.com/getAuthorList"
    response = requests.get(API_URL)
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        author = st.selectbox('Select an Author', data)

newQuote = st.text_area("Enter the Quote String")
source = st.text_input("Source of the Quote", value="Internet")
tags = st.text_input("Tags", value="")
likes = st.number_input("Likes", value=0)

st.write("")

btn = st.button("Add Quote", on_click=lambda:addNewQuote(author, newQuote, source, tags, likes))