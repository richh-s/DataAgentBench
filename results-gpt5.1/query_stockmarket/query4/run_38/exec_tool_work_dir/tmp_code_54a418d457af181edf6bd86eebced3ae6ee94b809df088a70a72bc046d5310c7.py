code = """import json, pandas as pd
from pathlib import Path

nyse_meta = pd.read_json(Path(var_call_VXY93cvngCXxTpY6a7LHv1KV))
name_map = dict(zip(nyse_meta['Symbol'], nyse_meta['Company Description']))
print('__RESULT__:')
print(json.dumps(name_map))"""

env_args = {'var_call_tbB0p7fD7qBqdk6JWhPTBi7a': 'file_storage/call_tbB0p7fD7qBqdk6JWhPTBi7a.json', 'var_call_VXY93cvngCXxTpY6a7LHv1KV': 'file_storage/call_VXY93cvngCXxTpY6a7LHv1KV.json', 'var_call_PN8xaMvNq6inhfoWHbD0PzV6': 'file_storage/call_PN8xaMvNq6inhfoWHbD0PzV6.json', 'var_call_k6ovE5oxFW9igePQG32t6zbg': 'file_storage/call_k6ovE5oxFW9igePQG32t6zbg.json'}

exec(code, env_args)
