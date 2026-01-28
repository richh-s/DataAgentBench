code = """import json
import pandas as pd
from datetime import datetime

file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def parse_date(date_str):
    try:
        formats = ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p', '%b %d, %Y at %I:%M %p']
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except:
                pass
        return None
    except:
        return None

df['ParsedDate'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['ParsedDate'])

df_2020 = df[df['ParsedDate'] >= datetime(2020, 1, 1)].copy()

df_2020['Open'] = pd.to_numeric(df_2020['Open'], errors='coerce')
df_2020['High'] = pd.to_numeric(df_2020['High'], errors='coerce')
df_2020['Low'] = pd.to_numeric(df_2020['Low'], errors='coerce')

df_2020 = df_2020.dropna(subset=['Open', 'High', 'Low'])
df_2020 = df_2020[df_2020['Open'] > 0]

df_2020['IntradayVolatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

volatility_by_index = df_2020.groupby('Index')['IntradayVolatility'].agg(['mean', 'count']).reset_index()
volatility_by_index = volatility_by_index.sort_values('mean', ascending=False)

# Create a comprehensive result
results = []
for _, row in volatility_by_index.iterrows():
    results.append({
        'index': row['Index'],
        'avg_volatility': float(row['mean']),
        'trading_days': int(row['count'])
    })

# Get the top result
top_result = results[0]

print('__RESULT__:')
print(json.dumps(top_result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'index': '399001.SZ', 'avg_volatility': 0.01898788110941682, 'trading_days': 158}}

exec(code, env_args)
