code = """import json
# var_call_MhzXTkdczdawn58wyHuM9TC8 is available from previous query
data = var_call_MhzXTkdczdawn58wyHuM9TC8
best = None
best_val = None
for r in data:
    try:
        val = float(r.get('avg_intraday_vol'))
    except Exception:
        continue
    if best_val is None or val > best_val:
        best_val = val
        best = r.get('Index')
result = {'index': best, 'avg_intraday_vol': best_val, 'avg_intraday_vol_percent': best_val * 100 if best_val is not None else None}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zdSvf0raBzI6rJChGlm3PeSf': ['index_trade'], 'var_call_YKjyRprprff1JzdnqoApwugv': ['index_info'], 'var_call_B4GSyjXYpc3oEpXO7CSirtM1': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_MhzXTkdczdawn58wyHuM9TC8': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_intraday_vol': '0.01382304680245353'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01348835226084207'}, {'Index': 'N225', 'avg_intraday_vol': '0.008720764073041308'}]}

exec(code, env_args)
