# https://platform.stratascratch.com/coding/10081-find-the-number-of-employees-who-received-the-bonus-and-who-didnt?code_type=2

# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
employee.merge(right=bonus, how='left', left_on='id', right_on='worker_ref_id').assign(has_bonus=lambda x: x['bonus_date'].notna().astype(int)).groupby(by='has_bonus')['id'].nunique()
