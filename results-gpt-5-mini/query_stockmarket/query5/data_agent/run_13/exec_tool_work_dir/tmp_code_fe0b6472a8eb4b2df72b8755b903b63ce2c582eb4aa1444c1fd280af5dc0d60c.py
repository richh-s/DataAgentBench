code = """import json

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

stockinfo = load_var(var_call_obofffwTil0kays857PB0osJ)
trade_tables = load_var(var_call_GWxju3cF897Xt8p4q6hk2Rmi)

symbols_info = [r['Symbol'] for r in stockinfo if r.get('Symbol')]
trade_set = set(trade_tables)
symbols = [s for s in symbols_info if s in trade_set]

sql_parts = []
for s in symbols:
    if '"' in s:
        continue
    part = "SELECT '{}' AS Symbol, COUNT(*) AS cnt FROM \"{}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\"".format(s, s)
    sql_parts.append(part)

if sql_parts:
    sql = "\nUNION ALL\n".join(sql_parts) + "\nORDER BY cnt DESC;"
else:
    sql = ""

out = {'sql': sql, 'num_symbols': len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_obofffwTil0kays857PB0osJ': 'file_storage/call_obofffwTil0kays857PB0osJ.json', 'var_call_GWxju3cF897Xt8p4q6hk2Rmi': 'file_storage/call_GWxju3cF897Xt8p4q6hk2Rmi.json'}

exec(code, env_args)
