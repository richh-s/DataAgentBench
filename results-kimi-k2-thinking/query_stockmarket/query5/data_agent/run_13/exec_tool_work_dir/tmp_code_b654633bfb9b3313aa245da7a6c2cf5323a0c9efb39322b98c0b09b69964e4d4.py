code = """import json
import os

# Load data for AGMH
agmh_path = locals()['var_functions.query_db:11']
with open(agmh_path, 'r') as f:
    agmh_data = json.load(f)

# Calculate high volatility days for AGMH
high_vol_days = 0
for day in agmh_data:
    try:
        high = float(day['High'])
        low = float(day['Low'])
        if low > 0:
            intraday_range = high - low
            pct_of_low = (intraday_range / low) * 100
            if pct_of_low > 20:
                high_vol_days += 1
    except (ValueError, TypeError):
        continue

print("__RESULT__:")
print(json.dumps({
    'symbol': 'AGMH',
    'total_days': len(agmh_data),
    'high_vol_days': high_vol_days
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nasdaq_capital_symbols': 86, 'available_in_trade_db': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
