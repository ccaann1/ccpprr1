#X Rays
import os
import streamlit as st
from openai import OpenAI
import requests


st.markdown(
    """
    <style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
    }
    .main .block-container { padding: 0rem; }

    .main .block-container { padding-top: 0rem; }

    .navbar {
        overflow: hidden;
        margin-bottom:20px;
        border-bottom:2px solid #48c6e0;
    }
    .navbar a {
        float: left;
        display: block;
        color: #48c6e0;
        text-align: center;
        padding: 10px 10px;
        text-decoration: none;
    }
    .navbar a:hover {
        color: black;
        border-bottom:1px solid #48c6e0;        
    }
    .navbar .logo {
        float: left;        
    }
    .navbar .menu {
        float: right;
    }
    .navbar .menu .active{color:#0099ff;border-bottom:1px solid #0099ff;}
    .navbar .menu a {
        display: inline-block;
    }
    @media screen and (max-width: 600px) {
        .navbar a {
            float: none;
            display: block;
            text-align: left;
        }
        .navbar .menu {
            float: none;
        }
        .notes h3{font-size:18pt;}
    }
        
    
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown(
    """
    <style>
    header {display: none !important;}
    #MainMenu {display: none !important;}
    footer {display: none !important;}
    footer, .stFooter {display: none !important;}
    div._container_gzau3_1 {display:none !important;}
    div._profileContainer_gzau3_53 {display:none !important;}
    </style>
    """,
    unsafe_allow_html=True
)


hide_streamlit_styles = """
    <style>
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_styles, unsafe_allow_html=True)




st.markdown(
    """
    <script>
    const footer = document.querySelector('footer');
    if (footer) {
        footer.style.display = 'none';
    }
    </script>
    """,
    unsafe_allow_html=True
)

response = requests.get('https://canceproit.pythonanywhere.com/ttthais')
data = response.json()
take_this = data[0]


st.markdown(
    """
    <div class="navbar">
        <div class="logo">
            <img src="https://www.cancepro.com/img/icon/CancePro_Icon.png" alt="Logo" style="height: 60px;">
        </div>
        <div class="menu">
            <a href="https://www.cancepro.com/">Go Home</a>
            <a href="https://canceprochat.streamlit.app/">Ask Me </a>
            <a href="#" class="active">X-Ray Analysis</a>
            <a href="https://canceproresearch.streamlit.app/">Cancer Research</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)



# Show title and description.

st.write(
    "Analyzing X-Rays is no more harder, ARTIFICIAL INTELLIGENCE is coming soon through CancePro to give accurate analysis over your Medical Diagnostics."
)

st.markdown(
    """
    <div class="navbar">
        <img src="https://www.cancepro.com/img/xxrr.png" alt="Process">        
    </div>
    """,
    unsafe_allow_html=True
)


# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# openai_api_key = st.text_input("OpenAI API Key", type="password")
# Setting the API key

# st.write(
#     "Has environment variables been set:",
#     os.environ["OPENAI_API_KEY"] == st.secrets["abcd_keyyy"]
# )
# st.write(st.secrets["abcd_keyyy"])


st.write("We are working on huge data to more accurately find the probability of Cancer chances, keep following our Instagram, LinkedIn channels to stay updated with our X-Ray Diagnostic Product.")



st.markdown(
    """
    <div class="notes">
        <h3>"Expected Launch Date is February 18, 2025."</h3>
    </div>
    """,
    unsafe_allow_html=True

)

st.markdown(
    """
    <style>
        .footer-note{
            float:middle;
            text-align:center;
            display: block;
            color: #48c6e0;
            position:relative;
            bottom:0px;
            text-decoration: none;
        }
        .footer-note a:hover {
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div>
        <!-- Footer Area -->
            <div class="footer-note">
                <p> © Copyright 2024,2025  |  All Rights Reserved by <a href="https://www.cancepro.com/">cancepro.com</a> </p>			
            </div>
        <!--/ End Footer Area -->
    </div>
    """,
    unsafe_allow_html=True
)

