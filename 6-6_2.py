# https://platform.stratascratch.com/coding/10013-positive-ad-channels?code_type=2
import pandas as pd
import numpy as np

grouped = uber_advertising.groupby(['advertising_channel']).agg({'customers_acquired':'min','money_spent':'max'}).reset_index()
result = grouped[(grouped['customers_acquired']>1500)].sort_values('money_spent')
result["Rank"] =     result['money_spent'].rank(method="dense")
result[result.Rank==1]['advertising_channel']
