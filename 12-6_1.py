# https://platform.stratascratch.com/coding/2029-the-most-popular-client_id-among-users-using-video-and-voice-calls?code_type=2

# Import your libraries
import pandas as pd, numpy as np

# Start writing code
df = fact_events

df['is_event'] = df['event_type'].apply(lambda x: 1 if x in [ 'video call received', 'video call sent', 'voice call received', 'voice call sent'] else 0)

df['event_avg'] = df.groupby('user_id')['is_event'].transform('mean')

ranked_df = df[df['event_avg']>=0.5].groupby('client_id')['user_id'].count().rank(ascending=False).reset_index()

ranked_df[ranked_df['user_id']==1][['client_id']]
