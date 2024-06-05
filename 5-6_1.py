# https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?code_type=2
import pandas as pd

df = pd.merge(left=airbnb_hosts,right=airbnb_units,left_on='host_id',right_on='host_id',how='inner')

df=df.loc[(df["unit_type"]=='Apartment') & (df["age"]<30)]

df.groupby('nationality')["unit_id"].nunique()
