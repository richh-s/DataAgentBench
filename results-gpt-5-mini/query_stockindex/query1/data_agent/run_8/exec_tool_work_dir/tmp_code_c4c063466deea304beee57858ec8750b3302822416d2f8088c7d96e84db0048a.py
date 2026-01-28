code = """import json
# var_call_yBeq9ujV8AUuhBWvqwovXr5s is available from previous query
data = var_call_yBeq9ujV8AUuhBWvqwovXr5s
# Convert avg_intraday_vol to float
for r in data:
    try:
        r['avg_intraday_vol'] = float(r['avg_intraday_vol'])
    except:
        r['avg_intraday_vol'] = None
# Find the index with the highest average intraday volatility
best = max([r for r in data if r['avg_intraday_vol'] is not None], key=lambda x: x['avg_intraday_vol'])
result = {
    'index': best['Index'],
    'avg_intraday_vol': best['avg_intraday_vol'],
    'avg_intraday_vol_pct': round(best['avg_intraday_vol'] * 100, 4),
    'region': 'Asia',
    'since': '2020-01-01'
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vpRuU77JL7cPCS8tUbBZgiop': ['index_trade'], 'var_call_lpzXqd1EyVbL6YNdKftm3Qg2': ['index_info'], 'var_call_n5j6kxhDpcgJKuIYww9M6FR1': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'J203.JO'}], 'var_call_yBeq9ujV8AUuhBWvqwovXr5s': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_intraday_vol': '0.01382304680245353'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01348835226084207'}, {'Index': 'N225', 'avg_intraday_vol': '0.008720764073041308'}]}

exec(code, env_args)
