code = """import json, pandas as pd

# Load nyse non-etf symbols
path = var_call_L8xcnqg0W4d8vI21aAHPrMvi
with open(path, 'r') as f:
    nyse = json.load(f)
nyse_syms = set(r['Symbol'] for r in nyse)

# Load trade tables list
path2 = var_call_skSYwGwRw6CeNdOLTg9XrRK6
with open(path2, 'r') as f:
    trade_tables = json.load(f)
trade_set = set(trade_tables)

candidates = sorted(nyse_syms & trade_set)

# Build response
out = {
    'candidate_symbols': candidates,
    'n_candidates': len(candidates)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_skSYwGwRw6CeNdOLTg9XrRK6': 'file_storage/call_skSYwGwRw6CeNdOLTg9XrRK6.json', 'var_call_L8xcnqg0W4d8vI21aAHPrMvi': 'file_storage/call_L8xcnqg0W4d8vI21aAHPrMvi.json'}

exec(code, env_args)
