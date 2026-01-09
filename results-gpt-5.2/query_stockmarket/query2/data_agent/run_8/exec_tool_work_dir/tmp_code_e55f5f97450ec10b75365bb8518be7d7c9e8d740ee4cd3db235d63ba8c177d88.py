code = """import json, pandas as pd
from pathlib import Path

# load ETF list (NYSE Arca) from file
p_etfs = Path(var_call_knqBjIaMxogR3lHkligwPloV)
etfs = pd.read_json(p_etfs)

# load available price tables list
p_tables = Path(var_call_GYsjmtShYsheb16Fvx5ZEBFJ)
tables = json.loads(p_tables.read_text())

# keep only those with a price table
etfs_in_prices = etfs[etfs['Symbol'].isin(tables)].copy()

# build union query to find max Adj Close in 2015 for each ticker
subs = []
for sym in etfs_in_prices['Symbol'].tolist():
    # quote table name for duckdb
    t = '"' + sym.replace('"','""') + '"'
    subs.append(
        f"SELECT '{sym}' AS Symbol, max(\"Adj Close\") AS max_adj_close_2015 FROM {t} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'"
    )
union_sql = "\nUNION ALL\n".join(subs)

out = json.dumps({"union_sql": union_sql, "n_symbols": int(len(subs))})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_knqBjIaMxogR3lHkligwPloV': 'file_storage/call_knqBjIaMxogR3lHkligwPloV.json', 'var_call_GYsjmtShYsheb16Fvx5ZEBFJ': 'file_storage/call_GYsjmtShYsheb16Fvx5ZEBFJ.json'}

exec(code, env_args)
