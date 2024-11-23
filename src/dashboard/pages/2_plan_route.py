import random
import folium
from streamlit_folium import st_folium
import streamlit as st


# Starting constants for map center and zoom
CENTER_START = [52.668528, 16.789972]
ZOOM_START = 13

left, right = st.columns([3, 2])
with left:

    # Create the map
    m = folium.Map(location=CENTER_START, zoom_start=ZOOM_START)

    # Pass session state values to st_folium
    st_folium(
        m,
        key="new",
        height=500,
        width=800,
    )


with right:
    # Sidebar or additional functionality
    st.write("## Route Options")
    st.write("Here you can plan your route in the forest")
    distance = st.slider("Set maximum distance", 0, 100, 1)
    st.write(f"Distance: {distance} km")
