import math

import numpy as np
import streamlit as st

def get_paths_distance(p, d):
    dis = 0

    for point in range(len(p) - 1):
        dis += d[p[point]][p[point + 1]]

    return dis

# get_paths_distance(path, distances)
def get_distance(p1, p2):
    r = 6371e3
    phi_1 = p1[1] * math.pi / 180
    phi_2 = p2[1] * math.pi / 180
    delta_phi = (p1[1] - p2[1]) * math.pi / 180
    delta_lambda = (p2[0] - p1[0]) * math.pi / 180

    a = math.sin(delta_phi / 2) ** 2
    a += math.cos(phi_1) * math.cos(phi_2) * (math.sin(delta_lambda / 2) ** 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return r * c

@st.cache_resource()
def get_info(_G, str="new_graph"):
    points = []
    point_indexes = {}

    for node in _G.nodes():
        point_indexes[node] = len(points)
        points.append(node)

    nodes = len(points)

    connections = np.zeros((nodes, nodes), dtype=bool)

    for edge in _G.edges():
        start, end = point_indexes[edge[0]], point_indexes[edge[1]]

        connections[start, end] = True
        connections[end, start] = True

    points = np.array(points)

    distances = np.zeros((nodes, nodes), dtype=float)

    for i in range(nodes):
        for j in range(i + 1, nodes):
            distance = get_distance(points[i], points[j])
            distances[i, j] = distance
            distances[j, i] = distance

    return points, connections, distances
