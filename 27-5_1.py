# https://platform.stratascratch.com/coding/9731-find-all-businesses-whose-lowest-and-highest-inspection-scores-are-different?code_type=2

import pandas as pd
import numpy as np

sf_restaurant_health_violations.head()

df = sf_restaurant_health_violations.loc[:,["business_name","inspection_score"]]

df = df.groupby("business_name")["inspection_score"].agg([np.min,np.max]).reset_index()
df.loc[df["amin"] != df["amax"]].dropna(axis=0)
