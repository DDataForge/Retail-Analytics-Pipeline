--Retail Dataset Insights
-- Total Revenue
SELECT SUM(total_spent) AS total_revenue
FROM retail_store_sales;

-- Top Payment Methods
SELECT payment_method, COUNT(*) AS usage_count
FROM retail_store_sales
GROUP BY payment_method
ORDER BY usage_count DESC;

-- Top Locations by Sales
SELECT location, SUM(total_spent) AS revenue
FROM retail_store_sales
GROUP BY location
ORDER BY revenue DESC;

-- Discount Impact
SELECT discount_applied, AVG(total_spent) AS avg_spending
FROM retail_store_sales
GROUP BY discount_applied;


-- Train Dataset Insights
-- Total Sales
SELECT SUM(sales) AS total_sales
FROM train;

-- Sales by Region
SELECT region, SUM(sales) AS revenue
FROM train
GROUP BY region;

-- Top Customers
SELECT customer_name, SUM(sales) AS total_spent
FROM train
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;

-- Product Performance
SELECT sub_category, SUM(sales) AS total_sales
FROM train
GROUP BY sub_category
ORDER BY total_sales DESC;