# https://platform.stratascratch.com/coding/2089-cookbook-recipes?code_type=2

import pandas as pd
import numpy as np

series = pd.DataFrame({'page_number': range(max(cookbook_titles.page_number) + 1)})
df = series.merge(cookbook_titles, how='left', on='page_number')
df['right_title'] = df['title'].shift(-1)
df[df['page_number']%2==0]
