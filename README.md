# Retail-Analytics-Pipeline

End-to-end retail analytics pipeline using SQL, Python, and machine learning for sales forecasting and customer insights.

---

## Overview

This project simulates a real-world retail data environment by integrating multiple datasets, building a complete ETL pipeline, performing SQL-based analysis, and generating business insights through data visualization and machine learning.

The pipeline processes raw retail transaction and order data into clean, analysis-ready datasets, enabling data-driven decision-making.

---

## Objectives

- Build a **data pipeline (ETL)** for retail datasets  
- Perform **data cleaning and transformation** using Python  
- Store and query data using **SQL (SQLite/PostgreSQL/SQL Server)**  
- Conduct **exploratory data analysis (EDA)**  
- Generate **business insights**  
- Implement **sales forecasting using machine learning**  
- Create a **dashboard for stakeholders (Power BI)**  

---

## Project Architecture
Raw Data → ETL Pipeline → Cleaned Data → SQL Database → Analysis → ML Model → Dashboard

---

## 📁 Project Structure
Retail-Analytics-Pipeline/
│
├── data/
│ ├── raw/ # Original datasets
│ └── processed/ # Cleaned datasets
│
├── notebooks/ # Jupyter notebooks (EDA)
│
├── sql/ # SQL schema and analysis queries
│
├── src/ # Python scripts (ETL, DB, ML)
│
├── dashboard/ # Power BI dashboard file
│
├── run_pipeline.py # Master pipeline script
├── README.md
├── requirements.txt


---

## Tech Stack

- **Python**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **SQL**: SQLite (extendable to PostgreSQL / SQL Server)  
- **Data Engineering**: ETL pipeline design  
- **Machine Learning**: Linear Regression (sales forecasting)  
- **Visualization**: Power BI / Matplotlib / Seaborn  
- **Version Control**: Git & GitHub  

---

## Datasets Used

### 1. Retail Store Sales Dataset
- Transaction-level data  
- Includes: customers, products, payment methods, locations  

### 2. Superstore (Train Dataset)
- Order-level data  
- Includes: sales, region, product categories, customers  


---

## ETL Pipeline

The ETL pipeline:
- Loads raw CSV data  
- Cleans and standardizes column names  
- Handles missing values  
- Converts data types (dates, numeric fields)  
- Outputs clean datasets for analysis  

Run:
```bash
python src/etl.py
