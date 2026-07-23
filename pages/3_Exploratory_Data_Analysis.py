import streamlit as st
from utils import display_plotly_fig_from_html, plots_distributions_path, plots_eda_path, plots_correlations_path, summaries_path, load_df_from_csv
import pandas as pd

st.set_page_config(layout="wide")
st.title("Exploratory Data Analysis (EDA)")

st.markdown("### Sales Distribution")
display_plotly_fig_from_html("sales_distribution", plots_distributions_path)

st.markdown("### Profit Distribution")
display_plotly_fig_from_html("profit_distribution", plots_distributions_path)

st.markdown("### Discount vs Profit")
display_plotly_fig_from_html("discount_vs_profit", plots_correlations_path)

st.markdown("### Correlation Matrix")
display_plotly_fig_from_html("correlation_matrix", plots_correlations_path)

st.markdown("### ABC Analysis - Top Products")
display_plotly_fig_from_html("abc_analysis_top_products", plots_eda_path)

st.markdown("### Pareto Analysis")
display_plotly_fig_from_html("pareto_analysis", plots_eda_path)

st.markdown("### Raw Correlation Data")
correlation_df = load_df_from_csv("correlation_matrix.csv", summaries_path)
if correlation_df is not None:
    st.dataframe(correlation_df, use_container_width=True)
else:
    st.warning("Correlation matrix data not found.")

st.markdown("### ABC Analysis Data")
abc_df = load_df_from_csv("abc_analysis_summary.csv", summaries_path)
if abc_df is not None:
    st.dataframe(abc_df, use_container_width=True)
else:
    st.warning("ABC Analysis summary data not found.")