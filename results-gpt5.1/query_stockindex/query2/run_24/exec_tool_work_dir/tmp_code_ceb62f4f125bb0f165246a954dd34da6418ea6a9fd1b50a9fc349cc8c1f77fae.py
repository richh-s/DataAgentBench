code = """import json, pandas as pd
from pathlib import Path

# Load large trade data
path = Path(var_call_72YIXV79ZVJrtbjkijnJlLL9)
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Determine up/down per row
df['up'] = df['Close'] > df['Open']
df['down'] = df['Close'] < df['Open']

agg = df.groupby('Index').agg(up_days=('up','sum'), down_days=('down','sum')).reset_index()

# Identify North American indices using geographic knowledge
# From distinct indices list: N225 (Japan), GSPTSE (Canada), NSEI (India), GDAXI (Germany), J203.JO (South Africa),
# IXIC (US - NASDAQ), HSI (Hong Kong), NYA (US - NYSE composite), 000001.SS (China), SSMI (Switzerland), TWII (Taiwan), N100 (Europe), 399001.SZ (China)

na_indices = ['GSPTSE', 'IXIC', 'NYA']

na_agg = agg[agg['Index'].isin(na_indices)].copy()
na_agg['more_up_than_down'] = na_agg['up_days'] > na_agg['down_days']

result_indices = na_agg[na_agg['more_up_than_down'] == True]['Index'].tolist()

result = {
  'north_american_indices': na_indices,
  'summary': na_agg.to_dict(orient='records'),
  'indices_more_up_than_down_2018': result_indices
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0rr8tWYaRtxlhbxYWdzdd6wD': ['index_info'], 'var_call_ETn63LdHWR7G5aza7dHMAliZ': ['index_trade'], 'var_call_Nf4z2EYfxgxkN3KMBWxPBAT3': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_EZe0QB8XeLwFQ6Z90PKLNaxQ': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_72YIXV79ZVJrtbjkijnJlLL9': 'file_storage/call_72YIXV79ZVJrtbjkijnJlLL9.json'}

exec(code, env_args)
