code = """import json, pandas as pd
from pathlib import Path

# Load ETF symbols listed on NYSE Arca
file_path = Path(var_call_9hPkFZsDuymgRcL7QRufasBW)
etf_symbols = pd.read_json(file_path).Symbol.tolist()

# Intersect with available price tables
tables = var_call_TYjWsVk7c4TsEHPan7ecqaIQ
symbols = sorted(set(etf_symbols).intersection(tables))

result = json.dumps(symbols)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_9hPkFZsDuymgRcL7QRufasBW': 'file_storage/call_9hPkFZsDuymgRcL7QRufasBW.json', 'var_call_TYjWsVk7c4TsEHPan7ecqaIQ': 'file_storage/call_TYjWsVk7c4TsEHPan7ecqaIQ.json'}

exec(code, env_args)
