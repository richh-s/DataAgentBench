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
        f"SELECT '{s}' AS symbol, "
        f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        f"FROM main.\"{tname}\" "
        f"WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )
    selects.append(sel)

union_query = " UNION ALL ".join(selects)

print('__RESULT__:')
print(json.dumps({'union_query': union_query}))"""

env_args = {'var_call_B0vkX78HzRpZUF0Cr76ulzBO': ['stockinfo'], 'var_call_tMVXf34zuoUADRRdrSNaMUxx': 'file_storage/call_tMVXf34zuoUADRRdrSNaMUxx.json', 'var_call_e3uF1NKVRblGP7d1DTbu5E1g': 'file_storage/call_e3uF1NKVRblGP7d1DTbu5E1g.json', 'var_call_nR2eQpQ99yltdzTydmehaEfp': {'symbols_count': 234, 'first_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}}

exec(code, env_args)
