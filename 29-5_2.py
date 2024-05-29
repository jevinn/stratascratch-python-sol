# https://platform.stratascratch.com/coding/9708-find-the-variance-and-the-standard-deviation-of-scores-that-have-grade-a/solutions?code_type=2

# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
los_angeles_restaurant_health_inspections.head()

grade_a = los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections.grade=='A']
variance = ((grade_a['score'] - grade_a['score'].mean())**2).mean()
std = np.sqrt(variance)
output = pd.DataFrame({
    'variance': [variance],
    'stdev': [std]
})
