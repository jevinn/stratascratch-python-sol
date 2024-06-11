import pandas as pd

df = airbnb_apartments

beds_df = df.groupby('host_id')['n_beds'].sum().reset_index()

beds_df['rank'] = beds_df["n_beds"].rank(ascending=False, method='dense')

beds_df.sort_values('rank')
