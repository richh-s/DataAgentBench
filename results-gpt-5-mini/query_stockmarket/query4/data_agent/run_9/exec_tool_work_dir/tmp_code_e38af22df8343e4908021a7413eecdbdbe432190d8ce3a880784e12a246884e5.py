code = """import json
with open(var_call_RTQBbDkWPELjIO5FP4rkeZY2, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_09LdLcgAY8tG44YYClxlgY5J, 'r') as f:
    trade_tables = json.load(f)
symbols_stockinfo = [r['Symbol'] for r in stockinfo]
trade_set = set(trade_tables)
symbols = [s for s in symbols_stockinfo if s in trade_set]
parts = []
for s in symbols:
    part = ('SELECT "{sym}" AS symbol, SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END) AS up_days, '
            'SUM(CASE WHEN "Close"<"Open" THEN 1 ELSE 0 END) AS down_days FROM "{sym}" '
            'WHERE "Date">=\'2017-01-01\' AND "Date"<=\'2017-12-31\'').format(sym=s)
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + '\n;'
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_RTQBbDkWPELjIO5FP4rkeZY2': 'file_storage/call_RTQBbDkWPELjIO5FP4rkeZY2.json', 'var_call_09LdLcgAY8tG44YYClxlgY5J': 'file_storage/call_09LdLcgAY8tG44YYClxlgY5J.json'}

exec(code, env_args)
