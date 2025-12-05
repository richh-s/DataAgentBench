code = """import json, pandas as pd
from pathlib import Path

etf_file = Path(var_call_f6Tg6xewDzu8LNzeqPkILNXn)
etf_symbols = pd.read_json(etf_file).Symbol.tolist()

trade_tables = set(var_call_t0RVqVxNzHULSFPLn9IEyJLg)

symbols = sorted(set(etf_symbols) & trade_tables)

batches = []
for i, sym in enumerate(symbols):
    batches.append(sym)

result = json.dumps({'symbols': batches})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_f6Tg6xewDzu8LNzeqPkILNXn': 'file_storage/call_f6Tg6xewDzu8LNzeqPkILNXn.json', 'var_call_t0RVqVxNzHULSFPLn9IEyJLg': 'file_storage/call_t0RVqVxNzHULSFPLn9IEyJLg.json'}

exec(code, env_args)
