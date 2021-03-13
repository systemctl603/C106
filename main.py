import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")

coffee = np.array(df["Coffee in ml"])
sleep = np.array(df["sleep in hours"])

correlation = np.corrcoef(coffee, sleep)
print(f"Correlation between coffee and sleep: {correlation[0, 1]}")