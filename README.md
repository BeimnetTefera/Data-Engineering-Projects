# 🌦️ Weather Data Pipeline

A **data engineering project** that fetches weather data from an API, transforms it into clean records, and stores it inside a SQLite database for querying and reporting.

---

## 📌 Overview
This project demonstrates a simple **ETL pipeline**:

1. **Extract** → Get raw weather data from API
2. **Transform** → Clean & structure the data
3. **Load** → Store into SQLite database
4. **Report** → Query and analyze stored data

---

## 🧰 Tech Stack
- Python 3
- SQLite
- Requests
- JSON
- VS Code + SQLite Extension (optional for viewing DB)

---

## 🗂️ Project Structure
```
weather_pipeline/
│
├── fetch.py        # Extract data from API
├── transform.py    # Clean & structure the data
├── load.py         # Store data into SQLite
├── report.py       # Query and analyze data
│
└── data/
    ├── weather.json   # Raw API response
    └── weather.db     # Final database
```

---

## ⚙️ Setup
Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
```

---

## ▶️ Run The Pipeline
Run scripts in order:

```bash
python fetch.py
python transform.py
python load.py
python report.py
```

---

## 🗃️ Database Output
The pipeline creates:

```
data/weather.db
```

Contains table:

| datetime | temperature |
|--------|------|
| 2026-02-19 00:00 | 4.8 |
| 2026-02-19 01:00 | 4.8 |
| ... | ... |

---

## 🔎 Example SQL Query
```sql
SELECT AVG(temperature) FROM weather;
```

---

## 👤 Author
**Beimnet Tefera**

