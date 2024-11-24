import random
import folium
from streamlit_folium import st_folium
import streamlit as st
import pickle
from src.dashboard.pathfinder.Pathfinder import PathFinder
from src.dashboard.pathfinder.utils import get_info, get_paths_distance

st.set_page_config(
    layout="wide",
)

if "path" not in st.session_state:
    st.session_state["path"] = None

ZOOM_START = 12

# Get graph from data
G = pickle.load(open("data/graph-old.pkl", "rb"))

points, connections, distances = get_info(G, "olddie_but_goldie")

# Calculate the center of the graph
center_y = sum(n[1] for n in G.nodes) / len(G.nodes)
center_x = sum(n[0] for n in G.nodes) / len(G.nodes)
CENTER_START = [center_y, center_x]


left, right = st.columns([4, 2])
with left:
    # Create the map
    m = folium.Map(location=CENTER_START, zoom_start=ZOOM_START)

    if st.session_state["path"]:
        coords = []
        for i in range(len(st.session_state["path"])):
            u = st.session_state["path"][i]
            coords.append([list(G.nodes)[u][1], list(G.nodes)[u][0]])

        fg = folium.FeatureGroup("Lines")
        folium.PolyLine(coords).add_to(fg)
        m.add_child(fg)

    # Display the map in the Streamlit app
    st_folium(
        m,
        key="new",
        height=700,
        width=800,
    )

with right:
    # Sidebar or additional functionality
    st.write("## Route Options")
    st.write("Here you can plan your route in the forest")
    distance = st.slider("Set maximum distance (km)", 0, 20, 2)
    if st.button("Find Route"):
        start_index = random.randint(0, len(points) - 1)
        pathfinder = PathFinder(points, connections, distances, target=distance * 1000, s=start_index, precision=500)
        path = pathfinder.get_closest_path()
        st.session_state["path"] = path
        st.rerun()

    if st.session_state["path"] is not None:
        distance = get_paths_distance(st.session_state["path"], distances)
        st.write(f"""
                 Found a great match for your route!
                 The total distance is {distance / 1000:.2f} km.
                 """)
