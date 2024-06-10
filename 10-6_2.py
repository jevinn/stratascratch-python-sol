# https://platform.stratascratch.com/coding/10160-rank-guests-based-on-their-ages?code_type=2
# Import your libraries
import pandas as pd

# Start writing code
airbnb_guests['rank']=airbnb_guests["age"].rank(ascending = False)

airbnb_guests.sort_values('rank')[["guest_id","rank"]]
