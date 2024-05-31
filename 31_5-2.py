# https://platform.stratascratch.com/coding/10319-monthly-percentage-difference/solutions?code_type=2
import pandas as pd
import numpy as np

df = sf_transactions

df["created_at"] = df['created_at'].dt.to_period('M')

df = df.groupby("created_at")["value"].sum().reset_index().rename(columns={"value":"current_month_rev"})

df["prev_month_rev"] = df["current_month_rev"].shift(1)
df["pct_change"] = (100.0 * (df["current_month_rev"]-df["prev_month_rev"])/df["prev_month_rev"]).round(2)

df[["created_at","pct_change"]]
