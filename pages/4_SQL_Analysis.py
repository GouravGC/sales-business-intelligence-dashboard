import streamlit as st
import pandas as pd
from utils import load_df_from_csv, summaries_path

st.set_page_config(layout="wide")
st.title("SQL Analysis Results")

st.markdown("### Yearly Revenue Trend")
yearly_revenue_df = load_df_from_csv("yearly_revenue_trend.csv", summaries_path)
if yearly_revenue_df is not None:
    st.dataframe(yearly_revenue_df, use_container_width=True)
else:
    st.warning("Yearly revenue trend data not found.")

st.markdown("### Yearly Profit Trend")
yearly_profit_df = load_df_from_csv("yearly_profit_trend.csv", summaries_path)
if yearly_profit_df is not None:
    st.dataframe(yearly_profit_df, use_container_width=True)
else:
    st.warning("Yearly profit trend data not found.")

st.markdown("### Monthly Revenue Trend")
monthly_revenue_df = load_df_from_csv("monthly_revenue_trend.csv", summaries_path)
if monthly_revenue_df is not None:
    st.dataframe(monthly_revenue_df, use_container_width=True)
else:
    st.warning("Monthly revenue trend data not found.")

st.markdown("### Monthly Profit Trend")
monthly_profit_df = load_df_from_csv("monthly_profit_trend.csv", summaries_path)
if monthly_profit_df is not None:
    st.dataframe(monthly_profit_df, use_container_width=True)
else:
    st.warning("Monthly profit trend data not found.")

st.markdown("### Quarterly Revenue Trend")
quarterly_revenue_df = load_df_from_csv("quarterly_revenue_trend.csv", summaries_path)
if quarterly_revenue_df is not None:
    st.dataframe(quarterly_revenue_df, use_container_width=True)
else:
    st.warning("Quarterly revenue trend data not found.")

st.markdown("### Quarterly Profit Trend")
quarterly_profit_df = load_df_from_csv("quarterly_profit_trend.csv", summaries_path)
if quarterly_profit_df is not None:
    st.dataframe(quarterly_profit_df, use_container_width=True)
else:
    st.warning("Quarterly profit trend data not found.")

st.markdown("### Revenue by Region")
revenue_by_region_df = load_df_from_csv("revenue_by_region.csv", summaries_path)
if revenue_by_region_df is not None:
    st.dataframe(revenue_by_region_df, use_container_width=True)
else:
    st.warning("Revenue by region data not found.")

st.markdown("### Profit by Region")
profit_by_region_df = load_df_from_csv("profit_by_region.csv", summaries_path)
if profit_by_region_df is not None:
    st.dataframe(profit_by_region_df, use_container_width=True)
else:
    st.warning("Profit by region data not found.")

st.markdown("### Top 10 States by Revenue")
top_10_states_revenue_df = load_df_from_csv("top_10_states_by_revenue.csv", summaries_path)
if top_10_states_revenue_df is not None:
    st.dataframe(top_10_states_revenue_df, use_container_width=True)
else:
    st.warning("Top 10 states by revenue data not found.")

st.markdown("### Bottom 10 States by Profit")
bottom_10_states_profit_df = load_df_from_csv("bottom_10_states_by_profit.csv", summaries_path)
if bottom_10_states_profit_df is not None:
    st.dataframe(bottom_10_states_profit_df, use_container_width=True)
else:
    st.warning("Bottom 10 states by profit data not found.")

st.markdown("### Top 10 Cities by Revenue")
top_10_cities_revenue_df = load_df_from_csv("top_10_cities_by_revenue.csv", summaries_path)
if top_10_cities_revenue_df is not None:
    st.dataframe(top_10_cities_revenue_df, use_container_width=True)
else:
    st.warning("Top 10 cities by revenue data not found.")

st.markdown("### Top 10 Customers by Revenue")
top_10_customers_revenue_df = load_df_from_csv("top_10_customers_by_revenue.csv", summaries_path)
if top_10_customers_revenue_df is not None:
    st.dataframe(top_10_customers_revenue_df, use_container_width=True)
else:
    st.warning("Top 10 customers by revenue data not found.")

