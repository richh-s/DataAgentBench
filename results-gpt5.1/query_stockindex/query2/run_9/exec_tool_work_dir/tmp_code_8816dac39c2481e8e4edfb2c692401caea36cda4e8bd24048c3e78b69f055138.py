code = """import json, pandas as pd

file_path = var_call_smYhVCtgOIU71Mzrjo17zK0Y
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

na_indices = ['NYA','IXIC','GSPTSE']
na_df = df[df['Index'].isin(na_indices)].copy()

summary = na_df.groupby('Index').apply(lambda x: pd.Series({
    'up_days': int((x['Close'] > x['Open']).sum()),
    'down_days': int((x['Close'] < x['Open']).sum())
})).reset_index()

more_up_than_down = summary[summary['up_days'] > summary['down_days']]['Index'].tolist()

result = {
    'summary': summary.to_dict(orient='records'),
    'indices_with_more_up_than_down': more_up_than_down
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_ZKKrMxnyQSFQTZEIg39gLipk': ['index_info'], 'var_call_WgCuz5hYWjWvAilAF8SeBUsf': ['index_trade'], 'var_call_1rCtoj5g9IfoUMNvyJ1unHmG': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_wpKZwk8nRgScSHgy83wsLIbp': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_smYhVCtgOIU71Mzrjo17zK0Y': 'file_storage/call_smYhVCtgOIU71Mzrjo17zK0Y.json'}

exec(code, env_args)
