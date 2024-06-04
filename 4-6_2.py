# https://platform.stratascratch.com/coding/2028-new-and-existing-users/solutions?code_type=2

import numpy as np
import pandas as pd
df=fact_events
df['time_id']=df['time_id'].dt.month
df=df[['time_id','user_id']].drop_duplicates()
df['r']=df.groupby('user_id',as_index=False)['time_id'].rank(method='dense')
df['new']=np.where(df['r']==1,1,0)
df['old']=np.where(df['r']==1,0,1)
return df.groupby('time_id',as_index=False).agg(share_of_new_users=('new','mean'),share_of_old_users=('old','mean'))
