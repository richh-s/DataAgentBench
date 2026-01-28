code = """import json
etf_symbols = json.load(open(var_call_vx11m3QWslYyh6hwWLDiNRzH))
trade_tables = json.load(open(var_call_7SX4OTiie9zyF0VBnTgJFMJl))
common = sorted([s for s in etf_symbols if s in trade_tables])
parts = []
for s in common:
    part = "SELECT '{}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'".format(s, s)
    parts.append(part)
sql = " UNION ALL ".join(parts)
wrapped_sql = "SELECT Symbol, max_adj FROM ( {} ) WHERE max_adj > 200 ORDER BY Symbol;".format(sql)
print("__RESULT__:")
print(json.dumps({"sql": wrapped_sql, "count_tables_considered": len(common)}))"""

env_args = {'var_call_Sl50zQtw5dxdaDLjE4E9ejzh': ['stockinfo'], 'var_call_l7OaIGTJy1Lsdgg6paZF0Mtd': 'file_storage/call_l7OaIGTJy1Lsdgg6paZF0Mtd.json', 'var_call_vx11m3QWslYyh6hwWLDiNRzH': 'file_storage/call_vx11m3QWslYyh6hwWLDiNRzH.json', 'var_call_7SX4OTiie9zyF0VBnTgJFMJl': 'file_storage/call_7SX4OTiie9zyF0VBnTgJFMJl.json'}

exec(code, env_args)
