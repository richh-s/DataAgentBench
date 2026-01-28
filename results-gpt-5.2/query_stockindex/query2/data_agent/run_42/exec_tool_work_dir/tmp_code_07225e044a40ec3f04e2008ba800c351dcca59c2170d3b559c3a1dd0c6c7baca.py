code = """import json
import pandas as pd

df = pd.DataFrame(var_call_F2E04xUzuzdRjPD0SVgWUzCs)
for c in ['up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# North America mapping based on exchange list and available indices
mapping = {
    'NYA': 'New York Stock Exchange',
    'IXIC': 'NASDAQ',
    'GSPTSE': 'Toronto Stock Exchange'
}

df['Exchange'] = df['Index'].map(mapping)
df['more_up_than_down'] = df['up_days'] > df['down_days']
result = df[df['more_up_than_down']][['Index','Exchange','up_days','down_days']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QZ8jyK603q2duo42AxTp9xI6': ['index_info'], 'var_call_vam4uTB8TNFvsDIxq9ABczMC': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_1h94U3qkgW8chdsQvXLPIOBB': [{'Index': '000001.SS', 'n': '5791'}, {'Index': '399001.SZ', 'n': '5760'}, {'Index': 'GDAXI', 'n': '8438'}, {'Index': 'GSPTSE', 'n': '10526'}, {'Index': 'HSI', 'n': '8492'}, {'Index': 'IXIC', 'n': '12690'}, {'Index': 'J203.JO', 'n': '2346'}, {'Index': 'N100', 'n': '5474'}, {'Index': 'N225', 'n': '13874'}, {'Index': 'NSEI', 'n': '3346'}, {'Index': 'NYA', 'n': '13947'}, {'Index': 'SSMI', 'n': '7671'}, {'Index': 'TWII', 'n': '5869'}], 'var_call_F2E04xUzuzdRjPD0SVgWUzCs': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}]}

exec(code, env_args)
