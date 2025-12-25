code = """import json, pandas as pd
from pathlib import Path

symbols_info_path = var_call_ZoxXTIkEg5ZdDMyedDebSxM2
symbols_info = json.loads(Path(symbols_info_path).read_text())
syms = [r['Symbol'] for r in symbols_info]

trade_tables_path = var_call_sRUK4slh5PzeLALqTCEprMm2
trade_tables = json.loads(Path(trade_tables_path).read_text())

common = sorted(set(syms).intersection(trade_tables))

ranges = []

import duckdb
con = duckdb.connect(database='stocktrade_database', read_only=True)

for sym in common:
    try:
        df = con.execute(f"SELECT Date, High, Low FROM '{sym}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31';").df()
    except Exception:
        continue
    if df.empty:
        continue
    df['range_ratio'] = (df['High'] - df['Low']) / df['Low']
    count = int((df['range_ratio'] > 0.20).sum())
    if count > 0:
        ranges.append({'Symbol': sym, 'Days': count})

con.close()

res_df = pd.DataFrame(ranges)
if not res_df.empty:
    top5 = res_df.sort_values(['Days','Symbol'], ascending=[False, True]).head(5)
    top_syms = top5['Symbol'].tolist()
else:
    top_syms = []

sym_to_name = {r['Symbol']: r['Company Description'] for r in symbols_info}
company_names = [sym_to_name[s] for s in top_syms]

result = json.dumps(company_names)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_sRUK4slh5PzeLALqTCEprMm2': 'file_storage/call_sRUK4slh5PzeLALqTCEprMm2.json', 'var_call_ZoxXTIkEg5ZdDMyedDebSxM2': 'file_storage/call_ZoxXTIkEg5ZdDMyedDebSxM2.json'}

exec(code, env_args)
