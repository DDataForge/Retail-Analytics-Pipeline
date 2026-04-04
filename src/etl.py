import pandas as pd
import os

# Get absolute base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -----------------------------
# LOAD DATA
# -----------------------------
def load_data():
    retail_path = os.path.join(BASE_DIR, "data/raw/retail_store_sales.csv")
    train_path = os.path.join(BASE_DIR, "data/raw/train.csv")

    retail = pd.read_csv(retail_path)
    train = pd.read_csv(train_path)

    print("Data loaded successfully")
    return retail, train


# -----------------------------
# CLEAN RETAIL DATA
# -----------------------------
def clean_retail(retail):
    retail.columns = retail.columns.str.lower().str.replace(" ", "_")

    # Convert types
    retail['transaction_date'] = pd.to_datetime(
        retail['transaction_date'], errors='coerce'
    )
    retail['price_per_unit'] = pd.to_numeric(retail['price_per_unit'], errors='coerce')
    retail['quantity'] = pd.to_numeric(retail['quantity'], errors='coerce')
    retail['total_spent'] = pd.to_numeric(retail['total_spent'], errors='coerce')

    # Handle missing values
    retail.fillna({
        'discount_applied': 'No',
        'payment_method': 'Unknown'
    }, inplace=True)

    # Drop bad rows
    retail.dropna(inplace=True)

    print("Retail data cleaned")
    return retail


# -----------------------------
# CLEAN TRAIN DATA
# -----------------------------
def clean_train(train):
    train.columns = train.columns.str.lower().str.replace(" ", "_")

    # Convert dates (FIXED ISSUE HERE )
    train['order_date'] = pd.to_datetime(
        train['order_date'], dayfirst=True, errors='coerce'
    )
    train['ship_date'] = pd.to_datetime(
        train['ship_date'], dayfirst=True, errors='coerce'
    )

    # Drop rows where dates failed
    train.dropna(subset=['order_date', 'ship_date'], inplace=True)

    # Fill remaining missing values
    train.fillna(method='ffill', inplace=True)

    print("Train data cleaned")
    return train


# -----------------------------
# SAVE DATA
# -----------------------------
def save_data(retail, train):
    processed_path = os.path.join(BASE_DIR, "data/processed")

    # Create folder if it doesn't exist
    os.makedirs(processed_path, exist_ok=True)

    retail.to_csv(os.path.join(processed_path, "retail_clean.csv"), index=False)
    train.to_csv(os.path.join(processed_path, "train_clean.csv"), index=False)

    print("Cleaned data saved")


# -----------------------------
# MAIN PIPELINE
# -----------------------------
if __name__ == "__main__":
    print("Starting ETL process...")

    r, t = load_data()
    r_clean = clean_retail(r)
    t_clean = clean_train(t)
    save_data(r_clean, t_clean)

    print("ETL pipeline completed successfully!")