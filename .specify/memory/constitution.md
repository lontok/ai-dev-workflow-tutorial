<!--
SYNC IMPACT REPORT
==================
Version change: 1.0.0 → 1.1.0 (MINOR - expanded visualization guidance)

Modified principles:
- "I. Simplicity First" → "I. Simple & Readable Code" (merged with principle II)
- "III. User-Friendly Visualizations" → "II. User-Friendly Interactive Visualizations" (expanded)

Added sections:
- Interactive tooltips requirement in visualization principle

Removed sections:
- Separate "Clear & Readable Code" principle (merged into principle I)
- Constraint against additional visualization libraries

Templates requiring updates:
- .specify/templates/plan-template.md: ✅ Compatible
- .specify/templates/spec-template.md: ✅ Compatible
- .specify/templates/tasks-template.md: ✅ Compatible

Follow-up TODOs: None
-->

# E-Commerce Analytics Dashboard Constitution

## Core Principles

### I. Simple & Readable Code

Code MUST be simple, clear, and written for human comprehension first.

- **YAGNI Enforcement**: Features MUST NOT be added unless explicitly required by the specification
- **Single Responsibility**: Each component, function, and module MUST do one thing well
- **Descriptive Naming**: Variables, functions, and files MUST have self-documenting names
- **Logical Organization**: Code MUST be organized in a predictable, intuitive structure
- **Appropriate Comments**: Comments explain "why," not "what" — the code itself explains "what"
- **Consistent Formatting**: All code MUST follow consistent indentation, spacing, and style

**Rationale**: This is an educational project. Code clarity enables learning and reduces confusion for students following the tutorial.

### II. User-Friendly Interactive Visualizations

All dashboard visualizations MUST prioritize clarity, usability, and interactivity.

- **Intuitive Layout**: Dashboard elements MUST be arranged logically (KPIs at top, trends below, breakdowns at bottom)
- **Clear Labels**: All charts, axes, and metrics MUST have descriptive, human-readable labels
- **Appropriate Chart Types**: Visualization type MUST match the data story (line for trends, bar for comparisons)
- **Interactive Tooltips**: Charts MUST display exact values when users hover over data points
- **Consistent Styling**: Colors, fonts, and spacing MUST be consistent across all visualizations

**Rationale**: The dashboard teaches data visualization best practices. Users should immediately understand what each visualization conveys and be able to explore data interactively.

### III. Python Best Practices

All Python code MUST follow established community standards.

- **PEP 8 Compliance**: Code MUST follow PEP 8 style guidelines
- **Type Hints**: Functions SHOULD include type hints for parameters and return values
- **Virtual Environment**: Project MUST use a virtual environment for dependency isolation
- **Requirements Management**: Dependencies MUST be explicitly declared in requirements.txt

**Rationale**: Following Python conventions prepares students for professional development environments and enables consistent code quality.

## Technology Standards

This project uses the following technology stack:

| Component | Technology | Version |
|-----------|------------|---------|
| Language | Python | 3.11+ |
| Web Framework | Streamlit | Latest stable |
| Data Processing | Pandas | Latest stable |
| Visualization | Plotly | Latest stable |
| Package Manager | uv | Latest stable |
| Version Control | Git | Latest stable |

## Development Workflow

All development MUST follow this workflow:

1. **Specification First**: Requirements MUST be documented before implementation begins
2. **Task Breakdown**: Work MUST be broken into discrete, trackable tasks
3. **Incremental Commits**: Changes MUST be committed frequently with descriptive messages
4. **Traceability**: Commits MUST reference the relevant Jira issue (e.g., `ECOM-1: description`)

**Quality Gates**:
- Code MUST run without errors before committing
- Dashboard MUST display correctly in the browser before pushing
- All data visualizations MUST accurately represent the underlying data

## Governance

This constitution establishes the non-negotiable standards for the E-Commerce Analytics Dashboard project.

**Amendment Process**:
1. Proposed changes MUST be documented with rationale
2. Changes MUST be reviewed for impact on existing code and documentation
3. Version number MUST be updated according to semantic versioning:
   - MAJOR: Principle removals or fundamental redefinitions
   - MINOR: New principles or materially expanded guidance
   - PATCH: Clarifications, wording improvements, typo fixes

**Compliance**:
- All code contributions MUST align with the Core Principles
- Violations MUST be documented and justified in the Complexity Tracking section of the implementation plan
- The constitution supersedes conflicting guidance in other project documents

**Version**: 1.1.0 | **Ratified**: 2026-01-15 | **Last Amended**: 2026-01-15
