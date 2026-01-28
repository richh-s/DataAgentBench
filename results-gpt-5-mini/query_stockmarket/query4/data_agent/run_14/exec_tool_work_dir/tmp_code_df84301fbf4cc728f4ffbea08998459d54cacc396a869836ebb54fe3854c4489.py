code = """import json
with open(var_call_B94K0khwE25FYcdJAC9uOdh6, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_NQ5Ham37xJsRiDqZHYYtyUqb, 'r') as f:
    trade_tables = json.load(f)

symbols_info = [rec['Symbol'] for rec in stockinfo]
trade_set = set(trade_tables)
common_symbols = [s for s in symbols_info if s in trade_set]
common_symbols.sort()

selects = []
for s in common_symbols:
    part = ('SELECT "{sym}" AS sym, '
            'SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END) AS up, '
            'SUM(CASE WHEN "Close"<"Open" THEN 1 ELSE 0 END) AS down '
            'FROM "{sym}" '
            "WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'")
    part = part.format(sym=s)
    selects.append(part)

full_query = "\nUNION ALL\n".join(selects)
# Wrap to order by difference
full_query = "SELECT sym, SUM(up) as up, SUM(down) as down FROM (\n" + full_query + "\n) AS t GROUP BY sym ORDER BY (up - down) DESC;"

print('__RESULT__:')
print(json.dumps(full_query))"""

env_args = {'var_call_B94K0khwE25FYcdJAC9uOdh6': 'file_storage/call_B94K0khwE25FYcdJAC9uOdh6.json', 'var_call_NQ5Ham37xJsRiDqZHYYtyUqb': 'file_storage/call_NQ5Ham37xJsRiDqZHYYtyUqb.json'}

exec(code, env_args)
