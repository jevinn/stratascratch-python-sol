# https://platform.stratascratch.com/coding/9986-find-the-top-5-least-paid-employees-for-each-job-title/solutions?code_type=2
# Import your libraries
import pandas as pd

# Start writing code
df = sf_public_salaries[['employeename', 'jobtitle', 'totalpaybenefits']]
df['rank'] = df.groupby('jobtitle')['totalpaybenefits'].rank(method='dense')

df.sort_values(by=['jobtitle', 'rank'])

df_sorted = df[df['rank']<=5]
df_result = df_sorted.sort_values(by=['jobtitle', 'rank'])
result = df_result[['employeename', 'jobtitle', 'totalpaybenefits']]
result
