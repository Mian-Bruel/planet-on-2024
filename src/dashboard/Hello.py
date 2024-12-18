import streamlit as st
from utils.utils import filter_and_sort_events
from utils.mock_data import local_progress, events, news

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
)

# Filter and sort events using the utility function
upcoming_events = filter_and_sort_events(events)

st.markdown(
    """
    <div style="text-align: center;">
        <h1>Welcome to Oborniki Forest!</h1>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style="text-align: center;">
        <h2>🌳 Local Goals Progress</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Centered content for each progress item
for item in local_progress:
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h3>{item['title']}</h3>
            <p> {item['description']}</p>
            <div style="width: 50%; margin: 0 auto;">
                <progress value="{item['progress_percentage']}" max="100" style="width: 100%; height: 20px;"></progress>
            </div>
            <p><strong>Progress:</strong> {item['progress_percentage']}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

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