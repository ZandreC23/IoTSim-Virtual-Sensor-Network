## 3. Test Cases

### 3.1 Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|--------------|----------------|------------|-------|----------------|---------------|--------|
| TC-001 | FR-01 | Temperature sensor follows daily cycle | Run simulator at 2pm & 4am, record temperature | Temp higher at 2pm (~25°C) than 4am (~18°C) | TBD | TBD |
| TC-002 | FR-02 | Humidity changes ≤5% per reading | Run 10 readings, calculate differences | All ≤5% | TBD | TBD |
| TC-003 | FR-03 | Water flow includes spikes | Run 50 readings, count >50 L/min | ≥2 spikes observed | TBD | TBD |
| TC-004 | FR-04 | Config file settings applied | Set temperature 20-30°C, run simulator, check CSV | All values 20-30°C | TBD | TBD |
| TC-005 | FR-07 | Data saves to CSV | Run simulator 1 min, open CSV | File exists with all columns | TBD | TBD |
| TC-006 | FR-11 | Dashboard updates every 2s | Measure time from CSV write to dashboard display | Delay ≤2s | TBD | TBD |
| TC-007 | FR-15 | Dashboard shows current values | Run simulator, view dashboard | Current temp, humidity, water flow displayed | TBD | TBD |
| TC-008 | FR-16 | Dashboard auto-refreshes | Watch for new data | New data appears automatically | TBD | TBD |

---

### 3.2 Non-Functional Test Cases

| Test Case ID | Requirement ID | Category | Description | Steps | Expected Result | Actual Result | Status |
|--------------|----------------|---------|------------|-------|----------------|---------------|--------|
| NTC-001 | NFR-05 | Security | System runs without internet | Disable WiFi, run simulator | Works normally, all data local | TBD | TBD |
| NTC-002 | NFR-09 | Security | No network connections | Run `netstat -an` | No outbound connections | TBD | TBD |
| NTC-003 | NFR-11 | Performance | 3 sensors at 5s intervals | Run 1 hour, count CSV rows | ≥2,160 rows, CPU <5% | TBD | TBD |
| NTC-004 | NFR-12 | Performance | Dashboard updates within 2s | Measure CSV → dashboard delay | ≤2s | TBD | TBD |
| NTC-005 | NFR-13 | Performance | System startup time | Measure from execution to first reading | ≤5s | TBD | TBD |
| NTC-006 | NFR-04 | Deployability | Runs on Windows & Linux | Test on Windows & Ubuntu VM | Both run without errors | TBD | TBD |
| NTC-007 | NFR-08 | Scalability | Add new sensor type | Add class + config, run simulator | New sensor appears in CSV | TBD | TBD |
| NTC-008 | NFR-01 | Usability | Works in multiple browsers | Open dashboard in Chrome, Firefox, Edge | Dashboard displays correctly | TBD | TBD |

---