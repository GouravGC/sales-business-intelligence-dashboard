import streamlit as st
import os
import pandas as pd
import json
from utils import datasets_clean_path, summaries_path, kpis_path, load_df_from_csv, load_json_report

st.set_page_config(layout="wide")
st.title("Reports and Downloads")

st.markdown("### Download Processed Datasets")

# Cleaned sales data
cleaned_sales_df = load_df_from_csv("sales_cleaned.csv", datasets_clean_path)
if cleaned_sales_df is not None:
    st.download_button(
        label="Download Cleaned Sales Data (CSV)",
        data=cleaned_sales_df.to_csv(index=False).encode('utf-8'),
        file_name="sales_cleaned.csv",
        mime="text/csv",
    )

st.markdown("### Download KPI Summaries")

# All KPIs summary
all_kpis_df = load_df_from_csv("all_kpis_summary.csv", kpis_path)
if all_kpis_df is not None:
    st.download_button(
        label="Download All KPIs Summary (CSV)",
        data=all_kpis_df.to_csv(index=False).encode('utf-8'),
        file_name="all_kpis_summary.csv",
        mime="text/csv",
    )

# KPI JSON
kpi_json_data = load_json_report("kpi_summary.json", kpis_path)
if kpi_json_data is not None:
    st.download_button(
        label="Download KPI Summary (JSON)",
        data=json.dumps(kpi_json_data,indent=4,ensure_ascii=False).encode("utf-8"),
        file_name="kpi_summary.json",
        mime="application/json",
    )

st.markdown("### Download Summary Tables")

# Example: Monthly Revenue Trend
monthly_revenue_trend_df = load_df_from_csv("monthly_revenue_trend.csv", summaries_path)
if monthly_revenue_trend_df is not None:
    st.download_button(
        label="Download Monthly Revenue Trend (CSV)",
        data=monthly_revenue_trend_df.to_csv(index=False).encode('utf-8'),
        file_name="monthly_revenue_trend.csv",
        mime="text/csv",
    )

# Example: Bottom 10 States by Profit
bottom_10_states_profit_df = load_df_from_csv("bottom_10_states_by_profit.csv", summaries_path)
if bottom_10_states_profit_df is not None:
    st.download_button(
        label="Download Bottom 10 States by Profit (CSV)",
        data=bottom_10_states_profit_df.to_csv(index=False).encode('utf-8'),
        file_name="bottom_10_states_by_profit.csv",
        mime="text/csv",
    )

st.markdown("### Download Reports")

# Business Recommendations (Markdown)
reports_path = "./artifacts/reports"
recommendations_filepath = os.path.join(reports_path, "business_recommendations.md")
if os.path.exists(recommendations_filepath):
    with open(recommendations_filepath, "r") as f:
        recommendations_content = f.read()
    st.download_button(
        label="Download Business Recommendations (Markdown)",
        data=recommendations_content.encode('utf-8'),
        file_name="business_recommendations.md",
        mime="text/markdown",
    )

st.markdown(
    "This page allows you to download various processed datasets, KPI summaries, and reports generated during the analysis. "
    "Use these files for further analysis, integration into other systems, or offline viewing."
)