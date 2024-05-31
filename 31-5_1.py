# https://platform.stratascratch.com/coding/2036-lowest-revenue-generated-restaurants/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = doordash_delivery[(doordash_delivery['customer_placed_order_datetime'].dt.month == 5) & (doordash_delivery['customer_placed_order_datetime'].dt.year == 2020)]
df = df.groupby('restaurant_id')['order_total'].sum().reset_index()
df[df['order_total'] <= df['order_total'].quantile(.02)]
