# https://platform.stratascratch.com/coding/2146-department-manager-and-employee-salary-comparison/solutions?code_type=2
import pandas as pd

df = employee_o[['department', 'id', 'salary','employee_title', 'manager_id']]
df_employee = df[df['employee_title'] != 'Manager']
df_manager = df[df['employee_title'] == 'Manager']
df_employee = df_employee.rename(columns={'id': 'employee_id'})
df_manager = df_manager.rename(columns={'salary': 'manager_salary'})
df_manager = df_manager[['manager_salary', 'manager_id']]
df_employee['avg_employee_salary'] = df_employee.groupby('department')['salary'].transform('mean')
df_employee['avg_employee_salary'] = df_employee['avg_employee_salary'].round(0)
df_employee = df_employee.rename(columns={'salary': 'employee_salary'})
df_employee = df_employee[['department', 'employee_id', 'employee_salary', 'avg_employee_salary', 'manager_id']]

merged = df_employee.merge(df_manager, on = 'manager_id', how = 'left')
final_result = merged.sort_values(by=['department', 'employee_salary'], ascending=[True, False])
final_result = final_result[['department', 'employee_id', 'employee_salary', 'manager_salary', 'avg_employee_salary']]
