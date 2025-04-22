import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load your dataset
data = pd.read_csv('data/housing.csv')

# Use 6 features available in your dataset
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'YearBuilt', 'FullBath']
target = 'SalePrice'

# Prepare the data
X = data[features]
y = data[target]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model to app folder (so Flask app.py can load it)
with open('app/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved at app/model.pkl using 6 features.")
