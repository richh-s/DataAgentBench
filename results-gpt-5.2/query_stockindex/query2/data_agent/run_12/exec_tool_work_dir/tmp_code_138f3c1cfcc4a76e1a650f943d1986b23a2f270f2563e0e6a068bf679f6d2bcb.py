code = """import json, pandas as pd, re
from datetime import datetime

path = var_call_Mg3beqDW6XupoNfUjPzPYcKE
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def parse_date(s):
    for fmt in ('%Y-%m-%d %H:%M:%S', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p'):
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            pass
    return None

df['dt'] = df['Date'].map(parse_date)
df = df[df['dt'].notna()]
df2018 = df[(df['dt']>=datetime(2018,1,1)) & (df['dt']<datetime(2019,1,1))].copy()
for c in ['Open','Close']:
    df2018[c] = pd.to_numeric(df2018[c], errors='coerce')
df2018 = df2018.dropna(subset=['Open','Close'])

g = df2018.groupby('Index').apply(lambda x: pd.Series({
    'up_days': int((x['Close']>x['Open']).sum()),
    'down_days': int((x['Close']<x['Open']).sum())
})).reset_index()

# Determine which had more up than down
g['more_up_than_down'] = g['up_days'] > g['down_days']
res = g[g['more_up_than_down']].sort_values('Index')[['Index','up_days','down_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_BLVRK0DnUDRCGbNFj2bqiyVV': ['index_info'], 'var_call_0UKCNjrRXdnHRkib9GvT5d1O': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_5YkLjgxKKcVXCLA0hPQK4PsE': [{'Index': 'J203.JO', 'n': '2346'}, {'Index': 'N225', 'n': '13874'}, {'Index': 'GSPTSE', 'n': '10526'}, {'Index': 'NSEI', 'n': '3346'}, {'Index': 'GDAXI', 'n': '8438'}, {'Index': 'HSI', 'n': '8492'}, {'Index': 'NYA', 'n': '13947'}, {'Index': '000001.SS', 'n': '5791'}, {'Index': 'SSMI', 'n': '7671'}, {'Index': 'TWII', 'n': '5869'}, {'Index': 'N100', 'n': '5474'}, {'Index': '399001.SZ', 'n': '5760'}, {'Index': 'IXIC', 'n': '12690'}], 'var_call_pWrbRu43OuWUCkIDSxHNO4Jj': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_Mg3beqDW6XupoNfUjPzPYcKE': 'file_storage/call_Mg3beqDW6XupoNfUjPzPYcKE.json'}

exec(code, env_args)
