import pandas as pd

# Load your CSV data into a DataFrame
df = pd.read_csv('your_data.csv')  # Replace 'your_data.csv' with the actual file name

# Group the data by category and calculate monthly totals
monthly_totals = df.groupby(['Category', pd.to_datetime(df['Date']).dt.strftime('%Y-%m')])['Amount'].sum().reset_index()

# Rename the columns for clarity
monthly_totals.columns = ['Category', 'Month', 'Total_Spent']

# Print or export the monthly_totals DataFrame for further analysis or reporting
print(monthly_totals)