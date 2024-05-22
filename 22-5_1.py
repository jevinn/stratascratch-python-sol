# https://platform.stratascratch.com/coding/10297-comments-distribution?code_type=2

import pandas as pd
import numpy as np

df = fb_users.merge(fb_comments, how='inner', left_on='id', right_on='user_id')
df = df[['id', 'joined_at', 'created_at']]
df = df[df['created_at']>df['joined_at']]
df = df[df['joined_at'].dt.year.isin([2018, 2019, 2020])]
df = df[df['created_at'].dt.year == 2020]
df = df[df['created_at'].dt.month == 1]
df =df.groupby('id')['created_at'].count().reset_index()
df.groupby('created_at').count().reset_index()
