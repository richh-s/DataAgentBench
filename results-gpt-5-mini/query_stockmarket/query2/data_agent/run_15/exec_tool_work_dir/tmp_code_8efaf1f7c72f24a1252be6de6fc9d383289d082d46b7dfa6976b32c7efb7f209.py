code = """import json
# load ETF symbols from stockinfo query result
etf_symbols = json.load(open(var_call_vx11m3QWslYyh6hwWLDiNRzH))
# load trade DB table list
trade_tables = json.load(open(var_call_7SX4OTiie9zyF0VBnTgJFMJl))
# compute intersection
common = sorted([s for s in etf_symbols if s in trade_tables])
# build SQL
parts = []
for s in common:
    part = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'"
    parts.append(part)
sql = " UNION ALL ".join(parts)
wrapped_sql = f"SELECT Symbol, max_adj FROM ( {sql} ) WHERE max_adj > 200 ORDER BY Symbol;"
# print result as JSON string
print("__RESULT__:")
print(json.dumps({"sql": wrapped_sql, "count_tables_considered": len(common)}))"""

env_args = {'var_call_Sl50zQtw5dxdaDLjE4E9ejzh': ['stockinfo'], 'var_call_l7OaIGTJy1Lsdgg6paZF0Mtd': 'file_storage/call_l7OaIGTJy1Lsdgg6paZF0Mtd.json', 'var_call_vx11m3QWslYyh6hwWLDiNRzH': 'file_storage/call_vx11m3QWslYyh6hwWLDiNRzH.json', 'var_call_7SX4OTiie9zyF0VBnTgJFMJl': 'file_storage/call_7SX4OTiie9zyF0VBnTgJFMJl.json'}

exec(code, env_args)
