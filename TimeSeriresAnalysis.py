import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
df = pd.read_csv('stock.csv')

# Step 2: Convert 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Sort data by date (optional but good practice)
df = df.sort_values('Date')

# Step 4: Plot the closing price over time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Close'], marker='o')

plt.title('Stock Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()
