import pickle
import os
import warnings
from flask import Flask, render_template, request

# Suppress version mismatch warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load the trained model
model = pickle.load(open("app/model.pkl", "rb"))

# Create Flask app
app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values
        OverallQual = float(request.form['OverallQual'])
        GrLivArea = float(request.form['GrLivArea'])
        GarageCars = float(request.form['GarageCars'])
        TotalBsmtSF = float(request.form['TotalBsmtSF'])
        YearBuilt = float(request.form['YearBuilt'])
        FullBath = float(request.form['FullBath'])

        # Prepare input for model
        features = [OverallQual, GrLivArea, GarageCars, TotalBsmtSF, YearBuilt, FullBath]
        prediction = model.predict([features])[0]

        # Convert to INR (₹)
        prediction_inr = round(prediction * 84.12, 2)

        return render_template('index.html', prediction=f"₹{prediction_inr:,.2f}")
    
    except Exception as e:
        return f"Error: {e}"

# Run app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
