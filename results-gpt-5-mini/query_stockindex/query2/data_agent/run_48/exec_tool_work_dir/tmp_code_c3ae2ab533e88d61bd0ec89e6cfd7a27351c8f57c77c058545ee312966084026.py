code = """import json
import pandas as pd
# load the large query result from file path stored in var_call_69rkbZXFvsPGvNgEsBF2DZXV
path = var_call_69rkbZXFvsPGvNgEsBF2DZXV
with open(path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# ensure numeric
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
# filter valid
df = df.dropna(subset=['Open','Close'])
# compute up/down/equal
df['up'] = (df['Close'] > df['Open']).astype(int)
[df['down'] = (df['Close'] < df['Open']).astype(int)"""

env_args = {'var_call_Utml8TGbeS8Cb2IhqfVb0ZwI': ['index_info'], 'var_call_aY1zDKf1dm70elWEKo7rzjXt': ['index_trade'], 'var_call_k5dLsDsojVy7yjhYyIeWDlI5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_69rkbZXFvsPGvNgEsBF2DZXV': 'file_storage/call_69rkbZXFvsPGvNgEsBF2DZXV.json'}

exec(code, env_args)
