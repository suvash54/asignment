import pandas as pd
import numpy as np

df = pd.read_csv("imdb.csv")
print("infomation",df.info())
print("descrption",df.describe())
