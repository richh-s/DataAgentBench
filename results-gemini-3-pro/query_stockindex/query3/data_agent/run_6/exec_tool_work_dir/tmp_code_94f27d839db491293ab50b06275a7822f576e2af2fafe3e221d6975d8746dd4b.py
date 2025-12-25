code = """import json
import pandas as pd

# Load data again (or use previous if persistence allowed, but usually separate calls need reload or careful management. 
# The system says "All previous tool results are available as variables." so I can use `var_function-call-4359623576049279886` again.
# But I need to parse dates again unless I serialized the DF. I printed the result JSON, not the DF.
# So I need to reload.

with open(locals()['var_function-call-4359623576049279886'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Minimal parsing for check
df = df[df['Index'].isin(['IXIC', 'NSEI', '399001.SZ', 'GDAXI', 'TWII'])]
# I'll just check the string dates min value roughly or parse properly
from dateutil import parser
def parse_dt(x):
    try:
        return parser.parse(x)
    except:
        return pd.NaT

df['Date'] = df['Date'].apply(parse_dt)
df = df.dropna(subset=['Date'])
df = df[df['Date'] >= '2000-01-01']

stats = df.groupby('Index')['Date'].min()
print("__RESULT__:")
print(stats.astype(str).to_json())"""

env_args = {'var_function-call-2913934071525250979': ['index_info'], 'var_function-call-2913934071525250614': ['index_trade'], 'var_function-call-3711871085042799337': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3711871085042802130': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-63921800962576420': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-63921800962578793': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-6037072348525956933': [{'count_star()': '104224'}], 'var_function-call-4359623576049279886': 'file_storage/function-call-4359623576049279886.json', 'var_function-call-17823732982549569091': [{'Index': 'IXIC', 'Country': 'USA', 'Return': 3.8269431542}, {'Index': 'NSEI', 'Country': 'India', 'Return': 1.3584273446}, {'Index': '399001.SZ', 'Country': 'China', 'Return': 1.3474875235}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 1.3470287159}, {'Index': 'TWII', 'Country': 'Taiwan', 'Return': 1.2982076187}]}

exec(code, env_args)
