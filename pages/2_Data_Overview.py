import streamlit as st
import pandas as pd
from utils import load_df_from_csv, datasets_clean_path

st.set_page_config(layout="wide")
st.title("Data Overview")

st.markdown("### Cleaned and Processed Data")

df_cleaned = load_df_from_csv("sales_cleaned.csv", datasets_clean_path)

if df_cleaned is not None:
    st.write("Displaying the first 100 rows of the cleaned dataset.")
    st.dataframe(df_cleaned.head(100), use_container_width=True)

    st.markdown("### Dataset Information")
    buffer = pd.io.common.StringIO()
    df_cleaned.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.markdown("### Descriptive Statistics")
    st.dataframe(df_cleaned.describe(include='all').T, use_container_width=True)

    st.markdown("### Missing Values (from raw metadata)")
    # Assuming raw_dataset_metadata.json contains missing_values info
    # If not, you might need a specific CSV for missing values
    from utils import metadata_path, load_json_report
    raw_metadata = load_json_report("raw_dataset_metadata.json", metadata_path)
    if raw_metadata and "missing_values" in raw_metadata:
        missing_df = pd.DataFrame.from_dict(raw_metadata["missing_values"], orient="index", columns=["Missing Count"])
        missing_df = missing_df[missing_df["Missing Count"] > 0].sort_values(by="Missing Count", ascending=False)
        if not missing_df.empty:
            st.dataframe(missing_df)
        else:
            st.info("No missing values were recorded in the raw dataset metadata.")
    else:
        st.warning("Missing values summary not available.")

    st.markdown("### Duplicate Rows (from raw metadata)")
    if raw_metadata and "duplicate_rows" in raw_metadata:
        st.write(f"Total Duplicate Rows in Raw Data: {raw_metadata['duplicate_rows']}")
    else:
        st.warning("Duplicate rows summary not available.")

else:
    st.error("Cleaned sales data not loaded. Please ensure `sales_cleaned.csv` exists in the artifacts folder.")