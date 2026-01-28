code = """import json
# load variables
s1 = var_call_OhZ4rWYNl61yYyzGFPplZ5WS
s2 = var_call_KVY7N3JVPncrE5cHywJzTNjV

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    else:
        return v

list_stockinfo = load_var(s1)
list_trade_tables = load_var(s2)

symbols_stockinfo = [rec['Symbol'] for rec in list_stockinfo]
trade_tables = list_trade_tables

symbols = sorted(set(symbols_stockinfo) & set(trade_tables))

sql_parts = []
DQ = chr(34)
for sym in symbols:
    part = "SELECT '" + sym + "' AS symbol FROM " + DQ + sym + DQ + " WHERE " + DQ + "Date" + DQ + " >= '2015-01-01' AND " + DQ + "Date" + DQ + " <= '2015-12-31' AND " + DQ + "Adj Close" + DQ + " > 200 LIMIT 1"
    sql_parts.append(part)

sql = "\nUNION ALL\n".join(sql_parts) if sql_parts else "SELECT NULL WHERE FALSE;"

out = {"sql": sql, "symbols_checked": symbols}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_OhZ4rWYNl61yYyzGFPplZ5WS': 'file_storage/call_OhZ4rWYNl61yYyzGFPplZ5WS.json', 'var_call_KVY7N3JVPncrE5cHywJzTNjV': 'file_storage/call_KVY7N3JVPncrE5cHywJzTNjV.json'}

exec(code, env_args)
