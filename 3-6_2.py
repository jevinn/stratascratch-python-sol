# https://platform.stratascratch.com/coding/2044-most-senior-junior-employee?code_type=2
# Import your libraries
import pandas as pd
import numpy as np

df = uber_employees

df = df[df['termination_date'].isna()]

df_date = df.groupby("hire_date").size().reset_index().rename(columns={0:"num_emp"}).sort_values("hire_date")

df_date["l_rank"] = df_date["hire_date"].rank()
df_date["s_rank"] = df_date["hire_date"].rank(ascending=False)

final_df = df_date.loc[df_date["l_rank"]==1].merge(df_date.loc[df_date["s_rank"]==1], left_on = "l_rank", right_on="s_rank")

final_df["tenure"] = (final_df["hire_date_y"]-final_df["hire_date_x"]).dt.days

final_df[["num_emp_x","num_emp_y","tenure"]].rename(columns={"num_emp_x":"longest_serving","num_emp_y":"shortest_serving"}) 
