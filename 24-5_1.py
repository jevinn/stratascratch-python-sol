# https://platform.stratascratch.com/coding/9898-unique-salaries?code_type=2

# Import your libraries
import pandas as pd
import numpy as np
twitter_employee["salary_rank"] = twitter_employee.groupby("department")["salary"].rank(ascending=False,method = "dense")
dept_salary = twitter_employee[["department","salary","salary_rank"]]
dept_salary = dept_salary.loc[dept_salary["salary_rank"]<4].sort_values(["department","salary"],ascending=[True,False]).drop_duplicates()

dept_salary.drop("salary_rank",axis=1)
