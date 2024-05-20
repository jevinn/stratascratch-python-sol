# https://platform.stratascratch.com/coding/9917-average-salaries?code_type=1
# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df = employee[['department', 'first_name', 'salary']].copy()
df['avg_sal'] = df.groupby('department').salary.transform('mean')
df
