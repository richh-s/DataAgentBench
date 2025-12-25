code = """import pandas as pd
import json

# Get file path from the variable
file_path = locals()['var_function-call-6629653509716102951']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# Attempt to handle multiple formats
# Formats seen:
# "31 Dec 1986, 00:00"
# "January 02, 1987 at 12:00 AM"
# "1987-01-05 00:00:00"

# Using pd.to_datetime should work for most common formats. 
# "January 02, 1987 at 12:00 AM" might be tricky for default parser without specific format string sometimes.
# But let's try.
df['Date_Parsed'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter
df_since_2020 = df[df['Date_Parsed'] >= '2020-01-01'].copy()

# Convert numeric
cols = ['Open', 'High', 'Low']
for col in cols:
    df_since_2020[col] = pd.to_numeric(df_since_2020[col], errors='coerce')

df_since_2020 = df_since_2020.dropna(subset=cols)
df_since_2020 = df_since_2020[df_since_2020['Open'] > 0]

# Volatility
df_since_2020['Volatility'] = (df_since_2020['High'] - df_since_2020['Low']) / df_since_2020['Open']

# Average
avg_vol = df_since_2020.groupby('Index')['Volatility'].mean().sort_values(ascending=False)

print("__RESULT__:")
print(json.dumps(avg_vol.to_dict()))"""

env_args = {'var_function-call-8037243058934568575': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-8037243058934568884': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-10151907800084527565': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-7745349874574273670': [{'count_star()': '43132'}], 'var_function-call-6629653509716102951': 'file_storage/function-call-6629653509716102951.json'}

exec(code, env_args)
