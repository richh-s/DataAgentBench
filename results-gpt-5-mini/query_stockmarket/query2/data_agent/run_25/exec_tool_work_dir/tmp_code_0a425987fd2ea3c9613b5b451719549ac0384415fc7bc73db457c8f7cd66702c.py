code = """import json
# Read previous tool results from storage variables
s1 = var_call_OhZ4rWYNl61yYyzGFPplZ5WS
s2 = var_call_KVY7N3JVPncrE5cHywJzTNjV

def load_var(v):
    if isinstance(v, str):
        # it's a file path to a JSON file
        with open(v, 'r') as f:
            return json.load(f)
    else:
        return v

list_stockinfo = load_var(s1)
list_trade_tables = load_var(s2)

# extract symbols from stockinfo records
symbols_stockinfo = [rec['Symbol'] for rec in list_stockinfo]
# trade tables is a list of table names
trade_tables = list_trade_tables

# compute intersection
symbols_set = set(symbols_stockinfo) & set(trade_tables)
symbols = sorted(symbols_set)

# build SQL that unions selects for each symbol checking Adj Close > 200 in 2015
# Use Date comparison strings
sql_parts = []
for sym in symbols:
    # double-quote the table name (DuckDB)
    part = f"SELECT '{sym}' AS symbol FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    sql_parts.append(part)

if not sql_parts:
    sql = "SELECT NULL WHERE FALSE;"
else:
    sql = "\nUNION ALL\n".join(sql_parts)

out = {"candidate_count": len(symbols), "symbols_checked": symbols, "query": sql}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_OhZ4rWYNl61yYyzGFPplZ5WS': 'file_storage/call_OhZ4rWYNl61yYyzGFPplZ5WS.json', 'var_call_KVY7N3JVPncrE5cHywJzTNjV': 'file_storage/call_KVY7N3JVPncrE5cHywJzTNjV.json'}

exec(code, env_args)
