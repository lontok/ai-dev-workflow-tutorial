import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="ShopSmart Sales Dashboard",
    layout="wide"
)

# Dashboard title
st.title("ShopSmart Sales Dashboard")


@st.cache_data
def load_data() -> pd.DataFrame | None:
    """Load sales data from CSV with caching and error handling."""
    try:
        df = pd.read_csv("data/sales-data.csv", parse_dates=["date"])
        return df
    except FileNotFoundError:
        st.error("Error: Could not find data/sales-data.csv. Please ensure the data file exists.")
        return None


# Load data
df = load_data()

if df is not None:
    # Calculate KPIs (T006, T007)
    total_sales = df["total_amount"].sum()
    total_orders = len(df)

    # Display KPI metrics in two columns (T008, T009, T010)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Sales", value=f"${total_sales:,.2f}")
    with col2:
        st.metric(label="Total Orders", value=f"{total_orders:,}")
