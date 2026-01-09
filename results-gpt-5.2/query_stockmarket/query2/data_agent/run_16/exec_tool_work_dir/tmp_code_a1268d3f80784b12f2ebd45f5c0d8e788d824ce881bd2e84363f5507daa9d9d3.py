code = """import json

# NOTE: required print format

path_etfs = var_call_GhhqzigemFWLhVImnohWlQBL
with open(path_etfs, 'r') as f:
    etfs = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs})

path_tables = var_call_LJHghFAAPNKl9yp5GcEObROY
with open(path_tables, 'r') as f:
    tables = set(json.load(f))

candidates = [t for t in tickers if t in tables]

result = {'candidates_count': len(candidates), 'sample': candidates[:10]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GhhqzigemFWLhVImnohWlQBL': 'file_storage/call_GhhqzigemFWLhVImnohWlQBL.json', 'var_call_LJHghFAAPNKl9yp5GcEObROY': 'file_storage/call_LJHghFAAPNKl9yp5GcEObROY.json'}

exec(code, env_args)
