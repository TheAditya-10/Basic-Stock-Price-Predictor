## Linear Regression for Stock Price Prediction (IRCTC.BO)

**Project Description**

This Python script implements a linear regression model to predict the closing price of a stock for the next day. It utilizes historical data downloaded from Yahoo Finance and focuses on the Indian stock IRCTC.BO (Indian Railway Catering and Tourism Corporation Limited). This README serves as a comprehensive guide for understanding the script, its functionalities, and limitations.

**How to Use**

**1. Requirements:**

* Python 3.x
* Libraries: pandas, matplotlib, scikit-learn, yfinance
* Install libraries using `pip install pandas matplotlib scikit-learn yfinance`

**2. Running the Script:**

* Save the code as a Python file (e.g., `stock_prediction.py`).
* Execute the script from the command line: `python stock_prediction.py`

**3. Output:**

* The script outputs the predicted closing price for the next day.
* It generates a plot depicting the actual closing prices for the last month and the predicted price for the next day.

**Code Breakdown**

**1. Data Acquisition and Preprocessing:**

* Lines 3-7 import necessary libraries for data manipulation (pandas), visualization (matplotlib), machine learning (scikit-learn), and financial data download (yfinance).
* Lines 9-11 define the stock ticker symbol (IRCTC.BO), start date (2023-01-01), and end date (2024-10-21) for data retrieval.
* Line 12 downloads historical data from Yahoo Finance using `yf.download`.
* Lines 13-15:
    * Reads the downloaded data into a pandas DataFrame (`df`).
    * Parses the 'Date' column as datetime.
    * Sets 'Date' as the index for easier time-based operations.
    * Drops rows with missing values (`dropna`).
* Lines 16-18:
    * Defines features (independent variables) - 'Open', 'High', 'Low', 'Volume' - representing daily stock opening, highest, lowest, and trading volume prices.
    * Defines the target variable (dependent variable) - 'Close' - representing the daily closing price.

**2. Model Training and Prediction:**

* Lines 19-22:
    * Splits the data into training and testing sets using `train_test_split`. 
    * Training data (80%) is used to train the model, and testing data (20%) is used to evaluate its performance on unseen data.
* Lines 23-24:
    * Creates a Linear Regression model using `LinearRegression` from scikit-learn.
    * Trains the model on the training data (`X_train`, `y_train`).
* Lines 25-28:
    * Retrieves the latest day's data from the DataFrame (`df.iloc[-1]`).
    * Selects relevant features from the latest data for prediction (`X_last_day`).
    * Reshapes the data into a 2D array suitable for model input.
    * Predicts the closing price for the next day using the trained model (`model.predict`).
* Lines 29-30: Prints the predicted closing price for the next day.

**3. Visualization:**

* Lines 31-39:
    * Extracts the closing prices for the last month (`last_month`).
    * Creates a plot with a figure size of 12 inches wide and 6 inches high using `plt.figure`.
    * Plots the actual closing prices of the last month with a label 'Actual'.
    * Retrieves the date of the last closing price (`last_month.index[-1]`).
    * Converts the date to a Python datetime object.
    * Plots a line representing the predicted price for the next day along with the actual closing price on the last day.
    * Sets labels for the x-axis ('Date') and y-axis ('Closing Price').
    * Adds a title 'Last Month Stock Closing Prices and Predicted Next Day'.
    * Includes a legend to differentiate between actual and predicted closing prices.
    * Displays the generated plot using `plt.show`.

**Disclaimer**

Stock prices are highly volatile and influenced by a multitude of factors. This script demonstrates a basic example using linear regression, which may not be the most accurate method for real-world predictions. The results should not be considered financial advice.

**Credits**
- This project uses yahoo finance to get data.
- This project incorporates insights from ChatGPT and Gemini for code generation and best practices.

**Future Improvements**

* Consider employing more sophisticated machine learning models like Random Forest or XGBoost for potentially better prediction accuracy.
* Explore incorporating additional features like technical indicators.
