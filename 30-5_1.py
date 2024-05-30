# https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=2
import numpy as np
import pandas as pd

df = ms_employee_salary

current_salaries = df.groupby(['id', 'first_name', 'last_name', 'department_id'], as_index=False)['salary'].max()
current_salaries_sorted = current_salaries.sort_values('id')
current_salaries_sorted
