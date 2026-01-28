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
    sel = "SELECT '{sym}' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main.\"{tbl}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'".format(sym=s, tbl=tname)
    selects.append(sel)

union_query = " UNION ALL ".join(selects)
print('__RESULT__:')
print(json.dumps({'union_query': union_query, 'len': len(union_query)}))"""

env_args = {'var_call_B0vkX78HzRpZUF0Cr76ulzBO': ['stockinfo'], 'var_call_tMVXf34zuoUADRRdrSNaMUxx': 'file_storage/call_tMVXf34zuoUADRRdrSNaMUxx.json', 'var_call_e3uF1NKVRblGP7d1DTbu5E1g': 'file_storage/call_e3uF1NKVRblGP7d1DTbu5E1g.json', 'var_call_nR2eQpQ99yltdzTydmehaEfp': {'symbols_count': 234, 'first_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_call_WbORnp2sLRKHMl3ebNiiZQDO': {'union_query': "SELECT 'AEFC' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AIN' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AIV' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AIZP' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AJRD' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AL' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AMN' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AMP' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AMT' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018", 'len': 52441}}

exec(code, env_args)
