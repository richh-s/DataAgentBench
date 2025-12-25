code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-7965355165121106327'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns to numeric
cols = ['Open', 'High', 'Low']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with NaN in numeric columns
df.dropna(subset=cols, inplace=True)

# Parse Date
# The date formats seem to be:
# "31 Dec 1986, 00:00"
# "January 02, 1987 at 12:00 AM"
# "1987-01-05 00:00:00"
# "06 Jan 1987, 00:00"
# pd.to_datetime usually handles these well.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter since 2020
df = df[df['Date'] >= '2020-01-01']

# Calculate Intraday Volatility
# (High - Low) / Open
# Handle Open = 0
df = df[df['Open'] > 0]
df['Volatility'] = (df['High'] - df['Low']) / df['Open']

# Group by Index and calculate mean
result = df.groupby('Index')['Volatility'].mean().sort_values(ascending=False)

print("__RESULT__:")
print(result.to_json())"""

env_args = {'var_function-call-3241585435409821147': ['index_info'], 'var_function-call-3241585435409820258': ['index_trade'], 'var_function-call-10704129844478345118': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-10704129844478342071': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-16521182874643957493': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-16521182874643959008': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'J203.JO'}], 'var_function-call-11610007258126017932': [{'Index': 'NYA', 'Date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N225', 'Date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'Date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'Date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'HSI', 'Date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NYA', 'Date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'Date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'SSMI', 'Date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'J203.JO', 'Date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'GDAXI', 'Date': 'September 30, 2016 at 12:00 AM'}], 'var_function-call-323406808569568173': [{'count_star()': '43132'}], 'var_function-call-7965355165121106327': 'file_storage/function-call-7965355165121106327.json'}

exec(code, env_args)
