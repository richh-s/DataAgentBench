code = """import json
# Load the large results from previous query_db and list_db calls
with open(var_call_PD6sCKvQPl7XG930NCaPdWBb, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_KBnUpk3gZ8X5OUAmIGU1w97y, 'r') as f:
    trade_tables = json.load(f)

# Extract ETF symbols from stockinfo result
etf_symbols = [rec['Symbol'] for rec in stockinfo]
# Ensure trade_tables are strings
trade_tables_set = set(trade_tables)

# Intersection: only symbols that have trading tables
symbols_to_check = [s for s in etf_symbols if s in trade_tables_set]

# Build SQL that unions MAX("Adj Close") for each symbol in 2015 and filters > 200
sql_parts = []
for s in symbols_to_check:
    part = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    sql_parts.append(part)

if sql_parts:
    sql = ' UNION ALL '.join(sql_parts) + " HAVING max_adj > 200"
    # Note: HAVING after union is not valid; instead wrap as subquery
    sql = f"SELECT Symbol, max_adj FROM ( {sql} ) WHERE max_adj > 200;"
else:
    sql = "SELECT '' AS Symbol, NULL AS max_adj WHERE 1=0;"

result = {'sql': sql, 'symbols_checked_count': len(symbols_to_check)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PD6sCKvQPl7XG930NCaPdWBb': 'file_storage/call_PD6sCKvQPl7XG930NCaPdWBb.json', 'var_call_KBnUpk3gZ8X5OUAmIGU1w97y': 'file_storage/call_KBnUpk3gZ8X5OUAmIGU1w97y.json'}

exec(code, env_args)
