import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

USAJOBS_API_KEY = st.secrets["USAJOBS_API_KEY"]
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]