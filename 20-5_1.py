#https://platform.stratascratch.com/coding/10350-algorithm-performance?code_type=1

# Import your libraries
import pandas as pd

# Start writing code
fb_search_events.head()
df=fb_search_events

def calculate_rating(c):
    if c['clicked']==0:
        return 1
    elif c['clicked']==1 and c['search_results_position']>3:
        return 2
    else:
        return 3
        
df['ratings']=df.apply(lambda row: calculate_rating(row), axis=1)
df.groupby('search_id').ratings.max().reset_index()
