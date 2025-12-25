code = """import json, pandas as pd
from pathlib import Path

batches = json.loads(Path(var_call_PN8xaMvNq6inhfoWHbD0PzV6).read_text())
print('__RESULT__:')
print(json.dumps(batches[:4]))"""

env_args = {'var_call_tbB0p7fD7qBqdk6JWhPTBi7a': 'file_storage/call_tbB0p7fD7qBqdk6JWhPTBi7a.json', 'var_call_VXY93cvngCXxTpY6a7LHv1KV': 'file_storage/call_VXY93cvngCXxTpY6a7LHv1KV.json', 'var_call_PN8xaMvNq6inhfoWHbD0PzV6': 'file_storage/call_PN8xaMvNq6inhfoWHbD0PzV6.json'}

exec(code, env_args)
