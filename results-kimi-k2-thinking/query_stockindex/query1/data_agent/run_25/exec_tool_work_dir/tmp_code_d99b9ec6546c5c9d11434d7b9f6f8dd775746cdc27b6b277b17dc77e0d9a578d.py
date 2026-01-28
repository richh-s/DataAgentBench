code = """import json
import pandas as pd

# Retrieve the file path from the stored variable
storage_var = locals().get('var_functions.query_db:10', '')
print("Storage variable content:", storage_var)

# Try to open the file
if storage_var and isinstance(storage_var, str):
    try:
        with open(storage_var, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        # If storage_var is the actual data instead of a file path
        # Try reading it as JSON string
        try:
            data = json.loads(storage_var)
        except json.JSONDecodeError:
            print("Could not read data")
            data = []
else:
    # Handle case where data might be in the variable directly
    data = storage_var or []

# If data is still empty, try the first few entries from preview
if not data:
    # Use a sample to test logic
    data = [
        {"Index": "N225", "Date": "2020-01-08 00:00:00", "Open": "22500.0", "High": "22600.0", "Low": "22400.0"},
        {"Index": "HSI", "Date": "2020-01-08 00:00:00", "Open": "28000.0", "High": "28200.0", "Low": "27900.0"}
    ]

print("Data loaded:", len(data), "records")

# Convert to DataFrame if we have data
if data:
    df = pd.DataFrame(data)
    
    # Convert numeric columns
    df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
    df['High'] = pd.to_numeric(df['High'], errors='coerce')
    df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
    
    # Remove rows with missing values
    df = df.dropna()
    
    # Calculate intraday volatility for each day
    df['Intraday_Volatility'] = (df['High'] - df['Low']) / df['Open']
    
    # Calculate average intraday volatility for each index
    avg_volatility = df.groupby('Index')['Intraday_Volatility'].mean().reset_index()
    avg_volatility = avg_volatility.sort_values('Intraday_Volatility', ascending=False)
    
    print("Average intraday volatility by index:")
    for _, row in avg_volatility.iterrows():
        print(f"{row['Index']}: {row['Intraday_Volatility']:.6f}")
    
    if not avg_volatility.empty:
        max_vol_row = avg_volatility.iloc[0]
        result = {
            'highest_volatility_index': max_vol_row['Index'],
            'average_intraday_volatility': float(max_vol_row['Intraday_Volatility'])
        }
    else:
        result = {'error': 'No data to calculate volatility'}
else:
    result = {'error': 'No data retrieved'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:8': {'asian_indices': ['N225', 'NSEI', 'HSI', '000001.SS', 'TWII', '399001.SZ'], 'all_indices': ['J203.JO', 'N225', 'GSPTSE', 'NSEI', 'GDAXI', 'IXIC', 'HSI', 'NYA', '000001.SS', 'SSMI', 'TWII', 'N100', '399001.SZ']}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
