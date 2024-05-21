# https://platform.stratascratch.com/coding/10310-class-performance?code_type=2

import pandas as pd 
import numpy as np

df = box_scores
df['total'] = df['assignment1'] + df['assignment2'] + df['assignment3']
ans = df['total'].max() - df['total'].min()
ans
