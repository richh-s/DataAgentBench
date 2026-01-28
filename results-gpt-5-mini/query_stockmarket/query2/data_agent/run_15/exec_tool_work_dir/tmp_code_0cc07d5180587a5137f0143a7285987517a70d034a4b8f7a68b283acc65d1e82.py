code = """import json
etf_symbols = json.load(open(var_call_vx11m3QWslYyh6hwWLDiNRzH))
trade_tables = json.load(open(var_call_7SX4OTiie9zyF0VBnTgJFMJl))
common = sorted([s for s in etf_symbols if s in trade_tables])
parts = []
for s in common:
    # quote symbol for SQL literal and table name
    parts.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'")
sql = " UNION ALL ".join(parts)
wrapped_sql = f"SELECT Symbol, max_adj FROM ( {sql} ) WHERE max_adj > 200 ORDER BY Symbol;"
output = {"sql": wrapped_sql, "count_tables_considered": len(common)}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Sl50zQtw5dxdaDLjE4E9ejzh': ['stockinfo'], 'var_call_l7OaIGTJy1Lsdgg6paZF0Mtd': 'file_storage/call_l7OaIGTJy1Lsdgg6paZF0Mtd.json', 'var_call_vx11m3QWslYyh6hwWLDiNRzH': 'file_storage/call_vx11m3QWslYyh6hwWLDiNRzH.json', 'var_call_7SX4OTiie9zyF0VBnTgJFMJl': 'file_storage/call_7SX4OTiie9zyF0VBnTgJFMJl.json', 'var_call_r6sc3gyUY0F5Khf1D1m5tPuc': {'len_a': 1435, 'len_b': 2753}}

exec(code, env_args)
