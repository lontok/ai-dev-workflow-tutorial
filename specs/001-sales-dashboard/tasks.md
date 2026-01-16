# Tasks: E-Commerce Sales Dashboard

**Input**: Design documents from `/specs/001-sales-dashboard/`
**Prerequisites**: plan.md (required), spec.md (required)

**Tests**: Manual verification only (Phase 1 scope per spec.md)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

Based on plan.md, this is a single-file Streamlit application at repository root:

```
app.py                   # Main Streamlit application
requirements.txt         # Python dependencies
data/sales-data.csv      # Source data (already exists)
```

---

## Phase 1: Setup

**Purpose**: Project initialization and dependency management

- [x] T001 Create `requirements.txt` with streamlit>=1.28.0, pandas>=2.0.0, plotly>=5.18.0
- [x] T002 Create `app.py` with basic Streamlit page configuration (title: "ShopSmart Sales Dashboard", wide layout)

**Checkpoint**: Project structure ready, `streamlit run app.py` launches without errors

---

## Phase 2: Foundational (Data Loading)

**Purpose**: Core data infrastructure that MUST be complete before ANY visualization can be implemented

**CRITICAL**: No user story work can begin until data loading is functional

- [ ] T003 [US1] Implement `load_data()` function with `@st.cache_data` decorator in `app.py`
- [ ] T004 [US1] Add date column parsing in `load_data()` function in `app.py`
- [ ] T005 [US1] Add error handling for missing CSV file with `st.error()` message in `app.py`

**Checkpoint**: Dashboard loads data from `data/sales-data.csv` and displays without errors

---

## Phase 3: User Story 1 - View Key Business Metrics (Priority: P1)

**Goal**: Display Total Sales and Total Orders prominently so executives can quickly assess business performance

**Independent Test**: Load dashboard and verify Total Sales (currency format) and Total Orders (count) are visible at top of screen

### Implementation for User Story 1

- [ ] T006 [US1] Calculate Total Sales as sum of `total_amount` column in `app.py`
- [ ] T007 [US1] Calculate Total Orders as count of rows in `app.py`
- [ ] T008 [US1] Create two-column layout using `st.columns(2)` in `app.py`
- [ ] T009 [US1] Display Total Sales using `st.metric()` with currency formatting (${:,.2f}) in `app.py`
- [ ] T010 [US1] Display Total Orders using `st.metric()` with number formatting in `app.py`

**Checkpoint**: KPI cards display at top of dashboard with correct values and formatting (FR-001, FR-002, SC-001)

---

## Phase 4: User Story 2 - Sales Trends Over Time (Priority: P2)

**Goal**: Show how sales have changed over time so business leaders can understand growth patterns and seasonal trends

**Independent Test**: Verify line chart displays 12 months of data with time on X-axis, sales on Y-axis, and interactive tooltips

### Implementation for User Story 2

- [ ] T011 [US2] Aggregate sales by month using `df.groupby(df['date'].dt.to_period('M'))` in `app.py`
- [ ] T012 [US2] Create Plotly line chart with month on X-axis and sales amount on Y-axis in `app.py`
- [ ] T013 [US2] Configure hover template to show exact sales value for each month in `app.py`
- [ ] T014 [US2] Add clear axis labels and chart title in `app.py`
- [ ] T015 [US2] Display chart using `st.plotly_chart()` with `use_container_width=True` in `app.py`

**Checkpoint**: Line chart shows 12-month trend with interactive tooltips (FR-003, FR-006, SC-002)

---

## Phase 5: User Story 3 - Sales by Category (Priority: P3)

**Goal**: Show sales breakdown by product category so marketing can allocate budget to high-performing segments

**Independent Test**: Verify horizontal bar chart shows all 5 categories sorted by value with interactive tooltips

### Implementation for User Story 3

- [ ] T016 [US3] Aggregate sales by category using `df.groupby('category')['total_amount'].sum()` in `app.py`
- [ ] T017 [US3] Sort category data descending by sales value in `app.py`
- [ ] T018 [US3] Create Plotly horizontal bar chart for category breakdown in `app.py`
- [ ] T019 [US3] Configure hover template to show exact sales value for each category in `app.py`
- [ ] T020 [US3] Add clear labels and chart title in `app.py`

