code = """import json
# Load the results from previous tool calls stored as file paths
with open(var_call_WaEvCHYDu8q5PYvnJxAh1X2s, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_C9yV3KAORv9nL5ONxiYWO0Ud, 'r') as f:
    trade_tables = json.load(f)
# Extract ETF symbols listed on NYSE Arca from stockinfo result
symbols = [r['Symbol'] for r in stockinfo]
# Compute intersection with available trade tables
available_symbols = [s for s in symbols if s in trade_tables]
# Build SQL that checks max Adj Close in 2015 for each available symbol and returns those with max>200
selects = []
for s in available_symbols:
    # quote table name
    tbl = '"%s"' % s
    sel = f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj FROM {tbl} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MAX(\"Adj Close\") > 200"
    selects.append(sel)
if selects:
    sql = '\nUNION ALL\n'.join(selects) + '\nORDER BY symbol;'
else:
    sql = ''
result = {'symbols_count_checked': len(available_symbols), 'symbols_checked': available_symbols, 'sql': sql}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7unxnarEaWwSx7trThvVwizq': ['stockinfo'], 'var_call_WaEvCHYDu8q5PYvnJxAh1X2s': 'file_storage/call_WaEvCHYDu8q5PYvnJxAh1X2s.json', 'var_call_C9yV3KAORv9nL5ONxiYWO0Ud': 'file_storage/call_C9yV3KAORv9nL5ONxiYWO0Ud.json'}

exec(code, env_args)
