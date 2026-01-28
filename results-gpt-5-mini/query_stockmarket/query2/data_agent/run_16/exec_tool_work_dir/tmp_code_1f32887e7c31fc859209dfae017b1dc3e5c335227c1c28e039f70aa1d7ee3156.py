code = """import json
with open(var_call_qmvmcRybdZcFdW5SX1SGgE7P, 'r') as f:
    data = json.load(f)
avail = data['available_symbols']
parts = []
for s in avail:
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
sql = '\nUNION ALL\n'.join(parts) + '\nORDER BY symbol;'
print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_7unxnarEaWwSx7trThvVwizq': ['stockinfo'], 'var_call_WaEvCHYDu8q5PYvnJxAh1X2s': 'file_storage/call_WaEvCHYDu8q5PYvnJxAh1X2s.json', 'var_call_C9yV3KAORv9nL5ONxiYWO0Ud': 'file_storage/call_C9yV3KAORv9nL5ONxiYWO0Ud.json', 'var_call_qmvmcRybdZcFdW5SX1SGgE7P': 'file_storage/call_qmvmcRybdZcFdW5SX1SGgE7P.json', 'var_call_OGElpgdUKVjjtwiBNMmoRl2k': {'found_candidates': ['SPY', 'IVV', 'VOO', 'VTI', 'VOO', 'GDX', 'GLD', 'IWM']}, 'var_call_pShZKFfPvkw2i3ho63eG2iA3': {'count': 1435}, 'var_call_T2s3SMmnrDDar7AfeaZilSXw': [{'max_adj': '193.3121490478516'}], 'var_call_8kigaDXVZ7Og7it9o6p36gIb': [{'max_adj': '193.5270538330078'}], 'var_call_Ae01SicKrlCdy5HcO3QyGazr': [{'max_adj': '177.17626953125'}], 'var_call_1AzmSteQF09NG7AMwMwlICg4': [{'max_adj': '100.54161834716795'}], 'var_call_CJsBQ25v8NqA1e0R1NRloR57': [{'max_adj': '22.22186088562012'}], 'var_call_hKwurSjHgwhhzhaVZfAnVvtn': [{'max_adj': '125.2300033569336'}], 'var_call_qa49juFLzEhrTKn02dzJCxOt': [], 'var_call_ctm4WU5ShENl5c1iM4nvVxKF': [], 'var_call_spOjJ0eiTyxLa4u61NH2sqCH': [], 'var_call_gXSVKDAI9uyblFeNm9LR5HJj': [], 'var_call_gycDezTgdlY33nNTyEJT3zcS': [], 'var_call_yy9yY7kMFYm5INs2WOMQfsMB': [], 'var_call_V0h9FA51MxJBMVt7sHpN9iE6': [], 'var_call_DWSsJBQ3IqiBKdx5lklaCocM': [], 'var_call_1SNXAsbyswsteERrtqDY1BKD': [], 'var_call_IWCN9FfDGnqrUNYoUTHzuocv': []}

exec(code, env_args)
