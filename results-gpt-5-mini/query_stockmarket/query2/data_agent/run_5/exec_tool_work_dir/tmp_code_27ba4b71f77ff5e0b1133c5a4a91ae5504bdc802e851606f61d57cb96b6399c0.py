code = """import json
with open(var_call_svQsBvucK6HUwI89ycJ6EqMt, 'r') as f:
    symbols = json.load(f)
calls = []
for s in symbols:
    q = "SELECT '{}' AS Symbol FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(s, s)
    calls.append({
        'recipient_name': 'functions.query_db',
        'parameters': {
            'db_name': 'stocktrade_database',
            'query': q
        }
    })
print('__RESULT__:')
print(json.dumps(calls))"""

env_args = {'var_call_sivacHuiSgcyyLES4JY2Pmbh': 'file_storage/call_sivacHuiSgcyyLES4JY2Pmbh.json', 'var_call_8wxgRA4ankapzlMw4DhePGJj': 'file_storage/call_8wxgRA4ankapzlMw4DhePGJj.json', 'var_call_GM4b9XWbZdjPKEghYXIfgFyD': {'has_SPY': True, 'total_etfs': 1435}, 'var_call_svQsBvucK6HUwI89ycJ6EqMt': 'file_storage/call_svQsBvucK6HUwI89ycJ6EqMt.json', 'var_call_2oMOmlZNivM6PlBm9Di2B1Cz': [], 'var_call_vnuNeODHxnkNI6xdxOSx0DKI': [{'max_adj': '193.3121490478516'}]}

exec(code, env_args)
