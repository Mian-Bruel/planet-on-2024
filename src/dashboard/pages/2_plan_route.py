import random
import folium
from streamlit_folium import st_folium
import streamlit as st
import pickle
import networkx as nx

# Starting constants for map center and zoom
# CENTER_START = [52.668528, 16.789972]
ZOOM_START = 13

# Get graph from data
G = pickle.load(open("data/graph.dupa", "rb"))

# Calculate the center of the graph
center_y = sum(n[1] for n in G.nodes) / len(G.nodes)
center_x = sum(n[0] for n in G.nodes) / len(G.nodes)
CENTER_START = [center_y, center_x]


left, right = st.columns([3, 2])
with left:
    # Create the map
    m = folium.Map(location=CENTER_START, zoom_start=ZOOM_START)

    # Add graph nodes and edges to the map
    for node, data in G.nodes(data=True):
        # Extract node coordinates
        if 'y' in data and 'x' in data:
            folium.CircleMarker(
                location=(data['y'], data['x']),
                radius=3,
                color="blue",
                fill=True,
                fill_opacity=0.8,
            ).add_to(m)

    for u, v, edge_data in G.edges(data=True):
        # Extract coordinates for the edge's nodes
        if 'geometry' in edge_data:
            # If the edge has a geometry, use it directly
            folium.PolyLine(
                locations=[(point.y, point.x) for point in edge_data['geometry'].coords],
                color="green",
                weight=2,
                opacity=0.7,
            ).add_to(m)
        else:
            # Otherwise, use the endpoints of the edge
            u_coords = (G.nodes[u]['y'], G.nodes[u]['x'])
            v_coords = (G.nodes[v]['y'], G.nodes[v]['x'])
            folium.PolyLine(
                locations=[u_coords, v_coords],
                color="green",
                weight=2,
                opacity=0.7,
            ).add_to(m)

    # Display the map in the Streamlit app
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
