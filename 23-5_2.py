# https://platform.stratascratch.com/coding/9606-differences-in-movie-ratings?code_type=2

# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
non_null_df = nominee_filmography.loc[(nominee_filmography["rating"].notnull()) & (nominee_filmography["role_type"]=="Normal Acting")]
non_null_df['lifetime_avg'] = non_null_df.groupby("name")["rating"].transform(np.mean)
non_null_df["movie_rank"]=non_null_df.groupby("name")["id"].rank(ascending=False)
non_null_df["variance"] = abs(non_null_df["lifetime_avg"] - non_null_df["rating"])
non_null_df.loc[non_null_df["movie_rank"]==2][["name","rating","lifetime_avg","variance"]]
