code = """import json, pandas as pd
path_info = var_call_tMVXf34zuoUADRRdrSNaMUxx
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# prefer name before ' - ' if present
info_df['name'] = info_df['company_name'].astype(str).str.split(' - ').str[0].str.strip()

symbols = info_df['symbol'].tolist()
chunks = [symbols[i:i+50] for i in range(0, len(symbols), 50)]
print('__RESULT__:')
print(json.dumps({'chunk_sizes':[len(c) for c in chunks], 'num_chunks': len(chunks), 'first_chunk': chunks[0]}))"""

env_args = {'var_call_B0vkX78HzRpZUF0Cr76ulzBO': ['stockinfo'], 'var_call_tMVXf34zuoUADRRdrSNaMUxx': 'file_storage/call_tMVXf34zuoUADRRdrSNaMUxx.json', 'var_call_e3uF1NKVRblGP7d1DTbu5E1g': 'file_storage/call_e3uF1NKVRblGP7d1DTbu5E1g.json', 'var_call_nR2eQpQ99yltdzTydmehaEfp': {'symbols_count': 234, 'first_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_call_WbORnp2sLRKHMl3ebNiiZQDO': {'union_query': "SELECT 'AEFC' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AIN' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AIV' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AIZP' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AJRD' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AL' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AMN' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AMP' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AMT' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM main. + tname +  WHERE Date >= '2017-01-01' AND Date < '2018", 'len': 52441}, 'var_call_FKfSJWgQ0YS52o5gDgSKdTEt': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_qBNoDDX6yMQglKvmFd4cK5LB': [{'rows_2017': '0', 'up_days': 'nan', 'down_days': 'nan'}]}

exec(code, env_args)
