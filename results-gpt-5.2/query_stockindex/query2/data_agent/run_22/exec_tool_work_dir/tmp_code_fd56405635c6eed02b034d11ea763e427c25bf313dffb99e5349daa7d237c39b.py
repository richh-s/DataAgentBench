code = """import json
import pandas as pd

df = pd.DataFrame(var_call_MlCGYI13j42F4Uh7dPGW0lFQ)
# ensure numeric
for c in ['up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

def region(idx):
    # infer North America indices in this dataset
    return idx in {'NYA','IXIC','GSPTSE'}

df_na = df[df['Index'].apply(region)].copy()
df_na = df_na[df_na['up_days'] > df_na['down_days']].sort_values('Index')
res = df_na[['Index','up_days','down_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_9lecetwrYSJRhjrdDnEHI3to': ['index_info'], 'var_call_w7cyt9ZXUp89UXt2hxCKUtpF': ['index_trade'], 'var_call_lRmsmSSouF9RYLYfLZNLvclF': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_SO1EC4DG6LCHqbw4sFoiN22e': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_MlCGYI13j42F4Uh7dPGW0lFQ': [{'Index': 'J203.JO', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'N225', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'HSI', 'up_days': '44.0', 'down_days': '42.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'N100', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)
