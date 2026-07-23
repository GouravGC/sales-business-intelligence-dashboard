import streamlit as st
import pandas as pd
from utils import load_json_report, display_plotly_fig_from_html, kpis_path, plots_dashboards_path, plots_trends_path, plots_business_path, plots_eda_path

st.set_page_config(layout="wide")
st.title("Dashboard Overview")

st.markdown("### Key Performance Indicators (KPIs)")

kpi_summary = load_json_report("kpi_summary.json", kpis_path)

if kpi_summary:

    row1 = st.columns(4)

    with row1[0]:
        st.metric("Total Revenue", f"${kpi_summary['Total_Revenue']:,.2f}")

    with row1[1]:
        st.metric("Total Profit", f"${kpi_summary['Total_Profit']:,.2f}")

    with row1[2]:
        st.metric("Total Orders", f"{kpi_summary['Total_Orders']:,}")

    with row1[3]:
        st.metric("Total Customers", f"{kpi_summary['Total_Customers']:,}")

    row2 = st.columns(4)

    with row2[0]:
        st.metric("Avg Order Value", f"${kpi_summary['Average_Order_Value']:,.2f}")

    with row2[1]:
        st.metric("Profit Margin", f"{kpi_summary['Profit_Margin_Percentage']:,.2f}%")

    with row2[2]:
        st.metric("Avg Sales/Customer", f"${kpi_summary['Avg_Sales_Per_Customer']:,.2f}")

    with row2[3]:
        st.metric("Avg Profit/Order", f"${kpi_summary['Avg_Profit_Per_Order']:,.2f}")
else:
    st.warning("KPIs not loaded. Please ensure `kpi_summary.json` exists in the artifacts folder.")

st.markdown("### Key Visualizations")

tab1, tab2, tab3, tab4 = st.tabs(["Monthly Revenue", "Monthly Profit", "Regional Performance", "Product Performance"])

with tab1:
    st.subheader("Monthly Revenue Trend")
    display_plotly_fig_from_html("monthly_revenue_trend", plots_trends_path)

with tab2:
    st.subheader("Monthly Profit Trend")
    display_plotly_fig_from_html("monthly_profit_trend", plots_trends_path)

with tab3:
    st.subheader("Revenue by Region")
    display_plotly_fig_from_html("revenue_by_region", plots_business_path)
    st.subheader("Profit by Region")
    display_plotly_fig_from_html("profit_by_region", plots_business_path)

with tab4:
    st.subheader("Sales by Category")
    display_plotly_fig_from_html("sales_by_category", plots_business_path)
    st.subheader("Profit by Category")
    display_plotly_fig_from_html("profit_by_category", plots_business_path)