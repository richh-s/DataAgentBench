code = """import json, os

def load_maybe_path(var):
    if isinstance(var, str) and os.path.exists(var):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

rec = load_maybe_path(var_call_7L41ZFTbZeAqvr48T0bE1vD2)
symbols = rec.get('symbols', [])

selects = []
for s in symbols:
    sel = ("SELECT '" + s + "' AS Symbol, COALESCE(SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * NULLIF(\"Low\",0) THEN 1 ELSE 0 END),0) AS cnt "
           "FROM \"" + s + "\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31'")
    selects.append(sel)

if selects:
    sql = " UNION ALL ".join(selects) + " ORDER BY cnt DESC LIMIT 5;"
else:
    sql = "SELECT '' AS Symbol, 0 AS cnt WHERE false;"

out = {'sql': sql}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WieKl7aHdSZW9WQUOPcwhEKt': 'file_storage/call_WieKl7aHdSZW9WQUOPcwhEKt.json', 'var_call_VgonKm8xOr3QKnin3IPr4pvT': 'file_storage/call_VgonKm8xOr3QKnin3IPr4pvT.json', 'var_call_9kEodSYCb5yj1kZ4zEVqvNCc': {'type_stockinfo': 'list', 'len_stockinfo': 86, 'type_trade_tables': 'list', 'len_trade_tables': 2753}, 'var_call_7L41ZFTbZeAqvr48T0bE1vD2': 'file_storage/call_7L41ZFTbZeAqvr48T0bE1vD2.json'}

exec(code, env_args)
