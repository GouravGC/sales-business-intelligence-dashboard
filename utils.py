import os
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components

# Define the base path for all artifacts
artifacts_base_path = "./artifacts"

# Define paths for specific artifact types
datasets_clean_path = os.path.join(artifacts_base_path, "datasets","clean")
datasets_raw_path = os.path.join( artifacts_base_path,"datasets","raw")

plots_eda_path = os.path.join(artifacts_base_path, "plots", "eda")
plots_business_path = os.path.join(artifacts_base_path, "plots", "business")
plots_distributions_path = os.path.join(artifacts_base_path, "plots", "distributions")
plots_trends_path = os.path.join(artifacts_base_path, "plots", "trends")
plots_correlations_path = os.path.join(artifacts_base_path, "plots", "correlations")
plots_dashboards_path = os.path.join(artifacts_base_path, "plots", "dashboards")

reports_path = os.path.join(artifacts_base_path, "reports")
summaries_path = os.path.join(artifacts_base_path, "summaries")
sql_path = os.path.join(artifacts_base_path, "sql")
kpis_path = os.path.join(artifacts_base_path, "kpis")
metadata_path = os.path.join(artifacts_base_path, "metadata")
logs_path = os.path.join(artifacts_base_path, "logs")

# Helper function to load DataFrame from CSV
@st.cache_data
def load_df_from_csv(filename, path):
    filepath = os.path.join(path, filename)
    if os.path.exists(filepath):
        try:
            df = pd.read_csv(filepath)
            return df
        except Exception as e:
            st.error(f"Error loading {filename}: {e}")
            return None
    else:
        st.warning(f"{filename} not found at {filepath}")
        return None

# Helper function to load JSON report
@st.cache_data
def load_json_report(filename, path):
    filepath = os.path.join(path, filename)
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
            return data
        except Exception as e:
            st.error(f"Error loading {filename}: {e}")
            return None
    else:
        st.warning(f"{filename} not found at {filepath}")
        return None

# Helper function to display Plotly figure from HTML
def display_plotly_fig_from_html(filename_base, path):
    html_path = os.path.join(path, f"{filename_base}.html")

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    components.html(
        html,
        height=900,
        width=1400,
        scrolling=True,
    )

# Helper function to display KPI cards
def display_kpi_card(title, value, delta=None, help_text=None):
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        st.metric(label=title, value=value, delta=delta, help=help_text)
    with col2:
        st.write("") # Placeholder for additional info if needed