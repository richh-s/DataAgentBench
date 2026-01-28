code = """import json
p = var_call_4cWA3639OvPpZZVOsHr7ctXT
with open(p,'r') as f:
    candidates = json.load(f)
lines = []
for s in candidates:
    lines.append("SELECT '{}' as Symbol FROM \"{}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(s,s))
sql = '\nUNION ALL\n'.join(lines) + ';' if lines else ''
out = {'sql': sql}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_EeBDIfF6nIPvT4Tn05bSTLUt': 'file_storage/call_EeBDIfF6nIPvT4Tn05bSTLUt.json', 'var_call_BhqADYroukDRFFl1xBNUru7t': 'file_storage/call_BhqADYroukDRFFl1xBNUru7t.json', 'var_call_4cWA3639OvPpZZVOsHr7ctXT': 'file_storage/call_4cWA3639OvPpZZVOsHr7ctXT.json', 'var_call_ZU9namdVaRUioT5CGLmaD0mf': {'num_candidates': 1435, 'checks': {'SPY': True, 'IVV': True, 'VOO': True, 'DIA': True, 'QQQ': False, 'IWM': True, 'GLD': True, 'TQQQ': False, 'VTI': True}}}

exec(code, env_args)
