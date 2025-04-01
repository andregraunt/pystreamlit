import time
import numpy as np
import pandas as pd
import streamlit as st

_LOREM_IPSUM = """
 Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
 incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
 nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
 """


def stream_data():
     for word in _LOREM_IPSUM.split(" "):
         yield word + " "
         time.sleep(0.2)

     yield pd.DataFrame(
         np.random.randn(7, 10),  # (5, 10)
         columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
     )

     for word in _LOREM_IPSUM.split(" "):
         yield word + " "
         time.sleep(0.2)


if st.button("Stream data"):
    #  st.write_stream(stream_data)
    st.write_stream(stream_data)
    
    st.title ("konverter valut")
st.write("perevod lyuboy valyuti v rubli")

x = st.number_input("USD")
st.write(x)
rate = 88.67
st.write () 
     