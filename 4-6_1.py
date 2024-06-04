# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
instacart_reviews.head()
instacart_stores = instacart_stores.rename(columns = {'id': 'store_id'}) 
df = pd.merge(instacart_reviews, instacart_stores, on = 'store_id', how = 'inner')
df = df[(df['opening_date'].dt.year==2021) & (df['opening_date'].dt.month.isin([7, 8, 9, 10, 11, 12]))]
df['negs'] = np.where(df['score']<5, 1, 0)
df['pos'] = np.where(df['score']>=5, 1, 0)
df_negs = df.groupby('name', as_index = False)['negs'].sum()
df_pos = df.groupby('name', as_index = False)['pos'].sum()
df = pd.merge(df_negs, df_pos, on = 'name', how = 'inner')
df['ratio'] = df['negs']/(df['negs']+df['pos'])
df = df[df['ratio']>0.2]
df['negative_positive_ratio'] = df['negs']/df['pos']
df[['name', 'negative_positive_ratio']]
