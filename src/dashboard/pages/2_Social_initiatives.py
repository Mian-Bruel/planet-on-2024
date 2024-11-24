import streamlit as st

initiatives = {
    "Beehive introduction":
       "Introducing beehives to the forest to help with pollination.",
    "Tree planting":
        "Planting new trees to help the forest grow.",
    "New path near the river":
        "Creating a new path near the river for the community to enjoy.",
}

for title, description in initiatives.items():
    st.markdown(f"## {title}")
    st.markdown(description)
    st.markdown("[upvote](#) this initiative! 🌳")
    st.markdown("---")