**Checkpoint**: Category bar chart shows all 5 categories sorted by value with tooltips (FR-004, FR-009, SC-003)

---

## Phase 6: User Story 4 - Sales by Region (Priority: P4)

**Goal**: Show sales breakdown by geographic region so regional managers can identify underperforming territories

**Independent Test**: Verify horizontal bar chart shows all 4 regions sorted by value with interactive tooltips

### Implementation for User Story 4

- [ ] T021 [P] [US4] Aggregate sales by region using `df.groupby('region')['total_amount'].sum()` in `app.py`
- [ ] T022 [US4] Sort region data descending by sales value in `app.py`
- [ ] T023 [US4] Create Plotly horizontal bar chart for region breakdown in `app.py`
- [ ] T024 [US4] Configure hover template to show exact sales value for each region in `app.py`
- [ ] T025 [US4] Create side-by-side layout with category chart using `st.columns(2)` in `app.py`

**Checkpoint**: Region bar chart shows all 4 regions sorted by value, displayed alongside category chart (FR-005, FR-010, SC-004)

---

## Phase 7: User Story 5 - Deployment (Priority: P5)

**Goal**: Make dashboard publicly accessible via shareable URL for stakeholder review

**Independent Test**: Access public URL from any browser and verify all visualizations load correctly

### Implementation for User Story 5

- [ ] T026 [US5] Verify all code is committed to GitHub repository
- [ ] T027 [US5] Connect repository to Streamlit Community Cloud
- [ ] T028 [US5] Deploy application and obtain public URL
- [ ] T029 [US5] Test dashboard in Chrome, Firefox, Safari, and Edge browsers

**Checkpoint**: Dashboard accessible via public URL, all features work in multiple browsers (FR-013, FR-014, SC-009, SC-010)

---

## Phase 8: Polish & Verification

**Purpose**: Final validation and quality assurance

- [ ] T030 Verify dashboard loads within 5 seconds (FR-012)
- [ ] T031 Verify all chart labels are clear and professional (FR-011, SC-007)
- [ ] T032 Verify top category and region identifiable within 10 seconds (SC-005)
- [ ] T033 Run complete verification checklist from plan.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational completion
  - US1 (KPIs) → US2 (Trends) → US3 (Category) → US4 (Region) in priority order
  - US3 and US4 bar charts can be developed in parallel after US2
- **Deployment (Phase 7)**: Depends on US1-US4 completion
- **Polish (Phase 8)**: Depends on Deployment completion

### User Story Dependencies

- **User Story 1 (P1)**: Requires data loading (T003-T005)
- **User Story 2 (P2)**: Requires data loading, can start after US1
- **User Story 3 (P3)**: Requires data loading, can start after US2 or in parallel with US4
- **User Story 4 (P4)**: Requires data loading, can start in parallel with US3
- **User Story 5 (P5)**: Requires all visualizations complete

### Parallel Opportunities

- T016-T020 (Category) and T021-T024 (Region) can run in parallel
- T029 (browser testing) can test multiple browsers in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T002)
2. Complete Phase 2: Foundational (T003-T005)
3. Complete Phase 3: User Story 1 (T006-T010)
4. **STOP and VALIDATE**: Test KPI display independently
5. Proceed to next story

### Incremental Delivery

1. Complete Setup + Foundational → Data loading works
2. Add User Story 1 → KPI cards display (MVP!)
3. Add User Story 2 → Trend line chart works
4. Add User Story 3 → Category breakdown works
5. Add User Story 4 → Region breakdown works
6. Add User Story 5 → Deploy to Streamlit Cloud
7. Each story adds value without breaking previous stories

---

## Notes

- All implementation is in single `app.py` file per constitution Principle I (simplicity)
- Plotly charts required for interactive tooltips per constitution Principle II
- Manual testing only for Phase 1 scope
- Commit after each completed user story
- Stop at any checkpoint to validate story independently
