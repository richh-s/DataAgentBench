code = """import json
# load storage-provided variables
with open(var_call_Fz7nm8iiM6I0EGNzHPcYwNFd, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_LPoy8phQBgl1jIZS3yMnJkIW, 'r') as f:
    trade_tables = json.load(f)

# Filter NYSE non-ETF symbols from stockinfo
nyse_non_etf = [r['Symbol'] for r in stockinfo if r.get('Listing Exchange') == 'N' and r.get('ETF') == 'N']
# Ensure symbols present in trade_tables
symbols_to_query = [s for s in nyse_non_etf if s in trade_tables]

# Build a single SQL query that unions counts for each symbol for 2017
parts = []
for s in symbols_to_query:
    part = "SELECT '{}' AS symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) AS up_count, SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) AS down_count FROM \"{}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(s, s)
    parts.append(part)
sql = "\nUNION ALL\n".join(parts) + ";"

result = {'sql': sql, 'count_symbols': len(symbols_to_query)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Fz7nm8iiM6I0EGNzHPcYwNFd': 'file_storage/call_Fz7nm8iiM6I0EGNzHPcYwNFd.json', 'var_call_LPoy8phQBgl1jIZS3yMnJkIW': 'file_storage/call_LPoy8phQBgl1jIZS3yMnJkIW.json'}

exec(code, env_args)
