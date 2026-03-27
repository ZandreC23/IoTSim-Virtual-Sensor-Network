## 2. Use Case Specifications

### Use Case 1: Configure Simulation

| Field | Content |
|-------|---------|
| Use Case ID | UC-01 |
| Use Case Name | Configure Simulation |
| Actors | IoT Developer, System Administrator, Researcher |
| Description | User modifies simulation parameters such as update frequency, sensor value ranges, and which sensors are enabled |
| Preconditions | `config.json` file exists |
| Postconditions | New settings applied. Next simulation cycle uses updated values |

**Basic Flow:**
1. User opens `config.json` in a text editor  
2. User modifies parameters (e.g., temperature range, update interval)  
3. User saves the file  
4. Simulator detects file change on next cycle  
5. Simulator applies new settings  

**Alternative Flow (File Not Found):**
1. Simulator starts and `config.json` does not exist  
2. System creates default config file with standard values  
3. Use case continues with default settings  

---

### Use Case 2: Generate Temperature Data

| Field | Content |
|-------|---------|
| Use Case ID | UC-02 |
| Use Case Name | Generate Temperature Data |
| Actors | IoT Developer, Researcher |
| Description | System generates temperature readings between 18-25°C following a daily cycle |
| Preconditions | Simulation is running, temperature sensor enabled |
| Postconditions | Temperature reading generated and added to data queue for CSV storage |

**Basic Flow:**
1. Simulator timer reaches generation interval  
2. System calculates current time of day  
3. System calculates temperature using sine wave (peak at 2pm, minimum at 4am)  
4. System assigns unique sensor ID  
5. System adds timestamp in ISO format  
6. Reading passed to Save Data to CSV  

**Alternative Flow (Sensor Disabled):**
1. User disables temperature sensor in config  
2. Simulator skips generation for this sensor type  

---

### Use Case 3: Generate Humidity Data

| Field | Content |
|-------|---------|
| Use Case ID | UC-03 |
| Use Case Name | Generate Humidity Data |
| Actors | IoT Developer, Researcher |
| Description | System generates humidity readings between 30-70% with controlled variation |
| Preconditions | Simulation is running, humidity sensor enabled |
| Postconditions | Humidity reading added to CSV |

**Basic Flow:**
1. Simulator timer reaches generation interval  
2. System generates random humidity value within 30-70%  
3. Change from previous reading ≤ 5%  
4. Sensor ID and timestamp assigned  
5. Reading passed to CSV  

**Alternative Flow (Deterministic Mode):**
1. `deterministic_mode` set to true in config  
2. System uses fixed random seed  
3. Same humidity values generated each run  

---

### Use Case 4: Generate Water Flow Data

| Field | Content |
|-------|---------|
| Use Case ID | UC-04 |
| Use Case Name | Generate Water Flow Data |
| Actors | IoT Developer, Researcher |
| Description | System generates water flow readings between 0-100 L/min with occasional spikes |
| Preconditions | Simulation running, water flow sensor enabled |
| Postconditions | Water flow reading added to CSV |

**Basic Flow:**
1. Timer triggers data generation  
2. Random baseline generated (0-20 L/min)  
3. Check spike counter; if spike → 50-100 L/min  
4. Assign sensor ID and timestamp  
5. Pass reading to CSV  

**Alternative Flow (Spike Occurs):**
1. Spike counter reaches threshold  
2. Generate spike value 50-100 L/min  
3. Counter resets  

---

### Use Case 5: Save Data to CSV

| Field | Content |
|-------|---------|
| Use Case ID | UC-05 |
| Use Case Name | Save Data to CSV |
| Actors | Software Tester, IT Department, Researcher |
| Description | Writes sensor readings to CSV with headers and timestamp |
| Preconditions | Data generated from sensors |
| Postconditions | Reading appended to CSV file |

**Basic Flow:**
1. System receives reading  
2. Check if CSV exists; create if not  
3. Append new row with timestamp, sensor type, ID, value  
4. Flush write buffer to disk  

**Alternative Flow (File Write Error):**
1. File locked or disk full  
2. Log error, skip writing  
3. Simulation continues  

---

### Use Case 6: View Dashboard

| Field | Content |
|-------|---------|
| Use Case ID | UC-06 |
| Use Case Name | View Dashboard |
| Actors | IoT Developer, Product Manager, Academic Instructor |
| Description | Displays live sensor data visualization |
| Preconditions | Dashboard server running, CSV exists |
| Postconditions | Charts display current values, auto-refresh every 2s |

**Basic Flow:**
1. User opens dashboard URL  
2. System reads latest CSV data  
3. Charts for temperature, humidity, water flow displayed  
4. Current values shown  
5. Auto-refresh every 2 seconds  

**Alternative Flow (No Data):**
- CSV empty → dashboard shows "Waiting for data"

---

### Use Case 7: Enable Deterministic Mode

| Field | Content |
|-------|---------|
| Use Case ID | UC-07 |
| Use Case Name | Enable Deterministic Mode |
| Actors | Software Tester |
| Description | Fixes random seed so simulation is repeatable |
| Preconditions | Config file exists |
| Postconditions | `deterministic_mode` enabled, data repeatable |

**Basic Flow:**
1. Open config.json  
2. Set `deterministic_mode: true`  
3. Save file  
4. Simulator applies setting on next cycle  

**Alternative Flow (Disable Mode):**
- `deterministic_mode: false` → random seed uses current time

---

### Use Case 8: Export Data

| Field | Content |
|-------|---------|
| Use Case ID | UC-08 |
| Use Case Name | Export Data |
| Actors | Researcher |
| Description | Export CSV data for external analysis |
| Preconditions | CSV contains readings |
| Postconditions | Data available externally |

**Basic Flow:**
1. Locate CSV  
2. Copy to desired location  
3. Open in Excel/Python/analysis tool  

**Alternative Flow (Large File):**
- CSV > 10,000 rows → use Python with pandas for efficient processing

---