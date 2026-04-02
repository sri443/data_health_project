# 📊 Data Health Monitor

A lightweight data monitoring system that detects data quality issues and anomalies using Python and Streamlit.

## 🚀 Overview

This project simulates a real-world data pipeline and provides:

- Data ingestion from multiple CSV files
- Data validation (null checks, spike detection)
- Anomaly detection using rolling statistics (Z-score)
- Interactive dashboard for monitoring data health

---

## 🧩 Features

- 📥 Load multiple CSV files automatically
- ⚠️ Detect null values and sudden spikes
- 🚨 Identify anomalies in revenue trends
- 📊 Visualize metrics with Streamlit
- 🧠 Compute a simple data health score

---

## 🏗️ Project Structure

data-health-monitor/
│
├── data/
│ └── raw/ # Generated CSV files
│
├── data_generator.py # Generates sample data
├── validator.py # Validation + anomaly logic
├── app.py # Streamlit dashboard
│
├── requirements.txt
└── README.md

---

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd data-health-monitor
pip install -r requirements.txt
```
---

## ▶️ How to Run

### 1. Generate Sample Data
```bash
python data_generator.py
```
Run this multiple times to simulate incoming data.

### 2. Start Dashboard
```bash
streamlit run app.py
```

---

## How It Works
### 1. Data Loading
- Loads all CSV files from data/raw/
### Validation Checks
- Detects null values in revenue
- Identifies abnormal spikes in user counts
### Anomaly Detection
- Uses rolling mean and standard deviation
- Flags values with high Z-scores
### Health Score
- Starts from 100
- Penalizes:
-- Data issues
-- Detected anomalies

---

## 🧠 Design Decisions

- **Why CSV-based ingestion?**  
  Simulates batch data pipelines commonly used in analytics workflows.

- **Why Z-score for anomaly detection?**  
  Chosen for simplicity and interpretability in early-stage monitoring systems.

- **Why focus on data validation instead of modeling?**  
  In real-world systems, ensuring data quality is critical before any downstream analysis or ML.

- **Why a simple health score?**  
  Provides a quick, interpretable summary for non-technical stakeholders.

---

## 📈 Example Workflow

1. Generate raw data using the data generator
2. System ingests and aggregates CSV files
3. Validation checks identify missing or inconsistent data
4. Anomaly detection flags unusual trends
5. Dashboard displays health score and insights

---

## 🧪 Edge Cases Handled

- Empty data directory (graceful failure)
- Missing values in critical columns
- Division-by-zero in anomaly calculations
- Sudden spikes in user activity

---

## ⚠️ Limitations

- Assumes structured input data with predefined schema
- Uses simple statistical methods (may not detect complex anomalies)
- Batch-based processing (no real-time streaming support)
- Limited scalability for large datasets

---

## Future Improvements
- Support for user-uploaded datasets
- Dynamic schema detection
- Alerts (email/Slack)
- Scheduling with Airflow
- Database integration

---

## 💬 What I Learned

- Importance of data validation before analysis
- Handling edge cases in data pipelines
- Designing simple but effective monitoring systems
- Building user-friendly dashboards for technical insights
