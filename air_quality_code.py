import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load data from one station (e.g., Aotizhongxin)
file_path = 'data/PRSA_Data_Aotizhongxin_20130301-20170228.csv'
df = pd.read_csv(file_path)

# Combine date columns into a datetime index
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
df.set_index('datetime', inplace=True)

# Drop unnecessary columns
df = df.drop(columns=['No', 'year', 'month', 'day', 'hour'])

# Handle missing values (simple forward fill)
df['PM2.5'] = df['PM2.5'].fillna(method='ffill')

# Basic EDA: Plot PM2.5 over time
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['PM2.5'], label='PM2.5 Concentration')
plt.title('PM2.5 Levels at Aotizhongxin Station')
plt.xlabel('Date')
plt.ylabel('PM2.5 (µg/m³)')
plt.legend()
plt.show()

# Resample to daily means for simpler forecasting
daily_df = df['PM2.5'].resample('D').mean()

# Simple ARIMA forecast (example: order=(1,1,1))
model = ARIMA(daily_df, order=(1, 1, 1))
model_fit = model.fit()

# Forecast next 7 days
forecast = model_fit.forecast(steps=7)
print("7-Day PM2.5 Forecast:")
print(forecast)

# Plot forecast
plt.figure(figsize=(12, 6))
plt.plot(daily_df[-30:], label='Historical PM2.5')
plt.plot(forecast.index, forecast, label='Forecast', color='red')
plt.title('7-Day PM2.5 Forecast at Aotizhongxin')
plt.xlabel('Date')
plt.ylabel('PM2.5 (µg/m³)')
plt.legend()
plt.show()
