# Planet-On-2024 Forests🌲

## Project Overview
The **Nazwa naszego projektu** is an interactive web application designed to help users plan forest routes while fostering a sense of community around the beauty and wonders of the forest. With the use of interactive maps, users can explore nature around them as well as take part in local environmental initiatives.

### Aim of the Project
The aim of this project is to provide an interactive platform where users can:
- **Plan routes** within the forest with real-time map integration, tailored to their preferences and needs.
- Track local **environmental initiatives** and other conservation efforts.
- Stay updated on the latest **news and events** related to the forest and its ecosystem.

This tool is intended to be used by locals, visitors to the forest, and anyone interested in the ongoing conservation efforts.

## Streamlit Tutorial

If you’re new to using this application or want to understand how to navigate the features, here’s a quick guide on the different possibilities:

- **Building Community:**
    - **Access Local Information**

        Click on any news item to get more detailed information about recent events, information about local environmental projects, and ongoing conservation efforts. 
    - **Track Progress and Goals:**

        The app provides information on local environmental goals, such as planting trees and maintaining trails.
    - **Vote on Local Initiatives:**

        Participate in community votes on local initiatives or propose your own ideas for developing the forest.
- **Plan Your Experience in the Forest:**
    - **Explore the Interactive Map:**
        
        Application displays an interactive map of the forest, with various paths, trails, and points of interest highlighted. You can explore different areas of the forest by zooming in and out or dragging the map to view specific locations.
    - **Plan Your Route:**
        -  Use the **slider** in the sidebar to set a **maximum distance** for your route. This helps you plan manageable trips based on your preferences.


This application is designed to be a one-stop platform for all things related to the forest, whether you’re planning a trip, looking to get involved in local initiatives, or simply want to stay informed about the latest news and events.

## Technical Details

### Tools and Technologies Used
- **Streamlit:** Streamlit is an open-source app framework for Machine Learning and Data Science projects. It allows you to create interactive web applications directly from Python scripts.

- **Folium:** Folium is a Python library used for visualizing geospatial data. It allows you to create interactive maps directly within your web application.

- **NetworkX:** NetworkX is a Python library used for creating, manipulating, and studying complex networks. It is used here for graph-based map handling.

### Data Sources
Spacial data for the forest map was obtained from the OpenStreetMap project, which provides free geographic data such as streets, buildings, and forests. The news and environmental initiative data is generated for demonstration purposes and does not reflect real-world events.


## How to Run the Code

### Prerequisites
Before running the application, you need to have the following installed:

- Python 3.x
- Streamlit
- Folium
- NetworkX
- Other required libraries (such as `pandas`, `geopandas`, etc.)

### Installation Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/Mian-Bruel/planet-on-2024
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Linux/Mac
    .venv\Scripts\activate     # For Windows
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit application:
    ```bash
    python -m streamlit run src/dasahboard/Hello.py
    ```

5. Open your browser and navigate to `http://localhost:8501` to view the application.


## Future Work

While this project serves as an interactive map and progress tracker, there are several ways in which it can be expanded and improved in the future:

- **Expansion to Other Forests:**
  - The application can be easily adapted to include data and routes for other forests, providing a wider range of exploration opportunities for users across different regions.

- **Mobile Application:**
  - Developing a mobile-friendly version or a dedicated mobile app would allow users to access the map and plan routes directly on their smartphones during their forest visits.

- **Enhanced Filtering Options:**
  - Adding more filters such as difficulty level, terrain type, or points of interest (e.g., scenic spots, picnic areas) would provide a more tailored experience for users.

- **Community Features:**
  - Introducing features like user-generated reviews, favorite trails, or community event planning to foster greater interaction among users.

- **Gamification:**
  - Adding gamified elements like achievements for exploring specific trails or participating in conservation activities to encourage user engagement.

- **Integration with Navigation Tools:**
  - Adding the ability to export routes to popular navigation apps like Google Maps for easier in-forest navigation.

These enhancements would not only improve usability but also strengthen the community’s connection to their natural surroundings.
