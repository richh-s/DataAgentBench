code = """import json, pandas as pd

r1 = pd.DataFrame(var_call_Cz16jLdhJO59PCZJulEP6FM8)
r2 = pd.DataFrame(var_call_NHHHJhV5mDw38PjNDVsgp4hm)

df = pd.concat([r1, r2], ignore_index=True)
for c in ['up_days','down_days']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df = df.dropna(subset=['up_days','down_days'])
df = df[df['up_days'] > df['down_days']]

top5 = df.sort_values(['up_days','Symbol'], ascending=[False, True]).head(5)

# join names
names_path = var_call_3MxZqE8D8mCsY0STYp4ujphc
with open(names_path,'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)
nyse_df = nyse_df.rename(columns={'company_name':'Company Description'})
name_map = dict(zip(nyse_df['Symbol'], nyse_df['Company Description']))

top5['Company'] = top5['Symbol'].map(name_map)
answer_list = top5['Company'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_3MxZqE8D8mCsY0STYp4ujphc': 'file_storage/call_3MxZqE8D8mCsY0STYp4ujphc.json', 'var_call_uMrsBwkUnotoXp99tcZtbiOO': 'file_storage/call_uMrsBwkUnotoXp99tcZtbiOO.json', 'var_call_4Uvx1qqK4R71Y8OgN6eizNX0': 'file_storage/call_4Uvx1qqK4R71Y8OgN6eizNX0.json', 'var_call_Cz16jLdhJO59PCZJulEP6FM8': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'Symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'Symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'Symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'Symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'Symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'Symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'Symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'Symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'Symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'Symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'Symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'Symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'Symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'Symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}, {'Symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'Symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'Symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}], 'var_call_NHHHJhV5mDw38PjNDVsgp4hm': [{'Symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'Symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'Symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'Symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'Symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'Symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'Symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'Symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'Symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}, {'Symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}, {'Symbol': 'CXH', 'up_days': '126.0', 'down_days': '91.0'}]}

exec(code, env_args)
