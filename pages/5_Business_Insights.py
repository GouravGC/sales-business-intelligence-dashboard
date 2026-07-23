import streamlit as st
import os

# Define the path to the reports artifact folder
reports_path = "./artifacts/reports"

st.set_page_config(layout="wide")
st.title("Business Insights and Recommendations")

recommendations_filepath = os.path.join(reports_path, "business_recommendations.md")

if os.path.exists(recommendations_filepath):
    with open(recommendations_filepath, "r") as f:
        recommendations_content = f.read()
    st.markdown(recommendations_content)
else:
    st.warning("Business recommendations report not found. Please ensure `business_recommendations.md` exists in the artifacts/reports folder.")

st.markdown(
    "This section summarizes the key findings and actionable recommendations derived from the comprehensive analysis. "
    "The insights cover overall business health, seasonality, geographical performance, product performance, customer behavior, "
    "and the impact of discounts, providing strategic guidance for optimizing sales and enhancing profitability."
)