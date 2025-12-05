code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_fwpxwop3LAqklYG9DZOMmd51)
symbols = json.loads(path.read_text())

path2 = Path(var_call_lUBJ0oOgCnYx5dFlzOCYUGFe)
meta = pd.read_json(path2)
valid_syms = set(meta['Symbol'])

records = []
for sym in symbols:
    if sym not in valid_syms:
        continue
    records.append(sym)

result = json.dumps(records)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_fwpxwop3LAqklYG9DZOMmd51': 'file_storage/call_fwpxwop3LAqklYG9DZOMmd51.json', 'var_call_lUBJ0oOgCnYx5dFlzOCYUGFe': 'file_storage/call_lUBJ0oOgCnYx5dFlzOCYUGFe.json'}

exec(code, env_args)
