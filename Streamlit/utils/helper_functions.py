# GLOBAL INPORTS
import joblib,os
import streamlit as st
import pandas as pd
from pathlib import Path
#from config  import INPUT_PATH, MODELS_PATH, PAGES_PATH

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
