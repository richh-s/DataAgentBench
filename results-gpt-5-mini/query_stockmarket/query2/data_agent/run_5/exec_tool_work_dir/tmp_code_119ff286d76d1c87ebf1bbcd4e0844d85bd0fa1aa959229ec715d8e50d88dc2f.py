code = """import json
with open(var_call_svQsBvucK6HUwI89ycJ6EqMt, 'r') as f:
    symbols = json.load(f)
batch = symbols[:150]
parts = []
for s in batch:
    parts.append("SELECT '" + s + "' AS Symbol, MAX(\"Adj Close\") as max_adj FROM \"" + s + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
query = " UNION ALL ".join(parts) + ";"
print('__RESULT__:')
print(json.dumps({'query': query, 'len': len(batch)}))"""

env_args = {'var_call_sivacHuiSgcyyLES4JY2Pmbh': 'file_storage/call_sivacHuiSgcyyLES4JY2Pmbh.json', 'var_call_8wxgRA4ankapzlMw4DhePGJj': 'file_storage/call_8wxgRA4ankapzlMw4DhePGJj.json', 'var_call_GM4b9XWbZdjPKEghYXIfgFyD': {'has_SPY': True, 'total_etfs': 1435}, 'var_call_svQsBvucK6HUwI89ycJ6EqMt': 'file_storage/call_svQsBvucK6HUwI89ycJ6EqMt.json', 'var_call_2oMOmlZNivM6PlBm9Di2B1Cz': [], 'var_call_vnuNeODHxnkNI6xdxOSx0DKI': [{'max_adj': '193.3121490478516'}], 'var_call_GvKoHGUrw88alYqSONJgoBfz': ['SELECT "SPY" FROM "SPY";']}

exec(code, env_args)
