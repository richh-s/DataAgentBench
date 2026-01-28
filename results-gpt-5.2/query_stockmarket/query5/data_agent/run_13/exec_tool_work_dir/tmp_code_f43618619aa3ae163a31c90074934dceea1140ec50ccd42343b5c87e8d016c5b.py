code = """import json, pandas as pd

# load stockinfo query result
path_info = var_call_UNBMamz12gvCXT5WzkaUkcAA
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# load available trade tables
path_tbl = var_call_K6LcJ7mQSoeipU97uzMMhTVq
with open(path_tbl, 'r') as f:
    tbls = json.load(f)
tbl_set = set(tbls)

# restrict to symbols that have a trade table
syms = sorted(set(info_df['Symbol']).intersection(tbl_set))

# build UNION ALL query for 2019 range-exceeding days
selects = []
for s in syms:
    # quote table name for duckdb
    selects.append(
        f"SELECT '{s}' AS symbol, COUNT(*)::BIGINT AS cnt "
        f"FROM \"{s}\" "
        f"WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        f"AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL "
        f"AND (High - Low) / Low > 0.2"
    )

# If no symbols, return empty
if not selects:
    out = json.dumps([])
    print('__RESULT__:')
    print(out)
else:
    union_query = " UNION ALL ".join(selects)
    final_query = f"SELECT symbol, SUM(cnt) AS days_exceed_20pct FROM ({union_query}) t GROUP BY symbol ORDER BY days_exceed_20pct DESC, symbol ASC LIMIT 5;"
    out = json.dumps({"query": final_query, "n_symbols": len(syms)})
    print('__RESULT__:')
    print(out)"""

env_args = {'var_call_UNBMamz12gvCXT5WzkaUkcAA': 'file_storage/call_UNBMamz12gvCXT5WzkaUkcAA.json', 'var_call_K6LcJ7mQSoeipU97uzMMhTVq': 'file_storage/call_K6LcJ7mQSoeipU97uzMMhTVq.json'}

exec(code, env_args)
