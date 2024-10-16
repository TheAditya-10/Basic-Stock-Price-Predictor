# Basic Stock Price Prediction with Linear Regression

**Description:**

This project uses Python libraries like pandas, yfinance, matplotlib, and scikit-learn to:

- Download historical stock data for TATA Motors (TATAMOTORS.NS) from Yahoo Finance.
- Preprocess the data (cleaning, handling missing values, setting index).
- Train a Linear Regression model to predict the closing price based on opening, high, low, and volume.
- Predict the closing price for the next day using the latest day's data.
- Visualize the actual closing prices of the last month and the predicted price for the next day.

**Features:**

- Downloads and preprocesses TATA Motors stock data.
- Trains a Linear Regression model for stock price prediction.
- Generates next-day closing price predictions.
- Creates a visualization of the actual and predicted prices.

**Installation:**

This project requires the following Python libraries:

- pandas
- yfinance
- matplotlib
- scikit-learn

You can install them using pip:

```bash
pip install pandas yfinance matplotlib scikit-learn
