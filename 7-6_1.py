# https://platform.stratascratch.com/coding/10300-premium-vs-freemium?code_type=2
# Import your libraries
import pandas as pd

# Start writing code
df = ms_download_facts.merge(ms_user_dimension)
df = df.merge(ms_acc_dimension)
df = df.pivot_table(index='date', columns='paying_customer', values='downloads', aggfunc='sum')
df[df['no']>df['yes']].reset_index()
