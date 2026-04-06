CREATE TABLE retail_store_sales (
    transaction_id TEXT,
    customer_id TEXT,
    category TEXT,
    item TEXT,
    price_per_unit REAL,
    quantity INTEGER,
    total_spent REAL,
    payment_method TEXT,
    location TEXT,
    transaction_date DATE,
    discount_applied TEXT
);

CREATE TABLE train (
    row_id INTEGER,
    order_id TEXT,
    order_date DATE,
    ship_date DATE,
    ship_mode TEXT,
    customer_id TEXT,
    customer_name TEXT,
    segment TEXT,
    country TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    region TEXT,
    product_id TEXT,
    category TEXT,
    sub_category TEXT,
    product_name TEXT,
    sales REAL
);