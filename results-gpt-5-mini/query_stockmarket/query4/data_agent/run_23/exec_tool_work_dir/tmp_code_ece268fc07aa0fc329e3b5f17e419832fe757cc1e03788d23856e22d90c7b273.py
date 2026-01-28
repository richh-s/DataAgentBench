code = """import json
# var_call_WZq9wz2apZmrEaTu4pYKgPLZ and var_call_yscC6NObrqvHfKXNY6uFGAve are provided in storage
p1 = var_call_WZq9wz2apZmrEaTu4pYKgPLZ
p2 = var_call_yscC6NObrqvHfKXNY6uFGAve

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

stockinfo = load_json(p1)  # list of dicts with Symbol and Company Description
trade_tables = load_json(p2)  # list of table names (strings)

# Extract symbols from stockinfo
symbols_stockinfo = [rec['Symbol'] for rec in stockinfo]
# Intersection with trade tables
symbols = sorted(list(set(symbols_stockinfo).intersection(set(trade_tables))))

# Build SQL that unions counts for each symbol for 2017
union_parts = []
for s in symbols:
    # Quote table name and column names
    part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_count, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_count FROM \"{s}\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'"
    union_parts.append(part)

sql = "\nUNION ALL\n".join(union_parts)
# Wrap to filter and order
final_sql = f"SELECT symbol, up_count, down_count FROM (\n{sql}\n) AS t WHERE up_count>down_count ORDER BY up_count DESC LIMIT 5;"

output = {"sql": final_sql, "symbols_considered_count": len(symbols)}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_WZq9wz2apZmrEaTu4pYKgPLZ': 'file_storage/call_WZq9wz2apZmrEaTu4pYKgPLZ.json', 'var_call_yscC6NObrqvHfKXNY6uFGAve': 'file_storage/call_yscC6NObrqvHfKXNY6uFGAve.json'}

exec(code, env_args)
