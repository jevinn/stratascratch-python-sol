#  https://platform.stratascratch.com/coding/10162-number-of-acquisitions?code_type=2
# Import your libraries
import pandas as pd

# Start writing code
df = crunchbase_acquisitions

df['quarter'] =  df['acquired_quarter'].dt.to_period('Q')
df.groupby("quarter").size().reset_index().rename(columns={0:'num_acquisitions'}).sort_values(by='num_acquisitions',ascending=False)
