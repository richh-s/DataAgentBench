code = """import json, pandas as pd

# Load stockinfo NYSE non-ETF symbols
path_info = var_call_tMVXf34zuoUADRRdrSNaMUxx
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# Load trade tables list
path_tbl = var_call_e3uF1NKVRblGP7d1DTbu5E1g
with open(path_tbl, 'r') as f:
    tbls = json.load(f)
tbl_df = pd.DataFrame(tbls)

# Intersection symbols present in trade db
symbols = sorted(set(info_df['symbol']).intersection(set(tbl_df['symbol'])))

# limit to a reasonable count (all should be manageable)
# Create SQL that unions per-table counts for 2017 up/down days
selects = []
for s in symbols:
    # DuckDB identifiers: quote with double quotes; but tables are in main and may include special chars.
    tname = s.replace('"','""')
    sel = f"SELECT '{s}' AS symbol, " \
          f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, " \
          f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days " \
          f"FROM main.\"{tname}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    selects.append(sel)

query = "\nUNION ALL\n".join(selects)

# Return query string so we can run it in query_db next
out = json.dumps({'symbols_count': len(symbols), 'union_query': query[:5000], 'union_query_len': len(query)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_B0vkX78HzRpZUF0Cr76ulzBO': ['stockinfo'], 'var_call_tMVXf34zuoUADRRdrSNaMUxx': 'file_storage/call_tMVXf34zuoUADRRdrSNaMUxx.json', 'var_call_e3uF1NKVRblGP7d1DTbu5E1g': 'file_storage/call_e3uF1NKVRblGP7d1DTbu5E1g.json'}

exec(code, env_args)
