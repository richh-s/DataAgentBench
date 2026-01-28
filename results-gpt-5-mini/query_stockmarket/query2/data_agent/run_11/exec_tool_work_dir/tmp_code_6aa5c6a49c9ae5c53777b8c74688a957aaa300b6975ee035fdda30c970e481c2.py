code = """import json
# Read previous tool results file paths
with open(var_call_PD6sCKvQPl7XG930NCaPdWBb, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_KBnUpk3gZ8X5OUAmIGU1w97y, 'r') as f:
    trade_tables = json.load(f)

etf_symbols = [rec['Symbol'] for rec in stockinfo]
trade_tables_set = set(trade_tables)
symbols_to_check = [s for s in etf_symbols if s in trade_tables_set]

sql_parts = []
for s in symbols_to_check:
    part = "SELECT '" + s + "' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"" + s + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    sql_parts.append(part)

if sql_parts:
    union_sql = ' UNION ALL '.join(sql_parts)
    sql = 'SELECT Symbol, max_adj FROM ( ' + union_sql + ' ) WHERE max_adj > 200;'
else:
    sql = "SELECT '' AS Symbol, NULL AS max_adj WHERE 1=0;"

result = {'sql': sql, 'symbols_checked_count': len(symbols_to_check)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_PD6sCKvQPl7XG930NCaPdWBb': 'file_storage/call_PD6sCKvQPl7XG930NCaPdWBb.json', 'var_call_KBnUpk3gZ8X5OUAmIGU1w97y': 'file_storage/call_KBnUpk3gZ8X5OUAmIGU1w97y.json'}

exec(code, env_args)
