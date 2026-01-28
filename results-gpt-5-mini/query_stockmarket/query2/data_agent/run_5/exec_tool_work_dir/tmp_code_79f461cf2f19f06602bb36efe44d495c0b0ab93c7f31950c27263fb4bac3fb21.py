code = """import json
with open(var_call_sivacHuiSgcyyLES4JY2Pmbh, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_8wxgRA4ankapzlMw4DhePGJj, 'r') as f:
    trade_tables = json.load(f)

etf_symbols = [r['Symbol'] for r in stockinfo_records]
trade_set = set(trade_tables)
symbols = [s for s in etf_symbols if s in trade_set]

subs = []
for s in symbols:
    tbl = '"' + s + '"'
    col = '"Adj Close"'
    sub = "SELECT '{}' AS Symbol FROM {} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND {} > 200 LIMIT 1".format(s, tbl, col)
    subs.append(sub)

query = ('\nUNION ALL\n'.join(subs) + ';') if subs else ''
output = {'query': query, 'num_symbols': len(symbols)}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_sivacHuiSgcyyLES4JY2Pmbh': 'file_storage/call_sivacHuiSgcyyLES4JY2Pmbh.json', 'var_call_8wxgRA4ankapzlMw4DhePGJj': 'file_storage/call_8wxgRA4ankapzlMw4DhePGJj.json', 'var_call_GM4b9XWbZdjPKEghYXIfgFyD': {'has_SPY': True, 'total_etfs': 1435}}

exec(code, env_args)
