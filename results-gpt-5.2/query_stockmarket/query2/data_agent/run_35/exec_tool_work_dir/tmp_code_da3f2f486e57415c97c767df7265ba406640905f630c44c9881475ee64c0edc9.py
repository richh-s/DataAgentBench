code = """import json, pandas as pd

# Load stockinfo ETF list (NYSE ARCA)
path_info = var_call_pyUpx70CiTUTPX4FbKRXqLqU
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# Load available price tables
path_tables = var_call_6pETY1mJuNOhB4PdOukuBDhp
with open(path_tables, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# Candidate tickers that have a price table
candidates = sorted(set(info_df['symbol']).intersection(tables_set))

print('__RESULT__:')
print(json.dumps({'candidates': candidates, 'n_candidates': len(candidates)}))"""

env_args = {'var_call_pyUpx70CiTUTPX4FbKRXqLqU': 'file_storage/call_pyUpx70CiTUTPX4FbKRXqLqU.json', 'var_call_6pETY1mJuNOhB4PdOukuBDhp': 'file_storage/call_6pETY1mJuNOhB4PdOukuBDhp.json'}

exec(code, env_args)
