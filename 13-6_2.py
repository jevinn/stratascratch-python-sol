# https://platform.stratascratch.com/coding/2012-viewers-turned-streamers?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df= twitch_sessions

df['session_rank'] = df.groupby('user_id')['session_start'].transform('rank')

df_first = df[(df['session_type']=='viewer')&(df['session_rank']==1)]

final = df_first.merge(df[df['session_type']=='streamer'], left_on = 'user_id', right_on='user_id')

final.groupby('user_id')['session_id_y'].count()
