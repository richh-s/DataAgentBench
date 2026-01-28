code = """import json
import pandas as pd

# Load the trade data from the stored file
trade_data_file = locals()['var_functions.query_db:10']

# Read the JSON file
with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Ensure numeric columns are properly typed
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])
df['Date'] = pd.to_datetime(df['Date'])

# Calculate up/down/same days
df['Change'] = df['Close'] - df['Open']
df['Day_Type'] = df['Change'].apply(lambda x: 'Up' if x > 0 else ('Down' if x < 0 else 'Same'))

# Group by index and count up/down days
summary = df.groupby('Index').agg({
    'Day_Type': lambda x: x.value_counts().to_dict(),
    'Date': 'count'
}).reset_index()

# Extract counts
summary['Up_Days'] = summary['Day_Type'].apply(lambda x: x.get('Up', 0))
summary['Down_Days'] = summary['Day_Type'].apply(lambda x: x.get('Down', 0))
summary['Total_Days'] = summary['Date']

# Filter for North American indices (NYA, IXIC, GSPTSE)
na_indices = ['NYA', 'IXIC', 'GSPTSE']
na_summary = summary[summary['Index'].isin(na_indices)].copy()

# Find indices with more up days than down days
result = na_summary[na_summary['Up_Days'] > na_summary['Down_Days']]

print('__RESULT__:')
print(json.dumps({
    'north_american_indices': na_summary[['Index', 'Up_Days', 'Down_Days', 'Total_Days']].to_dict('records'),
    'indices_with_more_up_days': result['Index'].tolist()
}, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '2018-01-05 00:00:00', 'Open': '30893.85938', 'High': '30911.00977', 'Low': '30638.5293', 'Close': '30814.64063', 'Adj Close': '30814.64063', 'CloseUSD': '4005.9032819'}, {'Index': 'HSI', 'Date': '2018-01-11 00:00:00', 'Open': '31066.21094', 'High': '31133.17969', 'Low': '30950.07031', 'Close': '31120.39063', 'Adj Close': '31120.39063', 'CloseUSD': '4045.6507819'}, {'Index': 'HSI', 'Date': '2018-01-12 00:00:00', 'Open': '31298.05078', 'High': '31412.53906', 'Low': '31198.35938', 'Close': '31412.53906', 'Adj Close': '31412.53906', 'CloseUSD': '4083.6300778'}, {'Index': 'HSI', 'Date': '2018-01-24 00:00:00', 'Open': '32907.23047', 'High': '33018.71094', 'Low': '32728.50977', 'Close': '32958.69141', 'Adj Close': '32958.69141', 'CloseUSD': '4284.6298833'}, {'Index': 'HSI', 'Date': '2018-01-25 00:00:00', 'Open': '32979.37891', 'High': '32998.05078', 'Low': '32650.2207', 'Close': '32654.44922', 'Adj Close': '32654.44922', 'CloseUSD': '4245.0783986'}, {'Index': 'HSI', 'Date': '2018-01-26 00:00:00', 'Open': '32836.28125', 'High': '33223.57813', 'Low': '32794.12891', 'Close': '33154.12109', 'Adj Close': '33154.12109', 'CloseUSD': '4310.0357417000005'}, {'Index': 'HSI', 'Date': '2018-01-30 00:00:00', 'Open': '32751.7207', 'High': '32976.75', 'Low': '32501.34961', 'Close': '32607.28906', 'Adj Close': '32607.28906', 'CloseUSD': '4238.9475778'}, {'Index': 'HSI', 'Date': '2018-02-02 00:00:00', 'Open': '32569.00977', 'High': '32778.51172', 'Low': '32321.41992', 'Close': '32601.7793', 'Adj Close': '32601.7793', 'CloseUSD': '4238.231309'}, {'Index': 'HSI', 'Date': '2018-02-05 00:00:00', 'Open': '31715.56055', 'High': '32394.86914', 'Low': '31712.01953', 'Close': '32245.2207', 'Adj Close': '32245.2207', 'CloseUSD': '4191.878691000001'}, {'Index': 'HSI', 'Date': '2018-02-20 00:00:00', 'Open': '31165.28906', 'High': '31339.68945', 'Low': '30720.48047', 'Close': '30873.63086', 'Adj Close': '30873.63086', 'CloseUSD': '4013.5720118'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
