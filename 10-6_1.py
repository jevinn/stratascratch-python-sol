# https://platform.stratascratch.com/coding/9966-quarterback-with-the-longest-throw?code_type=2
import pandas as pd


df = qbstats_2015_2016

df["lg_num"] = df['lg'].str.extract('(\d+)')

df = df[df["year"]==2016]

df.loc[df['lg_num']==df['lg_num'].max()][["qb","lg_num"]]
