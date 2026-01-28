code = """import json
records = var_call_C0tZxJxca42Hi831b0MY1KOQ
# North American indices in dataset: NYA (NYSE Composite, US), IXIC (Nasdaq Composite, US), GSPTSE (S&P/TSX Composite, Canada)
more_up = [r["Index"] for r in records if float(r["up_days"]) > float(r["down_days"])]
print('__RESULT__:')
print(json.dumps({"indices_more_up_than_down_2018": more_up, "details": records}))"""

env_args = {'var_call_bd6ZYrDcnckFinUOKCNNUnkI': ['index_info'], 'var_call_8fR77FaeiY0jq3KCpN5iNaJm': ['index_trade'], 'var_call_wQhrWOwrEWbSQg1wPOEnEnQ8': [], 'var_call_3Hkock5tEhvqe9FrUwUjDL7u': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_C0tZxJxca42Hi831b0MY1KOQ': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}]}

exec(code, env_args)
