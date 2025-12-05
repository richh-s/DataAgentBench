code = """import json, pandas as pd
from datetime import datetime

# Load the large trade data from file
path = var_call_mYDaz0glnNo3OcfjwPnPWwpE
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Normalize column names
df.columns = [c.strip() for c in df.columns]

# Parse dates that are strings in mixed formats; keep only records from 2020-01-01
def parse_date(s):
    for fmt in ["%Y-%m-%d", "%d %b %Y, %H:%M", "%B %d, %Y at %I:%M %p", "%d %b %Y, %H:%M"]:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    try:
        return pd.to_datetime(s, errors='coerce')
    except Exception:
        return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)

cutoff = datetime(2020,1,1)
df = df[df['Date_parsed'] >= cutoff]

# Ensure numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing or zero Open
df = df.dropna(subset=['Open','High','Low'])
df = df[df['Open'] != 0]

# Compute intraday volatility
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# Identify Asia indices based on Index symbol
asia_indices = ['N225','HSI','000001.SS','399001.SZ','NSEI','TWII','J203.JO','GSPTSE','GDAXI','IXIC','NYA','N100','SSMI']
# Correction: actually Asia are N225, HSI, 000001.SS, 399001.SZ, NSEI, TWII, and Korea (if present)
asia_indices = ['N225','HSI','000001.SS','399001.SZ','NSEI','TWII']

asia_df = df[df['Index'].isin(asia_indices)]

result = asia_df.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)

best_index = result.index[0] if len(result)>0 else None
best_value = float(result.iloc[0]) if len(result)>0 else None

out = {
  'average_intraday_vol_by_index': result.to_dict(),
  'highest_vol_index': best_index,
  'highest_vol_value': best_value
}

res_json = json.dumps(out)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_WWya97AdZpaEXNPpRsI0iykj': ['index_info'], 'var_call_nS0p21vpf05JY0bzqKFXlApm': ['index_trade'], 'var_call_nHda7dMn3RrMHbFWGtUbop8y': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_W2WXlPdkb5ep4hvuZbwMfDha': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_mYDaz0glnNo3OcfjwPnPWwpE': 'file_storage/call_mYDaz0glnNo3OcfjwPnPWwpE.json'}

exec(code, env_args)
