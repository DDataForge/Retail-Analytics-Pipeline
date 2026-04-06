from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///retail.db")

# --- OPTIONAL: PostgreSQL (for production-level setup) ---
# engine = create_engine("postgresql://username:password@localhost:5432/retail_db")

# --- OPTIONAL: SQL Server ---
# engine = create_engine("mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server")

def load_to_db():
    retail = pd.read_csv("data/processed/retail_clean.csv")
    train = pd.read_csv("data/processed/train_clean.csv")

    retail.to_sql("retail_store_sales", engine, if_exists="replace", index=False)
    train.to_sql("train", engine, if_exists="replace", index=False)

if __name__ == "__main__":
    load_to_db()