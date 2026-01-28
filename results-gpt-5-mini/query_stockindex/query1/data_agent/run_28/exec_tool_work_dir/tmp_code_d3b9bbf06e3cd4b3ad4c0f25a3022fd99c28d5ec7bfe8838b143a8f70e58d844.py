code = """import json
# var_call_GqNwa541ftm3AnzQPhUMumlj is available from previous query
data = var_call_GqNwa541ftm3AnzQPhUMumlj
# Convert avg_intraday_vol to float
for rec in data:
    rec['avg_intraday_vol'] = float(rec['avg_intraday_vol'])
best = max(data, key=lambda r: r['avg_intraday_vol'])
# Map index to exchange name (inferred)
mapping = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'TWII': 'Taiwan Stock Exchange'
}
result = {
    'index': best['Index'],
    'exchange_inferred': mapping.get(best['Index'], 'Unknown'),
    'avg_intraday_vol': best['avg_intraday_vol'],
    'avg_intraday_vol_percent': best['avg_intraday_vol'] * 100,
    'region': 'Asia',
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kqNtlm5LMqjN8RybBDaajnyC': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_GqNwa541ftm3AnzQPhUMumlj': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_intraday_vol': '0.01382304680245353'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01348835226084207'}, {'Index': 'N225', 'avg_intraday_vol': '0.008720764073041308'}]}

exec(code, env_args)
