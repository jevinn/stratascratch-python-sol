# https://platform.stratascratch.com/coding/10017-year-over-year-churn/solutions?code_type=2

# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df = lyft_drivers[lyft_drivers['end_date'].notna()]

df['year_left'] = df['end_date'].dt.year

res = df.groupby('year_left')['index'].nunique().to_frame('total_churn').reset_index()

res['prev_year_churn'] = res['total_churn'].shift(1, fill_value=0)

def change(row):
    if row['total_churn'] > row['prev_year_churn']:
        return 'increase'
        
    if row['total_churn'] < row['prev_year_churn']:
        return 'decrease'
    
    return 'no change'
    
res['inc/dec'] = res.apply(change, axis=1)

res
