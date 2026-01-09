code = """import json, pandas as pd

# load stockinfo result (might be file path)
info_src = var_call_pDpILRLzxzoT5P1Kosgioq0m
if isinstance(info_src, str):
    with open(info_src, 'r') as f:
        info = json.load(f)
else:
    info = info_src

# load available trade tables list
tbl_src = var_call_MCUnaKaEKzfS0pL4YmqLF0EK
if isinstance(tbl_src, str):
    with open(tbl_src, 'r') as f:
        tables = json.load(f)
else:
    tables = tbl_src

tables_set = set(tables)

df = pd.DataFrame(info)
# keep tickers that exist as tables
candidates = df[df['Symbol'].isin(tables_set)]['Symbol'].dropna().unique().tolist()

print('__RESULT__:')
print(json.dumps({'candidate_tickers': candidates, 'n': len(candidates)}))"""

env_args = {'var_call_pDpILRLzxzoT5P1Kosgioq0m': 'file_storage/call_pDpILRLzxzoT5P1Kosgioq0m.json', 'var_call_MCUnaKaEKzfS0pL4YmqLF0EK': 'file_storage/call_MCUnaKaEKzfS0pL4YmqLF0EK.json'}

exec(code, env_args)
