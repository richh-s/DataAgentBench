code = """import json
# Load stockinfo query result and stocktrade table list from storage
# Variables available: var_call_BgwYg1HfC2uTmILKaMuNl1Kc, var_call_J5nXUxgsJFd2mFEKbycrZPRG

def load_maybe_json(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r') as f:
            return json.load(f)
    return var

stockinfo = load_maybe_json(var_call_BgwYg1HfC2uTmILKaMuNl1Kc)
trade_tables = load_maybe_json(var_call_J5nXUxgsJFd2mFEKbycrZPRG)

symbols = [r['Symbol'] for r in stockinfo]
# Intersection with trade_tables
available_symbols = [s for s in symbols if s in trade_tables]

# Output the list of symbols to query
print('__RESULT__:')
print(json.dumps(available_symbols))"""

env_args = {'var_call_BgwYg1HfC2uTmILKaMuNl1Kc': 'file_storage/call_BgwYg1HfC2uTmILKaMuNl1Kc.json', 'var_call_J5nXUxgsJFd2mFEKbycrZPRG': 'file_storage/call_J5nXUxgsJFd2mFEKbycrZPRG.json'}

exec(code, env_args)
