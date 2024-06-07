# https://platform.stratascratch.com/coding/10163-product-transaction-count?code_type=2
# Import your libraries
import pandas as pd

excel_sql_inventory_data

df = excel_sql_inventory_data.merge(excel_sql_transaction_data, on='product_id',how='inner')
result = df.groupby(['product_id','product_name'])['transaction_id'].size().reset_index()
result.sort_values('product_id')[['product_name','transaction_id']]
