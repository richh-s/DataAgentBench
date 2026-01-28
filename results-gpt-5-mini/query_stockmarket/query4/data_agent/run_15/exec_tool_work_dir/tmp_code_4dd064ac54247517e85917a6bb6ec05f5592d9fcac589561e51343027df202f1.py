code = """import json
# load storage file paths
stockinfo_path = var_call_wsVInw8eEyMzIoSnAVX55pOn
trade_tables_path = var_call_mf8p8wR7qUDwPcMyViiKZp7a
with open(stockinfo_path, 'r') as f:
    stockinfo = json.load(f)
with open(trade_tables_path, 'r') as f:
    trade_tables = json.load(f)
# extract symbols and map to company description
sym_to_name = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}
# intersection
symbols = [s for s in sym_to_name.keys() if s in set(trade_tables)]
# sort symbols to have deterministic order
symbols.sort()
# build UNION ALL SQL
parts = []
for s in symbols:
    # wrap table name in double quotes for DuckDB if necessary
    part = "SELECT '{sym}' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(sym=s)
    parts.append(part)
sql = " UNION ALL ".join(parts) + ";"
# output the SQL string as JSON
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_mf8p8wR7qUDwPcMyViiKZp7a': 'file_storage/call_mf8p8wR7qUDwPcMyViiKZp7a.json', 'var_call_wsVInw8eEyMzIoSnAVX55pOn': 'file_storage/call_wsVInw8eEyMzIoSnAVX55pOn.json', 'var_call_atY7Z5oy1ePQMP8fS8SVojO2': {'a': 'ok'}}

exec(code, env_args)
