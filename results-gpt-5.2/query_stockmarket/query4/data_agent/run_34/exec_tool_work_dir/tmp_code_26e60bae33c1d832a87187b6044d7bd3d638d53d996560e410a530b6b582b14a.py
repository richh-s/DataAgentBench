code = """import json
import pandas as pd

nyse_path = var_call_W9DknPtITkO5E8fVFyGGCP1i
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)

trade_path = var_call_IkdZGIDgN5BwsY28UnCmseZJ
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

symbols = sorted(set(nyse_df['Symbol']).intersection(trade_tables))
chunks = [symbols[i:i+80] for i in range(0, len(symbols), 80)]

fmt = "SELECT '{0}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM \"{0}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"

queries = []
for chunk in chunks:
    parts = [fmt.format(sym) for sym in chunk]
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'n_chunks': len(queries), 'q0_start': queries[0][:160]}))"""

env_args = {'var_call_W9DknPtITkO5E8fVFyGGCP1i': 'file_storage/call_W9DknPtITkO5E8fVFyGGCP1i.json', 'var_call_IkdZGIDgN5BwsY28UnCmseZJ': 'file_storage/call_IkdZGIDgN5BwsY28UnCmseZJ.json', 'var_call_UsFARjzhRdUpjRMozyesZDyT': {'a': 1}, 'var_call_0Tl5rumVClCnuwCs6jSI49Ox': {'n_symbols': 234, 'first10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_fYerQF0UCfobeIErd7qXjARo': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_M7EGmETCBvxPGIMKeYmUothi': {'q': "SELECT 'AIN' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days"}, 'var_call_FDruDVhtF9CeIMWNfQYa0s66': {'pd_version': '2.3.3'}, 'var_call_3d0DpwYc7Ba9NHoC0ocaDbTv': {'s': "FROM '{0}' WHERE Date >= '2017-01-01'"}, 'var_call_MFQkdAqAFU34u03iO5S7SHac': {'s': 'FROM "X"'}, 'var_call_px2hcmt89gIE9RUG0CVEnTfo': {'s': 'SELECT 1 FROM "AEFC"'}}

exec(code, env_args)
