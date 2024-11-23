import pandas as pd
import numpy as np
import streamlit as st

left, right = st.columns([4, 1])

with left:
    df = pd.DataFrame(
        np.random.randn(20, 2) / [100, 100] + [52.668528, 16.789972],
        columns=["lat", "lon"],
    )
    st.map(df)

with right:
    st.write("## Route Options")
    st.write("Here you can plan your route in the forest")
    distance = st.slider("Set maximum distance", 0, 100, 1)
    st.write(f"Distance: {distance} km")
