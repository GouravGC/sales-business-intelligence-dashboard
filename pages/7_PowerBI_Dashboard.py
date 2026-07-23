import streamlit as st
import os
import base64

st.set_page_config(
    page_title="Power BI Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Power BI Dashboard")

st.markdown("""
This project also includes a professional **Microsoft Power BI Dashboard**
created using the same Sales Business Intelligence dataset.

The dashboard provides interactive business insights including:

- 💰 Revenue Analysis
- 📈 Profit Analysis
- 🌍 Regional Performance
- 📦 Product & Category Performance
- 👥 Customer Insights
- 📊 Executive KPI Dashboard

The complete dashboard can be previewed below or downloaded for further exploration.
""")

# ---------------------------------------------------------
# File Paths
# ---------------------------------------------------------

PDF_PATH = "powerbi/Sales_Business_Intelligence_Dashboard.pdf"
PBIX_PATH = "powerbi/Sales_Business_Intelligence_Dashboard.pbix"

# ---------------------------------------------------------
# Embedded PDF Preview
# ---------------------------------------------------------

st.markdown("---")
st.subheader("📄 Power BI Dashboard Preview")

if os.path.exists(PDF_PATH):

    with open(PDF_PATH, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="100%"
        height="900"
        style="border:none;border-radius:10px;">
    </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)

else:
    st.warning("Power BI PDF not found.")

# ---------------------------------------------------------
# Downloads
# ---------------------------------------------------------

st.markdown("---")
st.subheader("⬇ Download Dashboard Files")

col1, col2 = st.columns(2)

with col1:

    if os.path.exists(PDF_PATH):

        with open(PDF_PATH, "rb") as file:
            st.download_button(
                label="📄 Download Power BI PDF",
                data=file,
                file_name="Sales_Business_Intelligence_Dashboard.pdf",
                mime="application/pdf",
                use_container_width=True
            )

with col2:

    if os.path.exists(PBIX_PATH):

        with open(PBIX_PATH, "rb") as file:
            st.download_button(
                label="📊 Download Power BI Project (.pbix)",
                data=file,
                file_name="Sales_Business_Intelligence_Dashboard.pbix",
                mime="application/octet-stream",
                use_container_width=True
            )

st.markdown("---")

st.info(
    "The Power BI (.pbix) file can be opened using Microsoft Power BI Desktop. "
    "The embedded PDF provides a quick preview of the dashboard layout and business insights."
)