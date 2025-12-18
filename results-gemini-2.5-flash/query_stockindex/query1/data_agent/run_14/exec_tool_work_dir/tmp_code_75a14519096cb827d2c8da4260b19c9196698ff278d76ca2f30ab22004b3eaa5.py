code = """import pandas as pd
import json

with open(locals()['var_function-call-7143293489580451471'], 'r') as f:
    indextrade_data = json.load(f)

df = pd.DataFrame(indextrade_data)

# Convert relevant columns to numeric and date types
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter data from 2020 onwards
df_filtered = df[df['Date'].dt.year >= 2020]

# Calculate intraday volatility
df_filtered['Volatility'] = (df_filtered['High'] - df_filtered['Low']) / df_filtered['Open']

# Calculate average intraday volatility per index
average_volatility = df_filtered.groupby('Index')['Volatility'].mean().reset_index()

# Find the index with the highest average intraday volatility
highest_volatility_index = average_volatility.sort_values(by='Volatility', ascending=False).iloc[0]

print("__RESULT__:")
print(json.dumps(highest_volatility_index.to_dict()))"""

env_args = {'var_function-call-7143293489580451471': 'file_storage/function-call-7143293489580451471.json'}

exec(code, env_args)
