code = """import json, pandas as pd
from pathlib import Path

symbols_path = Path(var_call_8DQPbtO3dKYO6n32ZAdgBBVJ)
symbols = json.loads(symbols_path.read_text())
syms = [r['Symbol'] for r in symbols]

subset = syms[:200]

tables_path = Path(var_call_VVzGVAQojORj5Kibor2gdtMq)
all_tables = json.loads(tables_path.read_text())

valid = [s for s in subset if s in all_tables]

result = json.dumps({'symbols_subset': subset, 'valid_in_trade_db': valid})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_VVzGVAQojORj5Kibor2gdtMq': 'file_storage/call_VVzGVAQojORj5Kibor2gdtMq.json', 'var_call_8DQPbtO3dKYO6n32ZAdgBBVJ': 'file_storage/call_8DQPbtO3dKYO6n32ZAdgBBVJ.json'}

exec(code, env_args)
