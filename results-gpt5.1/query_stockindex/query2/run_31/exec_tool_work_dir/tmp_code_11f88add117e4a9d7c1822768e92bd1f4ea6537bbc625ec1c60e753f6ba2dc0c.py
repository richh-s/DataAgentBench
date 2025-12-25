code = """import json, pandas as pd, os

file_path = var_call_FlLXHBiyzrdncRosxqhPgLld
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

north_american_indices = ['NYA', 'IXIC', 'GSPTSE']

mask = df['Index'].isin(north_american_indices)
df_na = df[mask].copy()

for col in ['Open','Close']:
    df_na[col] = pd.to_numeric(df_na[col], errors='coerce')

summary = (
    df_na.assign(
        up = lambda x: x['Close'] > x['Open'],
        down = lambda x: x['Close'] < x['Open']
    )
    .groupby('Index')
    .agg(up_days=('up','sum'), down_days=('down','sum'))
    .reset_index()
)

indices_more_up = summary[summary['up_days'] > summary['down_days']]['Index'].tolist()

result = {
    'summary': summary.to_dict(orient='records'),
    'indices_more_up_than_down': indices_more_up
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_NtiwOB4WPDheLB2eT6FcJLTO': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_call_5TDOqipyVUIj69Am0zapL1jO': ['index_info'], 'var_call_WTG8Q709yWhcXWVbcE4N3icu': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_FlLXHBiyzrdncRosxqhPgLld': 'file_storage/call_FlLXHBiyzrdncRosxqhPgLld.json'}

exec(code, env_args)
