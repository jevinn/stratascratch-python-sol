# https://platform.stratascratch.com/coding/2033-find-the-most-profitable-location?code_type=2# 


# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
signups.head()
signups["signup_duration"] = (signups["signup_stop_date"] - signups["signup_start_date"]).dt.days

avg_signup_duration = signups.groupby("location")["signup_duration"].mean().reset_index()

avg_txn_amt = signups.merge(transactions, on="signup_id").groupby("location")["amt"].mean()

final_df = avg_signup_duration.merge(avg_txn_amt, on="location")

final_df["ratio"] = final_df["amt"] / final_df["signup_duration"]
final_df.sort_values("ratio", ascending=False)
