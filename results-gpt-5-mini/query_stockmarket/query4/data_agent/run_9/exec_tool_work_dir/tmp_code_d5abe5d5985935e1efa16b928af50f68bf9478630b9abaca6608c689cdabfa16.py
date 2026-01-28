code = """import json
# load storage entries
with open(var_call_RTQBbDkWPELjIO5FP4rkeZY2, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_09LdLcgAY8tG44YYClxlgY5J, 'r') as f:
    trade_tables = json.load(f)
# extract symbols from stockinfo result
symbols_stockinfo = [r['Symbol'] for r in stockinfo]
# intersect with available trade tables
trade_set = set(trade_tables)
symbols = [s for s in symbols_stockinfo if s in trade_set]
# build SQL union query for 2017 counts
parts = []
for s in symbols:
    # safe table name quoting
    part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_days FROM \"{s}\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'"
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + '\n;'
# print result in required format
print("__RESULT__:")
print(sql)"""

env_args = {'var_call_RTQBbDkWPELjIO5FP4rkeZY2': 'file_storage/call_RTQBbDkWPELjIO5FP4rkeZY2.json', 'var_call_09LdLcgAY8tG44YYClxlgY5J': 'file_storage/call_09LdLcgAY8tG44YYClxlgY5J.json'}

exec(code, env_args)
