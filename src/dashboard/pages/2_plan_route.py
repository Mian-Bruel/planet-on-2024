import pandas as pd
import numpy as np
import streamlit as st

left, right = st.columns([4, 1])

with left:
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=["lat", "lon"],
    )
    st.map(df)

with right:
    st.write("## Route Options")
    st.write("Here you can plan your route in the forest")
    distance = st.slider("Set maximum distance", 0, 100, 1)
    st.write(f"Distance: {distance} km")
    
