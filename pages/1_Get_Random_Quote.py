import requests
import streamlit as st


st.markdown("# Get a Random Quote")
st.sidebar.header("Random Quote")
st.write(
    """This page shows a Random Quote from a randomly picked Author.  We can also post the Quote to LinkedIn!"""
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


# Call the API and get the response
# Define the API endpoint URL
API_URL = "http://localhost:5000/getRandomQuote"
API_URL = "https://rdeshmukh73.pythonanywhere.com/getRandomQuote"
response = requests.get(API_URL)
# Check if the response is successful
custom_style = """
        <style>
        .custom {
        color: blue;
        font-size: 20px;
        font-weight: bold;
        }
        </style>
    """
if response.status_code == 200:
    # Display the API response in a multiline text box
    st.subheader("Random Quote")
    data = response.json()
    author = data['Author']
    quoteText = data['Quote']
    finalQuote = quoteText + "\n by:  " + author
    styled_string = f'<span class="custom">{finalQuote}</span>'
    st.markdown(custom_style + styled_string, unsafe_allow_html=True)   
    #st.markdown(f"<div style='border: 1px solid black; padding: 10px'>{finalQuote}</div>", unsafe_allow_html=True)

else:
    st.error("Failed to fetch data from API")

st.write("")
st.write("")
col1, col2 = st.columns(2)
btn1 = col1.button("Get a Random Quote")
#btn2 = col2.button("Post to LinkedIn", on_click=postToLinkedIn)

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

