code = """import json
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

nyse = pd.DataFrame(load_records(var_call_ShAWqPqxsj4pHI1S9zIIoOt3))
trade_tables = load_records(var_call_vI8ekiN5VeJk6XqELl5IDD41)
trade_set = set(trade_tables)
nyse = nyse[nyse['symbol'].isin(trade_set)].copy()
syms = nyse['symbol'].tolist()

# prioritize symbols likely to be equities (heuristics)
# exclude symbols with non-letter chars to avoid preferred/units/warrants (#, ., etc.)
filtered = [s for s in syms if s.isalpha()]

print('__RESULT__:')
print(json.dumps({'n_nyse_nonetf': int(len(nyse)), 'n_alpha': int(len(filtered)), 'symbols_alpha': filtered}))"""

env_args = {'var_call_ShAWqPqxsj4pHI1S9zIIoOt3': 'file_storage/call_ShAWqPqxsj4pHI1S9zIIoOt3.json', 'var_call_vI8ekiN5VeJk6XqELl5IDD41': 'file_storage/call_vI8ekiN5VeJk6XqELl5IDD41.json'}

exec(code, env_args)
