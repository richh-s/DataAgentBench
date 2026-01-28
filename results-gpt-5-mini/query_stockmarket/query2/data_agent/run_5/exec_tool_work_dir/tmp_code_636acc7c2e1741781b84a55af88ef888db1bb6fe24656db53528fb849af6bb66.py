code = """import json
# Load previous tool results from storage file paths
with open(var_call_sivacHuiSgcyyLES4JY2Pmbh, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_8wxgRA4ankapzlMw4DhePGJj, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols from stockinfo_records
etf_symbols = [r['Symbol'] for r in stockinfo_records]
# trade_tables is a list of table names
trade_set = set(trade_tables)

# Compute intersection: only symbols that have a table in trade database
symbols_to_check = [s for s in etf_symbols if s in trade_set]

# Build a UNION ALL query to check which symbols had Adj Close > 200 in 2015
subqueries = []
for s in symbols_to_check:
    # Escape double quotes in symbol if any (symbols shouldn't contain quotes)
    sub = f"SELECT '{s}' AS Symbol FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    subqueries.append(sub)

if not subqueries:
    query = ''
else:
    query = '\nUNION ALL\n'.join(subqueries) + ';'

output = {'num_etf_symbols_in_trade_db': len(symbols_to_check), 'num_subqueries': len(subqueries), 'query': query}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_sivacHuiSgcyyLES4JY2Pmbh': 'file_storage/call_sivacHuiSgcyyLES4JY2Pmbh.json', 'var_call_8wxgRA4ankapzlMw4DhePGJj': 'file_storage/call_8wxgRA4ankapzlMw4DhePGJj.json'}

exec(code, env_args)
