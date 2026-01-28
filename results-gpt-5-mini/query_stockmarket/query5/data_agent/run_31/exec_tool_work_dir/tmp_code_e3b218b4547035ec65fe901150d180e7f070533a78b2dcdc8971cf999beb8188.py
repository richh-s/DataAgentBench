code = """import json
with open(var_call_Ukj7TVJicBB40tkmvqenGyBx) as f:
    stock_s = json.load(f)
with open(var_call_5ITtwdMNsU1VtppAgfjRubYb) as f:
    trade_tables = json.load(f)
sym_to_comp = {rec['Symbol']: rec['Company Description'] for rec in stock_s}
symbols = [s for s in sym_to_comp.keys() if s in trade_tables]
parts = []
for s in symbols:
    part = "SELECT '{}' AS symbol, COUNT(*) AS cnt FROM \"{}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low)/Low > 0.2".format(s, s)
    parts.append(part)
if parts:
    union_sql = "\nUNION ALL\n".join(parts)
    sql = "SELECT symbol, cnt FROM (\n" + union_sql + "\n) ORDER BY cnt DESC LIMIT 5;"
else:
    sql = "SELECT '' AS symbol, 0 AS cnt WHERE false;"
output = {'sql': sql}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_5ITtwdMNsU1VtppAgfjRubYb': 'file_storage/call_5ITtwdMNsU1VtppAgfjRubYb.json', 'var_call_Ukj7TVJicBB40tkmvqenGyBx': 'file_storage/call_Ukj7TVJicBB40tkmvqenGyBx.json'}

exec(code, env_args)
