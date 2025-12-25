code = """import pandas as pd
import json

# Load the file
file_path = locals()['var_function-call-3867872361740379326']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# Try flexible parsing. The formats are:
# "31 Dec 1986, 00:00"
# "January 02, 1987 at 12:00 AM"
# "1987-01-05 00:00:00"

# Using coercing with a few format attempts or replace strings to make them uniform
# Replacing " at " with " " might help for the second format.
# Removing ", " might help.
# But pd.to_datetime with format='mixed' (pandas 2.0+) is best.
# Let's check if we can use mixed. If this is an older pandas, we might need a custom parser.
# Given I don't know the pandas version, I will try a custom approach if needed, but first try inferred.

# Clean up date strings slightly to help parser
df['Date_clean'] = df['Date'].astype(str).str.replace(' at ', ' ', regex=False).str.replace(',', '', regex=False)

# Try converting
try:
    df['Date'] = pd.to_datetime(df['Date_clean'], format='mixed')
except:
    # Fallback to simple inference
    df['Date'] = pd.to_datetime(df['Date_clean'], infer_datetime_format=True, errors='coerce')

# Drop invalid dates if any
df = df.dropna(subset=['Date'])

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Convert Adj Close to numeric
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Adj Close'])

# Group by Index
indices = df['Index'].unique()
results = []

investment_amount = 1000.0

for idx in indices:
    sub = df[df['Index'] == idx].sort_values('Date')
    
    if sub.empty:
        continue
    
    # Resample to monthly, taking the first available price of each month
    # We can create a period index
    sub['Month'] = sub['Date'].dt.to_period('M')
    monthly = sub.groupby('Month').first().reset_index()
    
    # Calculate DCA
    total_units = 0.0
    total_invested = 0.0
    months_count = 0
    
    # Check start date
    start_date = monthly['Date'].min()
    
    # Calculate
    for _, row in monthly.iterrows():
        price = row['Adj Close']
        if price > 0:
            units = investment_amount / price
            total_units += units
            total_invested += investment_amount
            months_count += 1
            
    if total_units > 0:
        # Final value
        # Get the very last price available in the dataset for this index (not just monthly first)
        last_price = sub.iloc[-1]['Adj Close']
        final_value = total_units * last_price
        
        # Overall Return (percentage)
        overall_return = (final_value - total_invested) / total_invested * 100
        
        results.append({
            'Index': idx,
            'Total Invested': total_invested,
            'Final Value': final_value,
            'Overall Return': overall_return,
            'Start Date': str(start_date.date()),
            'Months': months_count
        })

# Create DataFrame for results
res_df = pd.DataFrame(results)
res_df = res_df.sort_values('Overall Return', ascending=False)

print("__RESULT__:")
print(res_df.to_json(orient='records'))"""

env_args = {'var_function-call-14377125273683390392': ['index_info'], 'var_function-call-14377125273683390217': ['index_trade'], 'var_function-call-11747511180097848628': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-11747511180097848601': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-4064326070736977126': [{'Index': 'J203.JO'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_function-call-4064326070736977595': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-3867872361740379326': 'file_storage/function-call-3867872361740379326.json'}

exec(code, env_args)
