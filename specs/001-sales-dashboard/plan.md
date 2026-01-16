# Implementation Plan: E-Commerce Sales Dashboard

**Branch**: `001-sales-dashboard` | **Date**: 2026-01-15 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/001-sales-dashboard/spec.md`

## Summary

Build a Streamlit sales dashboard that displays KPIs (Total Sales, Total Orders), a sales trend line chart, and bar charts for category and region breakdowns. The dashboard loads data from CSV, uses Plotly for interactive visualizations, and deploys to Streamlit Community Cloud for public access.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: Streamlit, Pandas, Plotly
**Storage**: CSV file (data/sales-data.csv, 482 records)
**Testing**: Manual verification (Phase 1)
**Target Platform**: Web browser via Streamlit Community Cloud
**Project Type**: Single-file Streamlit application
**Performance Goals**: Dashboard loads within 5 seconds
**Constraints**: No authentication, static data refresh
**Scale/Scope**: ~500 transactions, 5 categories, 4 regions, 12 months

## Constitution Check

*GATE: Must pass before implementation. All principles verified.*

| Principle | Status | Verification |
|-----------|--------|--------------|
| I. Simple & Readable Code | ✅ PASS | Single-file app, descriptive naming, PEP 8 |
| II. User-Friendly Interactive Visualizations | ✅ PASS | Plotly charts with tooltips, logical layout |
| III. Python Best Practices | ✅ PASS | Type hints, venv, requirements.txt |

**Technology Stack Alignment**:
- Python 3.11+ ✅
- Streamlit ✅
- Pandas ✅
- Plotly ✅ (constitution v1.1.0 updated)

## Project Structure

### Documentation (this feature)

```text
specs/001-sales-dashboard/
├── spec.md              # Feature specification
├── plan.md              # This file
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Task list (created by /speckit.tasks)
```

### Source Code (repository root)

```text
app.py                   # Main Streamlit application
requirements.txt         # Python dependencies
data/
└── sales-data.csv       # Source data (already exists)
.streamlit/
└── config.toml          # Streamlit configuration (optional)
```

**Structure Decision**: Single-file Streamlit application at repository root. This is the simplest structure that works with Streamlit Community Cloud deployment and aligns with Constitution Principle I (simplicity).

## Implementation Approach

### Phase 1: Project Setup

1. Create `requirements.txt` with dependencies:
   ```
   streamlit
   pandas
   plotly
   ```

2. Create basic `app.py` structure with:
   - Page configuration (title, layout)
   - Data loading function
   - Main app entry point

### Phase 2: Data Loading (US1 Foundation)

1. Load CSV using Pandas
2. Parse date column
3. Handle missing file gracefully with error message
4. Cache data loading with `@st.cache_data`

### Phase 3: KPI Display (US1 - P1)

1. Calculate Total Sales: `df['total_amount'].sum()`
2. Calculate Total Orders: `len(df)`
3. Display using `st.metric()` in columns
4. Format currency with `${:,.2f}`

### Phase 4: Sales Trend Chart (US2 - P2)

1. Aggregate sales by month using Pandas groupby
2. Create Plotly line chart with:
   - X-axis: Month (formatted as "Jan 2024")
   - Y-axis: Sales amount
   - Hover template showing exact values
3. Display with `st.plotly_chart()`

### Phase 5: Category Breakdown (US3 - P3)

1. Aggregate sales by category
2. Sort descending by value
3. Create horizontal bar chart with Plotly
4. Display with proper labels and tooltips

### Phase 6: Region Breakdown (US4 - P4)

1. Aggregate sales by region
2. Sort descending by value
3. Create horizontal bar chart with Plotly
4. Display side-by-side with category chart using columns

### Phase 7: Deployment (US5 - P5)

1. Push code to GitHub
2. Connect repository to Streamlit Community Cloud
3. Deploy and verify public URL works
4. Test in multiple browsers

## Data Model

### Input: sales-data.csv

| Column | Type | Usage |
|--------|------|-------|
| date | datetime | Trend aggregation (by month) |
| order_id | string | Count for Total Orders |
| product | string | Not used in Phase 1 |
| category | string | Category breakdown grouping |
| region | string | Region breakdown grouping |
| quantity | int | Not used in Phase 1 |
| unit_price | float | Not used in Phase 1 |
| total_amount | float | Sum for Total Sales, all charts |

### Aggregations

```python
# KPIs
total_sales = df['total_amount'].sum()
total_orders = len(df)

# Trend (monthly)
monthly_sales = df.groupby(df['date'].dt.to_period('M'))['total_amount'].sum()

# Category breakdown
category_sales = df.groupby('category')['total_amount'].sum().sort_values(ascending=False)

# Region breakdown
region_sales = df.groupby('region')['total_amount'].sum().sort_values(ascending=False)
```

## Layout Specification

```
┌─────────────────────────────────────────────────────────────┐
│                 ShopSmart Sales Dashboard                    │
├─────────────────────────────────────────────────────────────┤
│   ┌─────────────────┐    ┌─────────────────┐                │
│   │  Total Sales    │    │  Total Orders   │                │
│   │  $XXX,XXX.XX    │    │     482         │                │
│   └─────────────────┘    └─────────────────┘                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│            Sales Trend Over Time (Line Chart)                │
│                                                              │
├──────────────────────────┬──────────────────────────────────┤
│   Sales by Category      │   Sales by Region                │
│   (Horizontal Bar)       │   (Horizontal Bar)               │
└──────────────────────────┴──────────────────────────────────┘
```

## Verification Checklist

After implementation, verify:

- [ ] Dashboard loads without errors
- [ ] Total Sales displays in currency format ($X,XXX.XX)
- [ ] Total Orders displays as formatted number
- [ ] Line chart shows 12 months of data
- [ ] Hovering on line chart shows tooltip with exact value
- [ ] Category bar chart shows all 5 categories sorted by value
- [ ] Region bar chart shows all 4 regions sorted by value
- [ ] Hovering on bar charts shows tooltips
- [ ] Dashboard loads within 5 seconds
- [ ] Deployed URL is publicly accessible
- [ ] Dashboard works in Chrome, Firefox, Safari, Edge

## Complexity Tracking

> No constitution violations. Implementation follows all principles.

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| Single file vs modules | Single `app.py` | Simplest for ~100 lines, educational clarity |
| Plotly vs Streamlit native | Plotly | Interactive tooltips required (FR-006) |
| Monthly vs daily trend | Monthly | Sufficient for 482 records, cleaner visualization |

## Dependencies

```text
# requirements.txt
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.18.0
```

## Deployment Notes

**Streamlit Community Cloud Requirements**:
1. Public GitHub repository
2. `requirements.txt` at repository root
3. Main app file: `app.py` (or specify in Streamlit dashboard)
4. Data file must be committed to repository

**Expected URL Format**: `https://<app-name>.streamlit.app`
