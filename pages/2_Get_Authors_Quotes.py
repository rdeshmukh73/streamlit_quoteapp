import requests
import streamlit as st


st.markdown("# List Authors and get their Quotes")
st.sidebar.header("Get Authors and their Quotes")
st.write(
    """This page shows a list of Authors.  Choose an Author to View a Random Quote by them
    """
)
finalQuote = ""

def postToLinkedIn():
    st.write(finalQuote)
    url = 'http://localhost:5000/postQuoteToLinkedIn'
    url = "https://rdeshmukh73.pythonanywhere.com/postQuoteToLinkedIn"
    textToPost = finalQuote + "\n\nvia QuoteApp by Raghavendra"
    response = requests.post(url, data=textToPost)
    if response.status_code != 200:
        st.error("Error posting to LinkedIn")
    else:
        st.success("Posted to LinkedIn")    


custom_style = """
        <style>
        .custom {
        color: blue;
        font-size: 20px;
        font-weight: bold;
        }
        </style>
    """

# Call the API and get the response
# Define the API endpoint URL
API_URL = "http://localhost:5000/getAuthorList"
API_URL = "https://rdeshmukh73.pythonanywhere.com/getAuthorList"
response = requests.get(API_URL)
# Check if the response is successful
if response.status_code == 200:
    # Display the API response in a multiline text box
    st.subheader("Author List")
    data = response.json()
    authorSelected = st.selectbox('Select an Author', data)

    #url = 'http://localhost:5000/getRandomQuoteForAuthor/' + authorSelected
    url = "https://rdeshmukh73.pythonanywhere.com/getRandomQuoteForAuthor/" + authorSelected
    response = requests.get(url)  
    if response.status_code == 200:
        data = response.json()
        #author = data['Author']
        quoteText = data['Quote']
        finalQuote =  "**:blue["+ quoteText + " -by: " + authorSelected + "]**"
        st.markdown(finalQuote)
        
        #styled_string = f'<span class="custom">{finalQuote}</span>'

        #st.markdown("This text is :pink[colored pink], and this is **:violet[purple-colored]** and bold.")

        #st.markdown(custom_style + styled_string, unsafe_allow_html=True)   
        #st.markdown(f"<div style='border: 1px solid black; padding: 10px'>{finalQuote}</div>", unsafe_allow_html=True)
    else:
        st.error('API Get Quote for Author fails')    

else:
    st.error("API Get Author List fails")

st.write("")
st.write("")
col1, col2 = st.columns(2)
#btn2 = col1.button("Post to LinkedIn", on_click=postToLinkedIn)

text = textToPost = finalQuote + "\n\nvia QuoteApp by Raghavendra"
components.html(
    f"""
        <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" 
        data-text="{text}"
        data-url=" "
        data-show-count="false">
        data-size="Large" 
        data-hashtags="streamlit,python"
        Tweet
        </a>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    """
)

