code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

info = load_records(var_call_WUWNAstTHRWuxShkejbmmb3q)
trade_tables = set(load_records(var_call_wN5P7wyYzbAWkh7ELYtCJadn))

# keep only those symbols that have a price table
syms = [r['symbol'] for r in info if r.get('symbol') in trade_tables]

print('__RESULT__:')
print(json.dumps({'symbols': syms, 'n_symbols': len(syms)}))"""

env_args = {'var_call_WUWNAstTHRWuxShkejbmmb3q': 'file_storage/call_WUWNAstTHRWuxShkejbmmb3q.json', 'var_call_wN5P7wyYzbAWkh7ELYtCJadn': 'file_storage/call_wN5P7wyYzbAWkh7ELYtCJadn.json'}

exec(code, env_args)
