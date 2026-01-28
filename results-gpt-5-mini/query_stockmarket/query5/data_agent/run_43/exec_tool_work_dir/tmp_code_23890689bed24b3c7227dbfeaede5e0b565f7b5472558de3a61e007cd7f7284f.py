code = """import json
import os

def load_maybe_path(var):
    if isinstance(var, str) and os.path.exists(var):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

stockinfo_records = load_maybe_path(var_call_WieKl7aHdSZW9WQUOPcwhEKt)
trade_tables = load_maybe_path(var_call_VgonKm8xOr3QKnin3IPr4pvT)

sym_to_company = {}
for rec in stockinfo_records:
    sym = rec.get('Symbol')
    desc = rec.get('Company Description')
    if sym:
        sym_to_company[sym.upper()] = desc

available_tables = [t.upper() for t in trade_tables]

symbols = sorted([s for s in sym_to_company.keys() if s in available_tables])

selects = []
for s in symbols:
    sel = ("SELECT '" + s + "' AS Symbol, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * \"Low\" THEN 1 ELSE 0 END) AS cnt "
           "FROM \"" + s + "\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31'")
    selects.append(sel)

if selects:
    sql = " UNION ALL ".join(selects) + " ORDER BY cnt DESC;"
else:
    sql = "SELECT '' AS Symbol, 0 AS cnt WHERE false;"

out = {
    'sql': sql,
    'num_symbols': len(symbols),
    'symbols_sample': symbols[:20],
    'mapping_count': len(sym_to_company)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WieKl7aHdSZW9WQUOPcwhEKt': 'file_storage/call_WieKl7aHdSZW9WQUOPcwhEKt.json', 'var_call_VgonKm8xOr3QKnin3IPr4pvT': 'file_storage/call_VgonKm8xOr3QKnin3IPr4pvT.json'}

exec(code, env_args)
