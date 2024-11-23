import streamlit as st

from utils.mock_data import news

st.write("""
         # Welcome to Oborniki Forest! 🌲
         Here is the latest news and social actions happening in the forest:
         """)

# Populate Local News in the first column
st.markdown("## 📰 Local News")
for article in news:
        st.markdown(f"### {article['title']}")
        st.markdown(f"**Description**: {article['description']}")
        st.markdown(f"[More Info]({article['url']})")

        st.markdown("---")
