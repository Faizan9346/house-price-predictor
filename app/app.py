import pickle
from flask import Flask, render_template, request
import warnings

# Suppress scikit-learn version warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load the trained model
model = pickle.load(open('app/model.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        OverallQual = float(request.form['OverallQual'])
        GrLivArea = float(request.form['GrLivArea'])
        GarageCars = float(request.form['GarageCars'])
        TotalBsmtSF = float(request.form['TotalBsmtSF'])
        YearBuilt = float(request.form['YearBuilt'])
        FullBath = float(request.form['FullBath'])

        # Features in same order as training
        features = [OverallQual, GrLivArea, GarageCars, TotalBsmtSF, YearBuilt, FullBath]

        # Predict price in USD
        price_usd = model.predict([features])[0]

        # Convert to INR
        conversion_rate = 83
        price_inr = price_usd * conversion_rate

        # Format with commas and two decimal places
        formatted_price = f"{price_inr:,.2f}"

        return render_template('index.html', prediction=formatted_price)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
