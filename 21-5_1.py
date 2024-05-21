# https://platform.stratascratch.com/coding/10172-best-selling-item?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
online_retail.head()
online_retail['month'] = online_retail['invoicedate'].dt.month
online_retail['total_invoice'] = online_retail['quantity'] * online_retail['unitprice']
df = online_retail.groupby(['month', 'description'])['total_invoice'].sum().reset_index()

df['rank'] = df.groupby(['month'])['total_invoice'].rank(ascending=False, method='dense')
top_items_by_month = df[df['rank'] == 1][['month', 'description', 'total_invoice']]
