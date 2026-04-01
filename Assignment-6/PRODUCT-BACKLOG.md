# Product Backlog: IoTSim

## MoSCoW Prioritization
- **Must-have**: Critical for system to function; without these, the product is unusable
- **Should-have**: Important but can be delivered later if necessary
- **Could-have**: Nice to have; adds value but not critical
- **Won't-have**: Out of scope for this release

## Effort Estimates (Story Points)
Using Fibonacci sequence: 1, 2, 3, 5, 8, 13
- **1 point**: Very simple (e.g., 1-2 lines of code, 30 minutes)
- **2 points**: Simple (e.g., 10-20 lines, 1-2 hours)
- **3 points**: Moderate (e.g., 30-50 lines, half day)
- **5 points**: Complex (e.g., 100+ lines, 1-2 days)
- **8+ points**: Too large; needs to be broken down

---

## Product Backlog Table

| Story ID | User Story | MoSCoW Priority | Story Points | Dependencies |
|----------|------------|-----------------|--------------|--------------|
| US-001 | Generate realistic temperature data with daily cycle | Must-have | 3 | None |
| US-002 | Generate realistic humidity data with random variations | Must-have | 2 | None |
| US-003 | Generate water flow data with usage spikes | Must-have | 2 | None |
| US-004 | Configure simulation parameters via config file | Must-have | 3 | None |
| US-006 | Save all sensor readings to CSV file | Must-have | 3 | US-001, US-002, US-003 |
| US-007 | Dashboard with live temperature, humidity, water flow charts | Must-have | 5 | US-006 |
| US-010 | System runs offline with no external dependencies | Must-have | 2 | None |
| US-005 | Unique sensor IDs for tracking | Should-have | 1 | None |
| US-008 | Dashboard shows current values in large numbers | Should-have | 2 | US-007 |
| US-009 | Dashboard auto-refreshes | Should-have | 1 | US-007 |
| US-011 | Add new sensor types without modifying existing code | Could-have | 5 | None |

---

## Justification for Prioritization

### Must-have Stories (7 stories)

| Story | Justification |
|-------|---------------|
| US-001, US-002, US-003 | Core functionality: without sensor data generation, the system has no purpose. Aligns with IoT Developer (S1) success metric: "Can generate 3 different sensor types." |
| US-004 | Configuration is essential for Researcher (S7) and Developer (S1) to customize behavior. Aligns with stakeholder need for flexibility. |
| US-006 | Data storage is critical for Software Tester (S2) and IT Department (S5). Without CSV storage, there is no data to verify or analyze. |
| US-007 | Dashboard is essential for Product Manager (S4) demonstrations and Academic Instructor (S6) teaching. Without visualization, the system is just a script. |
| US-010 | Local-only operation is non-negotiable for IT Department (S5). Without this, the system would not get security approval. |

### Should-have Stories (3 stories)

| Story | Justification |
|-------|---------------|
| US-005 | Unique IDs help with debugging but are not critical for basic functionality. Can be implemented after core sensors work. |
| US-008 | Large numbers improve dashboard usability but charts alone are sufficient for initial demos. |
| US-009 | Auto-refresh enhances user experience but manual refresh can work temporarily. |

### Could-have Stories (1 story)

| Story | Justification |
|-------|---------------|
| US-011 | Adding new sensor types is valuable for Researcher (S7) but requires more complex code. Can be delivered in a later sprint. |

---

## Effort Estimate Justification

| Story | Story Points | Justification |
|-------|--------------|---------------|
| US-001 | 3 | Requires sine wave calculation, time-of-day logic, and unique ID generation. Moderate complexity. |
| US-002 | 2 | Simple random generation with boundary checking. Straightforward. |
| US-003 | 2 | Random baseline with counter-based spikes. Simple logic. |
| US-004 | 3 | JSON parsing, file existence checking, default config generation. Moderate. |
| US-005 | 1 | Simple counter increment and string concatenation. Very easy. |
| US-006 | 3 | CSV writing, header creation, file append logic. Moderate. |
| US-007 | 5 | Most complex: multiple charts, auto-refresh, data parsing. Requires Streamlit learning. |
| US-008 | 2 | Simple metric display with formatting. Straightforward. |
| US-009 | 1 | Built into Streamlit; minimal code. Very easy. |
| US-010 | 2 | Ensuring no external calls; verification. Straightforward. |
| US-011 | 5 | Requires class inheritance design, factory pattern. Complex. |

---

## Backlog Summary

| Priority | Count | Total Story Points |
|----------|-------|-------------------|
| Must-have | 7 | 21 |
| Should-have | 3 | 4 |
| Could-have | 1 | 5 |
| **Total** | **11** | **30** |