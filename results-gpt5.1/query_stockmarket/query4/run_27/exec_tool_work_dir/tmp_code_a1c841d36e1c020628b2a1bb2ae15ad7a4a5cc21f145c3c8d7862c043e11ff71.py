code = """import json, pandas as pd
from pathlib import Path

symbols = json.loads(Path(var_call_fxnkv82rBl8tiSErzAmdokTp).read_text())
meta = pd.read_json(var_call_Kxfl8JHTJpmGvmbIlfmgsbfq)

valid = meta[meta['Symbol'].isin(symbols)].Symbol.tolist()
valid = valid[:50]

result = {'symbols': valid}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fxnkv82rBl8tiSErzAmdokTp': 'file_storage/call_fxnkv82rBl8tiSErzAmdokTp.json', 'var_call_Kxfl8JHTJpmGvmbIlfmgsbfq': 'file_storage/call_Kxfl8JHTJpmGvmbIlfmgsbfq.json'}

exec(code, env_args)
