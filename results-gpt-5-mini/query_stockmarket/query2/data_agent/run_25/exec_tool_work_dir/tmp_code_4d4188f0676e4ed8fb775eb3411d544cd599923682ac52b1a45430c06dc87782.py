code = """import json
s1 = var_call_OhZ4rWYNl61yYyzGFPplZ5WS
s2 = var_call_KVY7N3JVPncrE5cHywJzTNjV

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

list_stockinfo = load_var(s1)
list_trade_tables = load_var(s2)

symbols_stockinfo = [r['Symbol'] for r in list_stockinfo]
trade_tables = list_trade_tables

symbols = sorted(set(symbols_stockinfo) & set(trade_tables))

parts = []
for sym in symbols:
    part = "SELECT '" + sym + "' AS symbol FROM \"" + sym + "\" WHERE \"Date\">='2015-01-01' AND \"Date\"<='2015-12-31' AND \"Adj Close\">200 LIMIT 1"
    parts.append(part)

sql = "\nUNION ALL\n".join(parts) if parts else "SELECT NULL WHERE FALSE;"

out = {"sql": sql, "symbols_checked": symbols}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_OhZ4rWYNl61yYyzGFPplZ5WS': 'file_storage/call_OhZ4rWYNl61yYyzGFPplZ5WS.json', 'var_call_KVY7N3JVPncrE5cHywJzTNjV': 'file_storage/call_KVY7N3JVPncrE5cHywJzTNjV.json'}

exec(code, env_args)
