# https://platform.stratascratch.com/coding/10046-top-5-states-with-5-star-businesses?code_type=2

import pandas as pd


df = yelp_business

df = df[df['stars']==5].groupby('state')['business_id'].count().reset_index().rename(columns={'business_id':'num_biz'})


df['rank'] = df['num_biz'].rank(ascending=False)

df[df['rank']<=5][['state','num_biz']]
