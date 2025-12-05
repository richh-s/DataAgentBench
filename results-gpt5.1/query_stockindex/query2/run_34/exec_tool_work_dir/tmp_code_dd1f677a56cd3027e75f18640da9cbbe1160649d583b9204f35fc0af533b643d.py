code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_BsN3EGRCeN0rr3JhchDz16q0)
records = json.loads(path.read_text())

north_american_indices = ['NYA', 'IXIC', 'GSPTSE']

df = pd.DataFrame(records)

for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

na_df = df[df['Index'].isin(north_american_indices)].copy()

na_df['up'] = na_df['Close'] > na_df['Open']
na_df['down'] = na_df['Close'] < na_df['Open']

summary = na_df.groupby('Index').agg(up_days=('up','sum'), down_days=('down','sum')).reset_index()

summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary.to_dict(orient='records')

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_cCVePSUVi0fCx7DYrVjK44gL': ['index_info'], 'var_call_ilN8G48VNdNVTeB91RywysOe': ['index_trade'], 'var_call_2YnILE10m9Kp2usdgt2Dwrwj': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_s1Ovehjbgb7PqhnRGN0dCCfg': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_BsN3EGRCeN0rr3JhchDz16q0': 'file_storage/call_BsN3EGRCeN0rr3JhchDz16q0.json'}

exec(code, env_args)
