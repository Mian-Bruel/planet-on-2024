import streamlit as st
from utils.utils import filter_and_sort_events

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
)

# MOCK DATA
# Example local goal percentage
local_goal_percentage = 65

# Mock data for events with additional info
events = [
    {"title": "Tree Planting Day", "date": "2024-11-25", "description": "Join us for a day of planting new trees in the Oborniki forest.", "location": "North Meadow, Oborniki", "url": "https://example.com/tree-planting"},
    {"title": "Forest Cleanup Drive", "date": "2024-12-01", "description": "Help us clean up litter and preserve the beauty of our forest.", "location": "East Trailhead, Oborniki", "url": "https://example.com/forest-cleanup"},
    {"title": "Nature Photography Contest", "date": "2024-12-15", "description": "Showcase your photography skills and win exciting prizes!", "location": "Central Lookout, Oborniki", "url": "https://example.com/photography-contest"},
    {"title": "Old Event", "date": "2024-11-20", "description": "This event has already passed.", "location": "Unknown", "url": "#"},
]

# Filter and sort events using the utility function
upcoming_events = filter_and_sort_events(events)

# Mock data for local news
news = [
    {"title": "Oborniki Forest wins regional conservation award!", "url": "https://example.com/award"},
    {"title": "New walking trails opened last weekend.", "url": "https://example.com/new-trails"},
    {"title": "Forest ranger shares tips on wildfire prevention.", "url": "https://example.com/wildfire-prevention"},
]

st.write("# Welcome to Oborniki Forest! 🌲")

# Add progress bar at the top
st.markdown(f"### Local Goal Progress 🌟 ({local_goal_percentage}%)")
st.progress(local_goal_percentage / 100)

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This is a demo of the Oborniki route planner and social hub for your local foresters.
    """
)

# Split the screen into two sections
col1, col2 = st.columns([3, 1])

# Populate Local News in the first column
with col1:
    st.markdown("## 📰 Local News")
    for article in news:
        st.markdown(f"- [{article['title']}]({article['url']})")

# Populate Events in the second column
with col2:
    st.markdown("## 🌟 Upcoming Events")
    for event in upcoming_events:
        with st.expander(f"**{event['title']}** \n\n 📅 {event['date']}"):
            st.markdown(f"**Description**: {event['description']}")
            st.markdown(f"**Location**: {event['location']}")
            st.markdown(f"[More Info]({event['url']})")