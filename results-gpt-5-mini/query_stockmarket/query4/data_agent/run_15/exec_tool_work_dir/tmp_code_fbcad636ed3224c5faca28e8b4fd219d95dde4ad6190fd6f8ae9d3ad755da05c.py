code = """import json
# load previous tool results from storage variables
with open(var_call_wsVInw8eEyMzIoSnAVX55pOn, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_mf8p8wR7qUDwPcMyViiKZp7a, 'r') as f:
    trade_tables = json.load(f)
# extract symbols from stockinfo results
symbols = [rec['Symbol'] for rec in stockinfo]
# intersect with trade_tables
trade_set = set(trade_tables)
symbols_in_trade = [s for s in symbols if s in trade_set]
# build union SQL for 2017 counts
parts = []
for s in symbols_in_trade:
    part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    parts.append(part)
sql = " UNION ALL ".join(parts) + ";"
result = json.dumps(sql)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_mf8p8wR7qUDwPcMyViiKZp7a': 'file_storage/call_mf8p8wR7qUDwPcMyViiKZp7a.json', 'var_call_wsVInw8eEyMzIoSnAVX55pOn': 'file_storage/call_wsVInw8eEyMzIoSnAVX55pOn.json'}

exec(code, env_args)
