# https://platform.stratascratch.com/coding/10171-find-the-genre-of-the-person-with-the-most-number-of-oscar-winnings/solutions?code_type=2
# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df=oscar_nominees.merge(nominee_information,left_on='nominee',right_on='name').sort_values(by='nominee').query('winner==1')

df.groupby('top_genre')['nominee'].count().reset_index().sort_values(by='nominee',ascending=False).head(1)[['top_genre']]
