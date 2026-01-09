code = """import json, pandas as pd

df = pd.DataFrame(var_call_5FMFE4jEjPjD9CJrHuaIOcDI)
df['growth_of_each_contribution'] = df['growth_of_each_contribution'].astype(float)
df['n_months'] = df['n_months'].astype(int)
# keep only indices with near-full history since 2000; max in this result is 258 months
max_months = df['n_months'].max()
df_full = df[df['n_months'] >= max_months-1].copy()
top5 = df_full.sort_values('growth_of_each_contribution', ascending=False).head(5)

mapping = {
    'N100': {'country':'Europe (Eurozone)', 'exchange':'Euronext / pan-European (EURONEXT 100)'},
    '399001.SZ': {'country':'China', 'exchange':'Shenzhen Stock Exchange'},
    'IXIC': {'country':'United States', 'exchange':'NASDAQ'},
    'GSPTSE': {'country':'Canada', 'exchange':'Toronto Stock Exchange'},
    '000001.SS': {'country':'China', 'exchange':'Shanghai Stock Exchange'},
}
rows = []
for _, r in top5.iterrows():
    idx = r['Index']
    info = mapping.get(idx, {})
    rows.append({
        'Index': idx,
        'Overall_return_metric': r['growth_of_each_contribution'],
        'Months_used': int(r['n_months']),
        'Country': info.get('country', None),
        'Exchange': info.get('exchange', None)
    })

print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_7KWC90TCyZV6wv0BiGuEvMF0': ['index_info'], 'var_call_6uLR1NX3W2K3JkMd6gNrhZ9n': ['index_trade'], 'var_call_5FMFE4jEjPjD9CJrHuaIOcDI': [{'Index': 'N100', 'growth_of_each_contribution': '258.1452433128482', 'n_months': '258'}, {'Index': '399001.SZ', 'growth_of_each_contribution': '258.1139032336801', 'n_months': '258'}, {'Index': 'IXIC', 'growth_of_each_contribution': '258.0636720689828', 'n_months': '257'}, {'Index': 'GSPTSE', 'growth_of_each_contribution': '257.9598027802123', 'n_months': '257'}, {'Index': '000001.SS', 'growth_of_each_contribution': '257.5968008131514', 'n_months': '257'}, {'Index': 'NYA', 'growth_of_each_contribution': '257.3395107088079', 'n_months': '257'}, {'Index': 'GDAXI', 'growth_of_each_contribution': '257.2180611723547', 'n_months': '257'}, {'Index': 'N225', 'growth_of_each_contribution': '257.14226597752565', 'n_months': '257'}, {'Index': 'HSI', 'growth_of_each_contribution': '256.76989104168206', 'n_months': '257'}, {'Index': 'SSMI', 'growth_of_each_contribution': '256.4449157135544', 'n_months': '257'}, {'Index': 'TWII', 'growth_of_each_contribution': '256.0905473485583', 'n_months': '256'}, {'Index': 'NSEI', 'growth_of_each_contribution': '165.99932061845738', 'n_months': '165'}, {'Index': 'J203.JO', 'growth_of_each_contribution': '112.57448557964905', 'n_months': '112'}]}

exec(code, env_args)
