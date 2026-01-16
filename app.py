import streamlit as st
import pandas as pd
import plotly.express as px

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

    # Sales Trend Over Time (T011-T015)
    # Aggregate sales by month
    monthly_sales = df.groupby(df["date"].dt.to_period("M"))["total_amount"].sum().reset_index()
    monthly_sales["date"] = monthly_sales["date"].astype(str)

    # Create Plotly line chart
    fig = px.line(
        monthly_sales,
        x="date",
        y="total_amount",
        title="Sales Trend Over Time",
        labels={"date": "Month", "total_amount": "Sales ($)"},
    )

    # Configure hover template
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>"
    )

    # Display chart
    st.plotly_chart(fig, use_container_width=True)
