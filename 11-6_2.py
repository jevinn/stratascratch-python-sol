
import pandas as pd

df = pd.merge(db_employee, db_dept, left_on = 'department_id', right_on = 'id', how = 'left')

df[df["department"]=="marketing"]["salary"].max() - df[df["department"]=="engineering"]["salary"].max()
