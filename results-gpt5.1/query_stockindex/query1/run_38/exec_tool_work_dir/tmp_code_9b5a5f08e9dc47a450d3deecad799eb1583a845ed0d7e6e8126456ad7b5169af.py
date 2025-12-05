code = """import json, pandas as pd
from datetime import datetime

path = var_call_Mn7IoMavk9xNS3KQb4meY6cv
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

def parse_date(s):
    for fmt in ['%Y-%m-%d','%d %b %Y, %H:%M','%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)
df = df[df['Date_parsed'] >= pd.Timestamp('2020-01-01')]

asian_indices = ['HSI','N225','000001.SS','399001.SZ','SSEC','SZI','^NSEI','^BSESN','KS11','TWII']

asia_df = df[df['Index'].isin(asian_indices)].copy()
asia_df['volatility'] = (asia_df['High'] - asia_df['Low']) / asia_df['Open']
result = asia_df.groupby('Index')['volatility'].mean().sort_values(ascending=False).reset_index()

answer = {
    'ranking': result.to_dict(orient='records'),
    'top_index': result.iloc[0]['Index'] if len(result)>0 else None,
    'top_avg_volatility': float(result.iloc[0]['volatility']) if len(result)>0 else None
}

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_lVgIzfMwaxWr9kVo2XeIEfni': ['index_info'], 'var_call_MqqTdJbb6yZMrlpfyXXTAuPw': ['index_trade'], 'var_call_ArTixs3DtwsDsll6YElaQFG5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_Mn7IoMavk9xNS3KQb4meY6cv': 'file_storage/call_Mn7IoMavk9xNS3KQb4meY6cv.json'}

exec(code, env_args)
