import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import yfinance as yf
import warnings
warnings.simplefilter("ignore")

# Download historical data for TATA Motors stock from Yahoo Finance (replace with your desired ticker)
ticker = "TATAMOTORS.NS"
start_date = "2023-01-01"
end_date = "2024-10-16"
data = yf.download(ticker, start=start_date, end=end_date)
data.to_csv("tata_motors_data.csv")

# Clean and preprocess the data
df = pd.read_csv("tata_motors_data.csv", parse_dates=['Date'])
df.set_index('Date', inplace=True)
df.dropna(inplace=True)

# Select relevant features and target variable
X = df[['Open', 'High', 'Low', 'Volume']]
y = df['Close']

# Split data into training and testing sets (adjust test size if needed)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=62)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Get the latest day's data
last_day_data = df.iloc[-1]
X_last_day = last_day_data[['Open', 'High', 'Low', 'Volume']]

# Predict the next day's closing price
predicted_price = model.predict(X_last_day.values.reshape(1, -1))

print("Predicted closing price for the next day:", predicted_price[0])

# Plot the last month's stock closing prices
last_month = df.tail(30)
plt.figure(figsize=(12, 6))
plt.plot(last_month['Close'], label='Actual')
last_date = last_month.index[-1].to_pydatetime()
plt.plot([last_date, last_date + pd.Timedelta(days=1)], 
         [last_month['Close'][-1], predicted_price[0]], label='Predicted', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Last Month Stock Closing Prices and Predicted Next Day')
plt.legend()
plt.show()

