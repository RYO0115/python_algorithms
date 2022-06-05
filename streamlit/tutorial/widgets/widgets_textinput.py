import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    chart_data

st.text_input("Your name", key="name")

st.session_state.name