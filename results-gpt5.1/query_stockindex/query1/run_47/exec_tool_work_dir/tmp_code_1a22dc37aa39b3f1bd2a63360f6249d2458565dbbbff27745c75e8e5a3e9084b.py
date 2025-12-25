code = """import json, pandas as pd
from datetime import datetime

path = var_call_QIlq3vWskgOHshydHHD0DbXP
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# parse year from messy Date strings
def get_year(s):
    for fmt in ['%Y-%m-%d','%d %b %Y, %H:%M','%b %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(s, fmt).year
        except Exception:
            continue
    return None

df['year'] = df['Date'].apply(get_year)

# filter 2020+
df = df[df['year']>=2020]

# Asia indices mapping based on knowledge
asia_indices = ['N225','HSI','000001.SS','399001.SZ','TWII','NSEI']

asia_df = df[df['Index'].isin(asia_indices)].copy()

asia_df['vol'] = (asia_df['High'] - asia_df['Low']) / asia_df['Open']

result = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)

out = result.reset_index().to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5EIMi2TNnXWdayMXGAqazSfp': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_lWexIU0o9kDrhZY9Ibqrxdqi': ['index_info'], 'var_call_QIlq3vWskgOHshydHHD0DbXP': 'file_storage/call_QIlq3vWskgOHshydHHD0DbXP.json'}

exec(code, env_args)
