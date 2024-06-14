# https://platform.stratascratch.com/coding/10303-top-percentile-fraud?code_type=2

import pandas as pd

df = fraud_score
df.groupby('state').apply(lambda x: x[x['fraud_score'] >= x['fraud_score'].quantile(0.95)])
