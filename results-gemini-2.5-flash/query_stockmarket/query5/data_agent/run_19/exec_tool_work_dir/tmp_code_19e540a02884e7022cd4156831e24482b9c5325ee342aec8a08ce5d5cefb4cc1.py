code = """import json
import pandas as pd

# Load the trade data for AGMH
with open(locals()['var_function-call-1407298161823441402'], 'r') as f:
    agmh_trade_data = json.load(f)

# Convert to DataFrame for easier processing
df = pd.DataFrame(agmh_trade_data)

# Convert 'High' and 'Low' to numeric, handling potential errors
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

# Drop rows where conversion failed
df.dropna(subset=['High', 'Low'], inplace=True)

# Calculate if the intraday price range exceeded 20% of the low price
df['condition_met'] = (df['High'] - df['Low']) > (0.20 * df['Low'])

# Count the number of days the condition was met
condition_day_count = df['condition_met'].sum()

print("__RESULT__:")
print(json.dumps({'AGMH': int(condition_day_count)}))"""

env_args = {'var_function-call-1323294415120040832': 'file_storage/function-call-1323294415120040832.json', 'var_function-call-17593339953864697935': 'file_storage/function-call-17593339953864697935.json', 'var_function-call-1407298161823441402': 'file_storage/function-call-1407298161823441402.json'}

exec(code, env_args)
