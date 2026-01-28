code = """import json
p_stock = var_call_Ukj7TVJicBB40tkmvqenGyBx
with open(p_stock) as f:
    stock_s = json.load(f)
p_trade = var_call_5ITtwdMNsU1VtppAgfjRubYb
with open(p_trade) as f:
    trade_tables = json.load(f)
# map symbols for Market Category S
sym_to_comp = {rec['Symbol']: rec['Company Description'] for rec in stock_s}
symbols = [s for s in sym_to_comp.keys() if s in trade_tables]
# build SQL
parts = []
for s in symbols:
    # use double quotes around table name
    parts.append("SELECT '{}' AS symbol, COUNT(*) AS cnt FROM \"{}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low)/Low > 0.2".format(s, s))
if parts:
    union_sql = "\nUNION ALL\n".join(parts)
    sql = "SELECT symbol, cnt FROM (\n" + union_sql + "\n) ORDER BY cnt DESC LIMIT 5;"
else:
    sql = "SELECT '' AS symbol, 0 AS cnt WHERE false;"
out = {'sql': sql, 'n_symbols': len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_5ITtwdMNsU1VtppAgfjRubYb': 'file_storage/call_5ITtwdMNsU1VtppAgfjRubYb.json', 'var_call_Ukj7TVJicBB40tkmvqenGyBx': 'file_storage/call_Ukj7TVJicBB40tkmvqenGyBx.json', 'var_call_JjKrgSqh4gfIUOF4WM1EfHvX': {'n_symbols': 86, 'symbols_head': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}}

exec(code, env_args)
