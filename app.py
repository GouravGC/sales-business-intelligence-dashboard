import streamlit as st

st.set_page_config(
    page_title="Sales Business Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📊 Sales Business Intelligence Dashboard")
st.markdown("Welcome to the Sales Business Intelligence Dashboard! Navigate through the pages on the left to explore various aspects of the Superstore sales data.")

st.sidebar.title("Navigation")

st.info(
    "**Project Overview:** This project transforms raw sales data into actionable business intelligence using Python, Pandas, DuckDB, and Plotly. "
    "It covers KPIs, trend analysis, geographical and product performance, customer behavior, and the impact of discounts and shipping modes. "
    "The insights are crucial for strategic decision-making and improving overall business performance."
)

st.image("images/dashboard_overview.png", caption="Dashboard Overview")