st.markdown("### Top 10 Customers by Profit")
top_10_customers_profit_df = load_df_from_csv("top_10_customers_by_profit.csv", summaries_path)
if top_10_customers_profit_df is not None:
    st.dataframe(top_10_customers_profit_df, use_container_width=True)
else:
    st.warning("Top 10 customers by profit data not found.")

st.markdown("### Customer Count by Segment")
customer_count_by_segment_df = load_df_from_csv("customer_count_by_segment.csv", summaries_path)
if customer_count_by_segment_df is not None:
    st.dataframe(customer_count_by_segment_df, use_container_width=True)
else:
    st.warning("Customer count by segment data not found.")

st.markdown("### Revenue by Segment")
revenue_by_segment_df = load_df_from_csv("revenue_by_segment.csv", summaries_path)
if revenue_by_segment_df is not None:
    st.dataframe(revenue_by_segment_df, use_container_width=True)
else:
    st.warning("Revenue by segment data not found.")

st.markdown("### Revenue by Category")
revenue_by_category_df = load_df_from_csv("revenue_by_category.csv", summaries_path)
if revenue_by_category_df is not None:
    st.dataframe(revenue_by_category_df, use_container_width=True)
else:
    st.warning("Revenue by category data not found.")

st.markdown("### Profit by Category")
profit_by_category_df = load_df_from_csv("profit_by_category.csv", summaries_path)
if profit_by_category_df is not None:
    st.dataframe(profit_by_category_df, use_container_width=True)
else:
    st.warning("Profit by category data not found.")

st.markdown("### Revenue by Sub-Category")
revenue_by_subcategory_df = load_df_from_csv("revenue_by_subcategory.csv", summaries_path)
if revenue_by_subcategory_df is not None:
    st.dataframe(revenue_by_subcategory_df, use_container_width=True)
else:
    st.warning("Revenue by sub-category data not found.")

st.markdown("### Profit by Sub-Category")
profit_by_subcategory_df = load_df_from_csv("profit_by_subcategory.csv", summaries_path)
if profit_by_subcategory_df is not None:
    st.dataframe(profit_by_subcategory_df, use_container_width=True)
else:
    st.warning("Profit by sub-category data not found.")

st.markdown("### Top 10 Products by Revenue")
top_10_products_revenue_df = load_df_from_csv("top_10_products_by_revenue.csv", summaries_path)
if top_10_products_revenue_df is not None:
    st.dataframe(top_10_products_revenue_df, use_container_width=True)
else:
    st.warning("Top 10 products by revenue data not found.")

st.markdown("### Top 10 Products by Profit")
top_10_products_profit_df = load_df_from_csv("top_10_products_by_profit.csv", summaries_path)
if top_10_products_profit_df is not None:
    st.dataframe(top_10_products_profit_df, use_container_width=True)
else:
    st.warning("Top 10 products by profit data not found.")

st.markdown("### Average Discount by Category")
avg_discount_by_category_df = load_df_from_csv("average_discount_by_category.csv", summaries_path)
if avg_discount_by_category_df is not None:
    st.dataframe(avg_discount_by_category_df, use_container_width=True)
else:
    st.warning("Average discount by category data not found.")

st.markdown("### Revenue by Ship Mode")
revenue_by_ship_mode_df = load_df_from_csv("revenue_by_ship_mode.csv", summaries_path)
if revenue_by_ship_mode_df is not None:
    st.dataframe(revenue_by_ship_mode_df, use_container_width=True)
else:
    st.warning("Revenue by ship mode data not found.")

st.markdown("### Profit by Ship Mode")
profit_by_ship_mode_df = load_df_from_csv("profit_by_ship_mode.csv", summaries_path)
if profit_by_ship_mode_df is not None:
    st.dataframe(profit_by_ship_mode_df, use_container_width=True)
else:
    st.warning("Profit by ship mode data not found.")

st.markdown("### Seasonal Sales Trend")
seasonal_sales_trend_df = load_df_from_csv("seasonal_sales_trend.csv", summaries_path)
if seasonal_sales_trend_df is not None:
    st.dataframe(seasonal_sales_trend_df, use_container_width=True)
else:
    st.warning("Seasonal sales trend data not found.")