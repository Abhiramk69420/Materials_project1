# Materials Science Project

## Overview

This project uses a Raspberry Pi and Python to investigate how different materials respond to temperature changes when exposed to the same heat source.

The goal is to collect temperature data, analyze heating rates, compare thermal behavior between materials, and determine which materials transfer and retain heat most effectively.

This project combines concepts from:

- Materials Science
- Physics (Heat Transfer)
- Data Analysis
- Python Programming
- Raspberry Pi Sensor Integration

---

## Research Question

How do different materials respond to the same heating conditions, and which material heats up the fastest?

---

## Project Objectives

- Measure temperature changes over time for multiple materials.
- Calculate heating rates.
- Compare thermal performance between materials.
- Visualize experimental data using graphs.
- Rank materials based on their thermal response.

---

## Hardware Used

- Raspberry Pi 4
- Temperature Sensor
- Heat Source
- Test Materials (Metal samples)

---

## Software Used

- Python 3
- CSV Data Storage
- Matplotlib
- NumPy
- Raspberry Pi OS

---

# Project Structure

```
Materials_Project/
│
├── README.md
│
├── src/
│   ├── test_temp.py
│   ├── heating_rate.py
│   ├── compare.py
│   ├── graph.py
│   ├── error_analysis.py
│   ├── rank_materials.py
│   └── trial_statistics.py
│
└── old_data/
```

---

# Script Descriptions

## test_temp.py

### Purpose

Collects temperature readings from the sensor and stores them for analysis.

### What it does

- Reads temperature values from the sensor.
- Records temperatures at regular time intervals.
- Saves data into CSV files.
- Creates a separate data file for each material trial.

### Output

Example:

```
Time (s), Temperature (°C)
0,25.1
5,26.3
10,27.7
...
```

---

## graph.py

### Purpose

Visualizes experimental temperature data.

### What it does

- Reads CSV temperature files.
- Generates temperature vs. time graphs.
- Allows visual comparison of heating behavior.

### Output

- Line graph showing temperature increase over time.

---

## heating_rate.py

### Purpose

Calculates how quickly a material heats up.

### What it does

- Uses temperature and time data.
- Computes the rate of temperature change.

### Formula

```
Heating Rate =
(Change in Temperature) / (Change in Time)
```

### Output

Example:

```
Aluminum: 0.42 °C/s
Steel: 0.31 °C/s
Copper: 0.48 °C/s
```

---

## compare.py

### Purpose

Compares multiple materials side-by-side.

### What it does

- Loads data from multiple experiments.
- Displays results on a single graph.
- Makes differences easier to identify.

### Output

- Multi-material comparison graph.
- Summary statistics.

---

## trial_statistics.py

### Purpose

Analyzes repeatability and consistency.

### What it does

- Calculates averages from multiple trials.
- Computes statistical values.
- Reduces the effect of experimental error.

### Output

Example:

```
Material: Aluminum

Average Heating Rate: 0.43 °C/s
Maximum Temperature: 52.4 °C
```

---

## error_analysis.py

### Purpose

Evaluates experimental uncertainty.

### What it does

- Compares multiple trials.
- Calculates variation between measurements.
- Identifies possible experimental errors.

### Sources of Error

- Sensor precision limitations
- Uneven heating
- Environmental temperature changes
- Material placement differences

---

## rank_materials.py

### Purpose

Ranks materials based on performance.

### What it does

- Uses heating rate calculations.
- Uses average trial statistics.
- Assigns a score to each material.
- Produces a final ranking.

### Example Output

```
1. Copper
2. Aluminum
3. Steel
4. Brass
```

---

# Experimental Procedure

Follow these steps for every material tested.

## Step 1: Prepare Material

- Select the material sample.
- Place the temperature sensor consistently.
- Record the material name.

---

## Step 2: Start Data Collection

Run:

```bash
python test_temp.py
```

The script will begin recording temperature data.

---

## Step 3: Apply Heat

- Expose the material to the heat source.
- Keep heating conditions consistent for every trial.
- Do not move the sensor during testing.

---

## Step 4: Save Trial Data

Allow the experiment to finish.

The data will automatically be stored in a CSV file.

Example:

```
aluminum_trial1.csv
steel_trial1.csv
```

---

## Step 5: Generate Graph

Run:

```bash
python graph.py
```

This creates a temperature vs. time graph.

---

## Step 6: Calculate Heating Rate

Run:

```bash
python heating_rate.py
```

The script calculates how quickly the material heats up.

---

## Step 7: Repeat Trials

Perform at least three trials for each material.

Example:

```
aluminum_trial1.csv
aluminum_trial2.csv
aluminum_trial3.csv
```

---

## Step 8: Calculate Statistics

Run:

```bash
python trial_statistics.py
```

This generates averages and summary statistics.

---

## Step 9: Analyze Error

Run:

```bash
python error_analysis.py
```

Review uncertainty and variation between trials.

---

## Step 10: Rank Materials

Run:

```bash
python rank_materials.py
```

The final ranking will be generated.

---

# Future Improvements

- Test additional materials.
- Add cooling-rate analysis.
- Automate report generation.
- Create a live dashboard.
- Add real-time graph updates.
- Compare both heating and cooling performance.

---

# Author

Abhiram

Developed as an independent Materials Science and Raspberry Pi research project investigating thermal behavior in engineering materials.

