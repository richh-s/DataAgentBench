code = """import json
p1 = var_call_WZq9wz2apZmrEaTu4pYKgPLZ
p2 = var_call_yscC6NObrqvHfKXNY6uFGAve

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

stockinfo = load_json(p1)
trade_tables = load_json(p2)

symbols_stockinfo = [rec['Symbol'] for rec in stockinfo]
symbols = sorted(list(set(symbols_stockinfo).intersection(set(trade_tables))))

union_parts = []
for s in symbols:
    part = ('SELECT \'{sym}\' AS symbol, SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END) AS up_count, '
            'SUM(CASE WHEN "Close"<"Open" THEN 1 ELSE 0 END) AS down_count FROM "{sym}" '
            'WHERE "Date">=\'2017-01-01\' AND "Date"<=\'2017-12-31\'').format(sym=s)
    union_parts.append(part)

sql = "\nUNION ALL\n".join(union_parts)
final_sql = ('SELECT symbol, up_count, down_count FROM (\n' + sql + '\n) AS t '
             'WHERE up_count>down_count ORDER BY up_count DESC LIMIT 5;')

output = {"sql": final_sql, "symbols_considered_count": len(symbols)}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_WZq9wz2apZmrEaTu4pYKgPLZ': 'file_storage/call_WZq9wz2apZmrEaTu4pYKgPLZ.json', 'var_call_yscC6NObrqvHfKXNY6uFGAve': 'file_storage/call_yscC6NObrqvHfKXNY6uFGAve.json'}

exec(code, env_args)
