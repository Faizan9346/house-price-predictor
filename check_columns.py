import pandas as pd

data = pd.read_csv(r'C:\Users\Dell\Desktop\house_price_predictor\data\housing.csv')
print("Available columns:\n")
print(data.columns.tolist())
