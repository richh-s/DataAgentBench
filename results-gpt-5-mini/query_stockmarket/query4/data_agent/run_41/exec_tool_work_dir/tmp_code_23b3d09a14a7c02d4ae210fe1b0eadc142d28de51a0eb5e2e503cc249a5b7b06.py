code = """import json
with open(var_call_Fz7nm8iiM6I0EGNzHPcYwNFd, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_LPoy8phQBgl1jIZS3yMnJkIW, 'r') as f:
    trade_tables = json.load(f)

nyse_non_etf = [r['Symbol'] for r in stockinfo if r.get('Listing Exchange') == 'N' and r.get('ETF') == 'N']
symbols_to_query = [s for s in nyse_non_etf if s in trade_tables]

parts = []
for s in symbols_to_query:
    part = (
        "SELECT '{sym}' AS symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) AS up_count, "
        "SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) AS down_count "
        "FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    ).format(sym=s)
    parts.append(part)
sql = "\nUNION ALL\n".join(parts) + ";"

result = {'sql': sql, 'num_symbols': len(symbols_to_query)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Fz7nm8iiM6I0EGNzHPcYwNFd': 'file_storage/call_Fz7nm8iiM6I0EGNzHPcYwNFd.json', 'var_call_LPoy8phQBgl1jIZS3yMnJkIW': 'file_storage/call_LPoy8phQBgl1jIZS3yMnJkIW.json', 'var_call_2WwSDgOB1DZqKq0mfuR2e9VL': 234, 'var_call_m6fu3JmM8SGvqnsDlgLoVlZS': {'count': 234, 'symbols_sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT']}}

exec(code, env_args)
