code = """import json
with open(var_call_Fz7nm8iiM6I0EGNzHPcYwNFd, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_LPoy8phQBgl1jIZS3yMnJkIW, 'r') as f:
    trade_tables = json.load(f)

nyse_non_etf = [r['Symbol'] for r in stockinfo if r.get('Listing Exchange') == 'N' and r.get('ETF') == 'N']
symbols_to_query = [s for s in nyse_non_etf if s in trade_tables]

mapping = {}
for r in stockinfo:
    sym = r.get('Symbol')
    if sym in symbols_to_query:
        mapping[sym] = r.get('Company Description')

parts = []
for s in symbols_to_query:
    part = ("SELECT '{}' AS symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) AS up_count, "
            "SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) AS down_count FROM \"{}\" "
            "WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'").format(s, s)
    parts.append(part)
sql = "\nUNION ALL\n".join(parts) + ";"

result = {'sql': sql, 'symbols': symbols_to_query, 'mapping': mapping}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Fz7nm8iiM6I0EGNzHPcYwNFd': 'file_storage/call_Fz7nm8iiM6I0EGNzHPcYwNFd.json', 'var_call_LPoy8phQBgl1jIZS3yMnJkIW': 'file_storage/call_LPoy8phQBgl1jIZS3yMnJkIW.json', 'var_call_2WwSDgOB1DZqKq0mfuR2e9VL': 234}

exec(code, env_args)
