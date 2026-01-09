code = """import json, pandas as pd

path_info = var_call_tMVXf34zuoUADRRdrSNaMUxx
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

path_tbl = var_call_e3uF1NKVRblGP7d1DTbu5E1g
with open(path_tbl, 'r') as f:
    tbls = json.load(f)
tbl_df = pd.DataFrame(tbls)

symbols = sorted(set(info_df['symbol']).intersection(set(tbl_df['symbol'])))

selects = []
for s in symbols:
    tname = s.replace('"','""')
    sel = (
        "SELECT '{sym}' AS symbol, "
        "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        "FROM main.\"{tbl}\" "
        "WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )
    sel = sel.format(sym=s, tbl=tname)
    selects.append(sel)

union_query = " UNION ALL ".join(selects)

print('__RESULT__:')
print(json.dumps({'symbols_count': len(symbols), 'union_query_len': len(union_query), 'first_symbols': symbols[:10]}))"""

env_args = {'var_call_B0vkX78HzRpZUF0Cr76ulzBO': ['stockinfo'], 'var_call_tMVXf34zuoUADRRdrSNaMUxx': 'file_storage/call_tMVXf34zuoUADRRdrSNaMUxx.json', 'var_call_e3uF1NKVRblGP7d1DTbu5E1g': 'file_storage/call_e3uF1NKVRblGP7d1DTbu5E1g.json'}

exec(code, env_args)
