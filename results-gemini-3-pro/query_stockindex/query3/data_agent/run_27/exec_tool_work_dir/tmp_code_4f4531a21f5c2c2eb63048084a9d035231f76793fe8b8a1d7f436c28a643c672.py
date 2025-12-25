code = """import pandas as pd
import json

# Load data
# Use the file path from the previous step
file_path = locals()['var_function-call-2522961745035833947']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert Adj Close to numeric, coercing errors
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')

# Parse dates. We use dateutil parser implicitly via pd.to_datetime? 
# pd.to_datetime is faster if we let it infer.
# Since formats are mixed, we rely on pandas parsing capabilities.
df['Date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce')

# Filter for dates >= 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01', tz='UTC')]

# Remove rows with NaT or NaN Adj Close
df = df.dropna(subset=['Date', 'Adj Close'])

# Define Country Mapping
country_map = {
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'United States',
    'J203.JO': 'South Africa',
    'N100': 'Europe',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    '000001.SS': 'China',
    '399001.SZ': 'China'
}

results = []

for index_symbol, group in df.groupby('Index'):
    # Sort by date
    group = group.sort_values('Date')
    
    # Group by Month and take the first trading day
    # We use to_period('M') to identify months
    group['YearMonth'] = group['Date'].dt.to_period('M')
    
    # Get the first row for each month (simulating buying at the start)
    monthly_buys = group.groupby('YearMonth').first().reset_index()
    
    # Calculate units purchased (Assuming $1 investment per month)
    monthly_buys['Units'] = 1.0 / monthly_buys['Adj Close']
    
    total_units = monthly_buys['Units'].sum()
    total_invested = len(monthly_buys) # Total dollars invested
    
    if total_invested == 0:
        continue
        
    # Current Value (using the very last closing price in the dataset for this index)
    last_price = group.iloc[-1]['Adj Close']
    total_value = total_units * last_price
    
    # Return ROI
    roi = (total_value - total_invested) / total_invested
    
    results.append({
        'Index': index_symbol,
        'Total Return': roi,
        'Country': country_map.get(index_symbol, 'Unknown')
    })

# Convert to DataFrame
results_df = pd.DataFrame(results)

# Sort by Total Return Descending
top_5 = results_df.sort_values('Total Return', ascending=False).head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-12343112234965767592': ['index_info'], 'var_function-call-12343112234965767797': ['index_trade'], 'var_function-call-529550041605901716': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-529550041605900707': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-14388816773425252252': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-13875376002476427755': [{'Index': 'NYA', 'Date': 'December 31, 1965 at 12:00 AM', 'Close': '528.690002', 'Adj Close': '528.690002', 'CloseUSD': '528.690002'}, {'Index': 'NYA', 'Date': '03 Jan 1966, 00:00', 'Close': '527.210022', 'Adj Close': '527.210022', 'CloseUSD': '527.210022'}, {'Index': 'NYA', 'Date': '1966-01-04 00:00:00', 'Close': '527.840027', 'Adj Close': '527.840027', 'CloseUSD': '527.840027'}, {'Index': 'NYA', 'Date': '05 Jan 1966, 00:00', 'Close': '531.119995', 'Adj Close': '531.119995', 'CloseUSD': '531.119995'}, {'Index': 'NYA', 'Date': 'January 06, 1966 at 12:00 AM', 'Close': '532.070007', 'Adj Close': '532.070007', 'CloseUSD': '532.070007'}], 'var_function-call-13875376002476425216': [{'Index': 'N225', 'Date': '1965-01-05 00:00:00', 'Close': '1257.719971', 'Adj Close': '1257.719971', 'CloseUSD': '12.57719971'}, {'Index': 'N225', 'Date': 'January 06, 1965 at 12:00 AM', 'Close': '1263.98999', 'Adj Close': '1263.98999', 'CloseUSD': '12.6398999'}, {'Index': 'N225', 'Date': '07 Jan 1965, 00:00', 'Close': '1274.27002', 'Adj Close': '1274.27002', 'CloseUSD': '12.7427002'}, {'Index': 'N225', 'Date': '1965-01-08 00:00:00', 'Close': '1286.430054', 'Adj Close': '1286.430054', 'CloseUSD': '12.86430054'}, {'Index': 'N225', 'Date': '1965-01-12 00:00:00', 'Close': '1288.540039', 'Adj Close': '1288.540039', 'CloseUSD': '12.88540039'}], 'var_function-call-2522961745035833947': 'file_storage/function-call-2522961745035833947.json'}

exec(code, env_args)
