code = """import json
# var_call_lCBAWEHlSlVrH02gGSxVht7U is available from previous query
data = var_call_lCBAWEHlSlVrH02gGSxVht7U
# Ensure numeric conversion
for d in data:
    d['avg_intraday_vol'] = float(d['avg_intraday_vol'])
best = max(data, key=lambda x: x['avg_intraday_vol'])
result = {
    'index': best['Index'],
    'avg_intraday_vol': best['avg_intraday_vol'],
    'avg_intraday_vol_pct': round(best['avg_intraday_vol'] * 100, 4)
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FxbppF2CSn9Z4REnI3SZiQ1R': ['index_trade'], 'var_call_c9bl5Hc46VEV1TKQQzAXZEpx': ['index_info'], 'var_call_GnE6JGBd4aZtDbVAZ24XJKXq': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_lCBAWEHlSlVrH02gGSxVht7U': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_intraday_vol': '0.01382304680245353'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01348835226084207'}, {'Index': 'N225', 'avg_intraday_vol': '0.008720764073041308'}]}

exec(code, env_args)
