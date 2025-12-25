code = """import pandas as pd
import json
import os
from dateutil import parser

# Load data
file_path = locals()['var_function-call-15274514796049911276']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# Using dateutil.parser.parse might be slow for many rows but handles mixed formats well. 
# However, pandas to_datetime is faster. Let's try to_datetime with mixed format support if available or just let it infer.
# Since the dataset is 43k rows, dateutil is acceptable.
# But let's try pd.to_datetime first as it is vectorized.
# The formats are quite distinct. Let's try to normalize.

def parse_date(date_str):
    try:
        return parser.parse(date_str)
    except:
        return pd.NaT

# Apply parsing. Doing it via list comprehension might be faster than apply for mixed types if pd.to_datetime fails.
# Let's use pd.to_datetime(..., format='mixed') available in newer pandas, but I am not sure of the version.
# Let's fallback to dateutil if needed.
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed') 
except:
    # Manual parsing if format='mixed' is not available or fails
    df['Date'] = df['Date'].apply(parse_date)

# Filter for >= 2020-01-01
df = df[df['Date'] >= pd.Timestamp('2020-01-01')]

# Calculate Volatility
# Ensure numeric types
cols = ['Open', 'High', 'Low']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=cols)
df = df[df['Open'] > 0] # Avoid division by zero

df['Volatility'] = (df['High'] - df['Low']) / df['Open']

# Average volatility by Index
avg_volatility = df.groupby('Index')['Volatility'].mean().sort_values(ascending=False)

print("__RESULT__:")
print(json.dumps(avg_volatility.to_dict()))"""

env_args = {'var_function-call-7355997390205926452': ['index_info'], 'var_function-call-7355997390205925087': ['index_trade'], 'var_function-call-920041864904650870': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-920041864904650849': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-3570259335682730614': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-15999375070978996061': [{'Date': 'September 30, 2019 at 12:00 AM'}, {'Date': 'September 30, 2016 at 12:00 AM'}, {'Date': 'September 30, 1997 at 12:00 AM'}, {'Date': 'September 30, 1993 at 12:00 AM'}, {'Date': 'September 29, 2016 at 12:00 AM'}], 'var_function-call-10305767931711700694': [{'count_star()': '43132'}], 'var_function-call-15274514796049911276': 'file_storage/function-call-15274514796049911276.json'}

exec(code, env_args)
