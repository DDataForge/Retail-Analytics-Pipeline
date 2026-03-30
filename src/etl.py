import pandas as pd

def load_data():
    superstore = pd.read_csv("data/raw/superstore.csv")
    dirty = pd.read_csv("data/raw/dirty_retail.csv")
    return superstore, dirty


def clean_data(superstore, dirty):
    # Standardize column names
    superstore.columns = superstore.columns.str.lower().str.replace(" ", "_")
    dirty.columns = dirty.columns.str.lower().str.replace(" ", "_")

    # Handle missing values
    superstore.fillna(method='ffill', inplace=True)
    dirty.dropna(inplace=True)

    return superstore, dirty


def save_data(superstore, dirty):
    superstore.to_csv("data/processed/superstore_clean.csv", index=False)
    dirty.to_csv("data/processed/dirty_clean.csv", index=False)


if __name__ == "__main__":
    s, d = load_data()
    s_clean, d_clean = clean_data(s, d)
    save_data(s_clean, d_clean)