# https://platform.stratascratch.com/coding/10284-popularity-percentage?code_type=2
import pandas as pd
import numpy as np

concatvalues =len(np.unique(np.concatenate([facebook_friends.user1.values,facebook_friends.user2.values])))
revert = facebook_friends.rename(columns= {'user1':'user2','user2':'user1'})
final = pd.concat([facebook_friends, revert],sort = False).drop_duplicates()
result = final.groupby('user1').size().to_frame('count').reset_index()
result['popularity_percent'] = 100*(result['count'] /concatvalues)
result = result[['user1', 'popularity_percent']]
