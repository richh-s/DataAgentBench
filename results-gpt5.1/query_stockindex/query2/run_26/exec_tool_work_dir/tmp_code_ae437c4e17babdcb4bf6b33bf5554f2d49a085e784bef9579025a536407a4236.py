code = """import json, pandas as pd
from collections import defaultdict

file_path = var_call_Zjr53kaTjNjKM9AcDCOmQvCZ
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Map indices to regions using knowledge
north_america_indices = {'NYA','IXIC','GSPTSE'}

mask_2018 = df['Date'].str.startswith('2018')

df_2018 = df[mask_2018 & df['Index'].isin(north_america_indices)].copy()

up = df_2018['Close'] > df_2018['Open']
down = df_2018['Close'] < df_2018['Open']

summary = df_2018.groupby('Index').agg(up_days = ('Index', lambda x: int(up[x.index].sum())),
                                       down_days = ('Index', lambda x: int(down[x.index].sum())))

more_up_than_down = summary[summary['up_days'] > summary['down_days']]

result = {
    'summary': summary.to_dict(orient='index'),
    'indices_with_more_up_than_down': list(more_up_than_down.index)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_XtBbG4QNMTPOkBWgQO48pQV2': ['index_info'], 'var_call_YreqbKaiFmmzf44L6FkUzcHt': ['index_trade'], 'var_call_JrWnrJA4wiJDeD9KP27Pr6xO': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_0nTXoxTO04vCYGkNwiLdQbuB': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_Zjr53kaTjNjKM9AcDCOmQvCZ': 'file_storage/call_Zjr53kaTjNjKM9AcDCOmQvCZ.json'}

exec(code, env_args)
