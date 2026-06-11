import streamlit as st
from market_research_agent import market_analysis

st.set_page_config(page_title="Market Research Assistant")

st.title("Intelligent Market Research Assistant")

query = st.text_input("Enter Market Research Query")

if st.button("Analyze"):
result = market_analysis(query)
st.write(result)
