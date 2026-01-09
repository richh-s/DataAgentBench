code = """import json, pandas as pd
from pathlib import Path

sym_src = var_call_FYEjIjKBttbGajFqd6mFIEyR
if isinstance(sym_src, str) and Path(sym_src).exists():
    sym_payload = json.loads(Path(sym_src).read_text())
else:
    sym_payload = sym_src
symbols = set(sym_payload['symbols'])

lst_src = var_call_TacH1SzeiloqaPHt8X1kJMhw
if isinstance(lst_src, str) and Path(lst_src).exists():
    all_tables = json.loads(Path(lst_src).read_text())
else:
    all_tables = lst_src

available = sorted(list(symbols.intersection(all_tables)))
missing = sorted(list(symbols.difference(all_tables)))

print('__RESULT__:')
print(json.dumps({'available': available, 'missing': missing, 'n_available': len(available), 'n_missing': len(missing)}))"""

env_args = {'var_call_Zn1ziHBgt0lm454JT5C7GiNT': 'file_storage/call_Zn1ziHBgt0lm454JT5C7GiNT.json', 'var_call_FYEjIjKBttbGajFqd6mFIEyR': 'file_storage/call_FYEjIjKBttbGajFqd6mFIEyR.json', 'var_call_TacH1SzeiloqaPHt8X1kJMhw': 'file_storage/call_TacH1SzeiloqaPHt8X1kJMhw.json'}

exec(code, env_args)
