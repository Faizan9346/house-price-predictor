# 🏡 House Price Predictor – A Smart ML Web App

Hi there! 👋  
This is a machine learning project I built that predicts the **price of a house** based on a few key features. Think of it like a tiny real estate assistant — trained on real data — and wrapped in a clean, responsive web interface.

The goal?  
To learn by doing — and create something that's practical, easy to use, and deployable. All powered by Python 🐍 + Flask 🔥 + ML 🧠

---

## 🌍 Live Demo

🟢 **Check it out here** → [https://house-price-predictor-p01t.onrender.com](https://house-price-predictor-p01t.onrender.com)

Give it a spin — try different inputs and see the predictions in **Indian Rupees (₹)**!

---

## 🛠 What I Used

- **Python & Flask** for the web backend
- **scikit-learn** to train a simple Linear Regression model
- **pandas + NumPy** for data wrangling
- **Bootstrap** to make the form user-friendly
- **Matplotlib + Seaborn** for data visualization

---

## 💡 How It Works

- You enter 6 house-related details (like size, year built, bathrooms)
- The model makes a prediction based on historical housing data
- It then displays the estimated price in ₹ (formatted and clean)

Behind the scenes, the model was trained on the **Ames Housing Dataset**, which is a great alternative to the more commonly used Boston dataset.

---

## 📊 Visuals & EDA

Before building the model, I explored the dataset a bit. Here are a few insights I visualized:

### 🏠 Sale Price Distribution
![SalePrice Distribution](app/static/saleprice_distribution.png)

### 📏 Living Area vs Price
![GrLivArea vs SalePrice](app/static/grlivarea_vs_saleprice.png)

### 🔥 Feature Correlation Heatmap
![Correlation Heatmap](app/static/correlation_heatmap.png)

---

## ⚙️ Run It Yourself

Wanna run it locally? Here's how:

```bash
# Step 1: Clone the project
git clone https://github.com/Faizan9346/house-price-predictor.git
cd house-price-predictor

# Step 2: Create a virtual environment
python -m venv venv
venv\Scripts\activate  # for Windows

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Train the model
python train_model.py

# Step 5: Run the app
python app/app.py
