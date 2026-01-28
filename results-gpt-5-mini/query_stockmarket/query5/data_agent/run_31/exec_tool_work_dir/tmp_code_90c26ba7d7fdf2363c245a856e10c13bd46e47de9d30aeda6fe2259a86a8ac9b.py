code = """import json
# Load stockinfo 'S' query result
with open(var_call_Ukj7TVJicBB40tkmvqenGyBx) as f:
    stock_s = json.load(f)
# Load list of trade tables
with open(var_call_5ITtwdMNsU1VtppAgfjRubYb) as f:
    trade_tables = json.load(f)
# Build symbol -> company mapping for Market Category S
sym_to_comp = {rec['Symbol']: rec['Company Description'] for rec in stock_s}
# Intersection with trade_tables
symbols = [s for s in sym_to_comp.keys() if s in trade_tables]
# If no symbols, produce empty
if not symbols:
    sql = "SELECT '' AS symbol, 0 AS cnt WHERE false;"
else:
    parts = []
    for s in symbols:
        part = f"SELECT '{s}' AS symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low)/Low > 0.2"
        parts.append(part)
    union_sql = "\nUNION ALL\n".join(parts)
    sql = f"SELECT symbol, cnt FROM (\n{union_sql}\n) ORDER BY cnt DESC LIMIT 5;"
output = {'sql': sql, 'mapping': sym_to_comp}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_5ITtwdMNsU1VtppAgfjRubYb': 'file_storage/call_5ITtwdMNsU1VtppAgfjRubYb.json', 'var_call_Ukj7TVJicBB40tkmvqenGyBx': 'file_storage/call_Ukj7TVJicBB40tkmvqenGyBx.json'}

exec(code, env_args)
