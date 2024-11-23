import geopandas as gpd
import networkx as nx
from shapely.geometry import LineString, MultiPoint
from shapely.ops import split
import osmnx as ox
import pickle
from geopy.distance import geodesic

from shapely.geometry import GeometryCollection

from shapely.geometry import GeometryCollection

def split_linestrings_at_intersections(geometries):
    """Split LineStrings at their intersections."""
    all_intersection_points = []

    # Collect all intersection points
    for i, line1 in enumerate(geometries):
        if not isinstance(line1, LineString):
            continue
        for j, line2 in enumerate(geometries):
            if i >= j:  # Avoid duplicate checks
                continue
            if line1.intersects(line2):
                intersection = line1.intersection(line2)
                if intersection.is_empty:
                    continue
                if intersection.geom_type == "Point":
                    all_intersection_points.append(intersection)
                # elif intersection.geom_type == "MultiPoint":
                #     all_intersection_points.extend(intersection.geoms)

    # Split each LineString at intersection points
    new_geometries = []
    for line in geometries:
        if isinstance(line, LineString):
            split_points = [pt for pt in all_intersection_points if line.intersects(pt)]
            if split_points:
                # Perform the split
                split_result = split(line, MultiPoint(split_points))
                if isinstance(split_result, GeometryCollection):
                    # Extract LineString components from the GeometryCollection
                    for geom in split_result.geoms:
                        if isinstance(geom, LineString):
                            new_geometries.append(geom)
                else:
                    new_geometries.extend(split_result)
            else:
                new_geometries.append(line)
    return new_geometries


def create_graph_from_geometries(geometries):
    """Create a graph representation from LineStrings."""
    G = nx.Graph()
    for line in geometries:
        if isinstance(line, LineString):
            coords = list(line.coords)
            for i in range(len(coords) - 1):
                node_start = coords[i]
                node_end = coords[i + 1]

                # Calculate distance
                distance = geodesic((node_start[1], node_start[0]), (node_end[1], node_end[0])).meters

                # Add nodes and edge
                G.add_node(node_start, x=node_start[0], y=node_start[1])
                G.add_node(node_end, x=node_end[0], y=node_end[1])
                G.add_edge(node_start, node_end, length=distance)
    return G


import matplotlib.pyplot as plt

def plot_graph_subset(G, center_node=None, radius=0.01):
    """
    Plot a small subset of a graph centered around a given node or first node.
    :param G: NetworkX graph
    :param center_node: Node to center the subset around (default: first node)
    :param radius: Radius (in coordinate units) for selecting nearby nodes
    """
    # Select a center node if not provided
    if center_node is None:
        center_node = list(G.nodes)[0]

    # Get the position of the center node
    center_x, center_y = G.nodes[center_node]['x'], G.nodes[center_node]['y']

    # Filter nodes within the specified radius
    subset_nodes = [
        n for n, attrs in G.nodes(data=True)
        if abs(attrs['x'] - center_x) <= radius and abs(attrs['y'] - center_y) <= radius
    ]

    # Create a subgraph from these nodes
    subgraph = G.subgraph(subset_nodes)

    # Extract positions for plotting
    pos = {n: (attrs['x'], attrs['y']) for n, attrs in subgraph.nodes(data=True)}

    # Plot the subgraph
    plt.figure(figsize=(10, 10))
    nx.draw(
        subgraph, pos, with_labels=False, node_size=20, node_color="red", edge_color="blue"
    )
    plt.title("Graph Subset")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()


if __name__ == "__main__":
    # Load your data
    
    latitude = 52.6578
    longitude = 16.81660
    radius = 3000
    pavement_tags = {"highway": ["track", "path", "footway", "cycleway"]}
    pavements_gdf = ox.features.features_from_point((latitude, longitude), tags=pavement_tags, dist=radius)
    pavements_gdf = pavements_gdf.to_crs(epsg=4326)


    # Split LineStrings at intersections
    split_geometries = split_linestrings_at_intersections(pavements_gdf.geometry)

    # Create the graph
    G = create_graph_from_geometries(split_geometries)
    G = G.to_undirected()

    # edges = 0
    # for node in G.nodes:
    #     edges += len(G.edges(node)) if len(G.edges(node)) >= 3 else 0
    # print(edges)


    # save to pickle
    with open('graph.pkl', 'wb') as f:
        pickle.dump(G, f)

