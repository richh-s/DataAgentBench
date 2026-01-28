code = """import json

# Load stockinfo query result and list_db result from storage
p1 = var_call_zMD84XMnjkH9UlsG24xJ8ZSe
p2 = var_call_KyzReNveROt475cBa6fObcUY

if isinstance(p1, str):
    with open(p1, 'r') as f:
        stockinfo = json.load(f)
else:
    stockinfo = p1

if isinstance(p2, str):
    with open(p2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = p2

# Extract symbols from stockinfo (already filtered to Listing Exchange = N and ETF = N)
symbols_stockinfo = set([rec['Symbol'] for rec in stockinfo if rec.get('Symbol')])
trade_tables_set = set(trade_tables)

# Intersection
symbols = sorted(symbols_stockinfo & trade_tables_set)

# Build SQL with one SELECT per symbol using UNION ALL
selects = []
for s in symbols:
    # Quote single quotes in symbol if any
    s_escaped = s.replace("'", "''")
    sel = (
        f"SELECT '{s_escaped}' AS symbol, \
         SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_days, \
         SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_days \
         FROM \"{s}\" \
         WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'"
    )
    selects.append(sel)

if not selects:
    sql = ""
else:
    sql = " UNION ALL ".join(selects)
    # Optionally filter later; we'll fetch all and process in Python

# Return the SQL string as JSON
out = json.dumps(sql)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uXvZcerR4ZItvITwGgYWUY3A': 'file_storage/call_uXvZcerR4ZItvITwGgYWUY3A.json', 'var_call_KyzReNveROt475cBa6fObcUY': 'file_storage/call_KyzReNveROt475cBa6fObcUY.json', 'var_call_zMD84XMnjkH9UlsG24xJ8ZSe': 'file_storage/call_zMD84XMnjkH9UlsG24xJ8ZSe.json'}

exec(code, env_args)
