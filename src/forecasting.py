from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("data/processed/train_clean.csv")

df['order_date'] = pd.to_datetime(df['order_date'])

# Aggregate daily sales
df = df.groupby('order_date')['sales'].sum().reset_index()

# Feature engineering
df['day'] = range(len(df))

X = df[['day']]
y = df['sales']

model = LinearRegression()
model.fit(X, y)

df['prediction'] = model.predict(X)

print(df.tail())