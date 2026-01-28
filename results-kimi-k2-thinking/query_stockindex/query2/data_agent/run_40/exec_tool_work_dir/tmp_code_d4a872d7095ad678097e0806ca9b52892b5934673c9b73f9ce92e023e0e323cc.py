code = """import json

# Read the full result from the file path stored in var_functions.query_db:8
with open(var_functions.query_db:8, 'r') as f:
    trade_data = json.load(f)

# Filter for North American indices: NYA (NYSE), IXIC (NASDAQ), GSPTSE (TSX)
na_indices = ['NYA', 'IXIC', 'GSPTSE']

# Process the data to count up and down days for 2018
results = {}

for index in na_indices:
    # Filter data for this index
    index_data = [row for row in trade_data if row['Index'] == index]
    
    up_days = 0
    down_days = 0
    
    # Count up and down days
    for row in index_data:
        open_price = float(row['Open'])
        close_price = float(row['Close'])
        
        if close_price > open_price:
            up_days += 1
        elif close_price < open_price:
            down_days += 1
    
    results[index] = {
        'up_days': up_days,
        'down_days': down_days,
        'total_days': up_days + down_days
    }

# Prepare result string
result_str = "_RESULT_: 
"
result_str += json.dumps(results, indent=2)

print("__RESULT__:")
print(result_str)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
