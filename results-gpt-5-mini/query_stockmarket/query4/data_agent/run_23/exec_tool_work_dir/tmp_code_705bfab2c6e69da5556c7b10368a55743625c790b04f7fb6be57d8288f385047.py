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
    part = ('''SELECT '{sym}' AS symbol, SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END) AS up_count, """
            """
            .replace('\n',''))
    # The above is placeholder to avoid syntax issues

print("__RESULT__:")
print(json.dumps({'symbols_count': len(symbols)}))"""

env_args = {'var_call_WZq9wz2apZmrEaTu4pYKgPLZ': 'file_storage/call_WZq9wz2apZmrEaTu4pYKgPLZ.json', 'var_call_yscC6NObrqvHfKXNY6uFGAve': 'file_storage/call_yscC6NObrqvHfKXNY6uFGAve.json'}

exec(code, env_args)
