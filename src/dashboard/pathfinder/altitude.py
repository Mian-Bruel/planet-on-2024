import struct
import streamlit as st

@st.cache_data()
def read_hgt(_file, latitude, longitude):
    """
    Reads altitude from an HGT _file for the given latitude and longitude.

    Parameters:
        _file (str): Path to the .hgt _file.
        latitude (float): Latitude in degrees (e.g., 52.1234).
        longitude (float): Longitude in degrees (e.g., 16.5678).

    Returns:
        int: Elevation in meters, or None if coordinates are out of range.
    """
    # Get the grid dimensions (3601 for 1 arc-second resolution)
    grid_size = 3601
    resolution = 1.0 / (grid_size - 1)  # 1 arc-second resolution

    # Extract the integer lat/lon from the _file name
    file_check = _file.split("/")[-1]
    hgt_lat = int(file_check[1:3])
    hgt_lon = int(file_check[4:7])
    # Adjust for N/S and E/W
    if file_check == 'S':
        hgt_lat = -hgt_lat
    if file_check == 'W':
        hgt_lon = -hgt_lon

    # Check if the latitude and longitude are in range
    if not (hgt_lat <= latitude < hgt_lat + 1 and hgt_lon <= longitude < hgt_lon + 1):
        return None

    # Calculate the row and column in the grid
    row = int((hgt_lat + 1 - latitude) / resolution)
    col = int((longitude - hgt_lon) / resolution)

    # Ensure the row and col are within bounds
    row = min(max(row, 0), grid_size - 1)
    col = min(max(col, 0), grid_size - 1)

    # Open the _file and read the elevation
    with open(_file, 'rb') as f:
        # Calculate the offset in the binary _file
        offset = (row * grid_size + col) * 2  # 2 bytes per elevation value
        f.seek(offset)
        # Read 2 bytes and unpack as a big-endian signed integer
        elevation = struct.unpack('>h', f.read(2))[0]

    return elevation
