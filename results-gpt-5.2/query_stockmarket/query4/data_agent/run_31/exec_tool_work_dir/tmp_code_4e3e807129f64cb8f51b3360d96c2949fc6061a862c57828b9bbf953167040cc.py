code = """import json
import pandas as pd

nyse = var_call_OnB6fCK9Z9sc0oRJT1v3w7fS
if isinstance(nyse, str):
    with open(nyse, 'r') as f:
        nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)
nyse_symbols = set(nyse_df['Symbol'].astype(str))

tables = var_call_MW2L0mKITaFAwthgkJuiG1GZ
if isinstance(tables, str):
    with open(tables, 'r') as f:
        tables = json.load(f)

db_tables = set(tables)
use_symbols = sorted(nyse_symbols.intersection(db_tables))

chunks = []
step = 80
for i in range(0, len(use_symbols), step):
    chunks.append(use_symbols[i:i+step])

queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        stmt = "SELECT '{s}' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(s=sym)
        parts.append(stmt)
    queries.append(" UNION ALL ".join(parts))

out_obj = {
    "n_symbols": len(use_symbols),
    "n_chunks": len(queries),
    "first_queries": queries[:5]
}
print('__RESULT__:')
print(json.dumps(out_obj))"""

env_args = {'var_call_KX5UnkAb3MmDwt33HLN1ZTMv': ['stockinfo'], 'var_call_OnB6fCK9Z9sc0oRJT1v3w7fS': 'file_storage/call_OnB6fCK9Z9sc0oRJT1v3w7fS.json', 'var_call_MW2L0mKITaFAwthgkJuiG1GZ': 'file_storage/call_MW2L0mKITaFAwthgkJuiG1GZ.json'}

exec(code, env_args)
