code = """import json
# Load stockinfo list and stocktrade tables list from storage-provided file paths
with open(var_call_p3wehT7WbD92Ab0NJaPpAfGD, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_Brv828NQIaemUxAB6OfCNpOc, 'r') as f:
    trade_tables = json.load(f)
# Build mapping for Market Category S (already filtered in query result)
mapping = {item['Symbol']: item.get('Company Description','') for item in stockinfo}
# Find symbols present in both mapping and trade_tables
symbols = sorted([s for s in mapping.keys() if s in trade_tables])
# Build UNION ALL SQL for DuckDB (stocktrade_database). Use double quotes for table and column names.
parts = []
for sym in symbols:
    part = f"SELECT '{sym}' AS symbol, COUNT(*) AS cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\""
    parts.append(part)
if not parts:
    sql = ''
else:
    sql = ' UNION ALL '.join(parts) + ' ORDER BY cnt DESC LIMIT 10;'
output = {'sql': sql, 'mapping': mapping, 'symbols_count': len(symbols)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_p3wehT7WbD92Ab0NJaPpAfGD': 'file_storage/call_p3wehT7WbD92Ab0NJaPpAfGD.json', 'var_call_Brv828NQIaemUxAB6OfCNpOc': 'file_storage/call_Brv828NQIaemUxAB6OfCNpOc.json'}

exec(code, env_args)
