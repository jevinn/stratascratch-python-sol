# https://platform.stratascratch.com/coding/2147-most-expensive-and-cheapest-wine-with-ties?code_type=1

# Import your libraries
import pandas as pd

# Start writing code


df1 = winemag_pd.loc[:,["region_1","variety","price"]].rename(columns={"region_1":"region"})
df2 = winemag_pd.loc[:,["region_2","variety","price"]].rename(columns={"region_2":"region"})

df = pd.concat([df1,df2],axis=0)
df["exp_rank"] = df.groupby("region")["price"].rank(ascending=False,method='dense')
df["chp_rank"] = df.groupby("region")["price"].rank(method='dense')

df_exp = df.loc[df["exp_rank"]==1][:]
df_chp = df.loc[df["chp_rank"]==1][:]

final_df = df_exp.merge(df_chp, left_on=["region","exp_rank"],right_on=["region","chp_rank"], how="inner")
final_df.drop_duplicates(inplace=True)
final_df.loc[:,["region","variety_x","variety_y"]]
