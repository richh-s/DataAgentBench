code = """import json, pandas as pd
from pathlib import Path

# Load full 2018 data
file_path = Path(var_call_lgJttk5crO4mNyXGqpBsW9Xz)
records = json.loads(file_path.read_text())

df = pd.DataFrame(records)

# Ensure numeric
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Keep only North American indices: NYA (NYSE Composite), IXIC (Nasdaq Composite), GSPTSE (S&P/TSX)
north_america = ['NYA','IXIC','GSPTSE']
na_df = df[df['Index'].isin(north_america)].copy()

# Classify days
na_df['up'] = na_df['Close'] > na_df['Open']
na_df['down'] = na_df['Close'] < na_df['Open']

agg = na_df.groupby('Index').agg(up_days=('up','sum'), down_days=('down','sum')).reset_index()

# Determine which had more up days than down days
agg['more_up_than_down'] = agg['up_days'] > agg['down_days']

result_indices = agg[agg['more_up_than_down']]['Index'].tolist()

out = {
  'summary_by_index': agg.to_dict(orient='records'),
  'north_american_indices_with_more_up_than_down_in_2018': result_indices
}

res_str = json.dumps(out)
print("__RESULT__:")
print(res_str)"""

env_args = {'var_call_Ut4I99P2mujuwafD61o9EYuv': ['index_info'], 'var_call_G2TTD8dTidyKO8iAx3tI8qkQ': ['index_trade'], 'var_call_fxQod6XBozQdVG1hiQrncoXk': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_vtErpaP7opMYTSEdYIXifXrg': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_lgJttk5crO4mNyXGqpBsW9Xz': 'file_storage/call_lgJttk5crO4mNyXGqpBsW9Xz.json'}

exec(code, env_args)
