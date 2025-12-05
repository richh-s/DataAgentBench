code = """import json, pandas as pd
from pathlib import Path

symbols_path = Path(var_call_jreTHt5lIugJbSy1KKkOhymu)
with open(symbols_path) as f:
    all_symbols = json.load(f)

nyse_path = Path(var_call_ZJzUCWbbpRn7gUBsf0crFa8l)
with open(nyse_path) as f:
    nyse_records = json.load(f)

nyse_syms = {r['Symbol'] for r in nyse_records}
common = sorted(list(set(all_symbols) & nyse_syms))

result = json.dumps(common)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_jreTHt5lIugJbSy1KKkOhymu': 'file_storage/call_jreTHt5lIugJbSy1KKkOhymu.json', 'var_call_ZJzUCWbbpRn7gUBsf0crFa8l': 'file_storage/call_ZJzUCWbbpRn7gUBsf0crFa8l.json'}

exec(code, env_args)
