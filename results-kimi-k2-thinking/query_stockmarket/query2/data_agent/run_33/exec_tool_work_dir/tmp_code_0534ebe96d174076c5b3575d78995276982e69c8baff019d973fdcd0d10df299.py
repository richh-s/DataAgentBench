code = """import json, duckdb

# Read the ETF list
with open('file_storage/functions.query_db:0.json', 'r') as f:
    etf_list = json.load(f)

etf_symbols = [etf['Symbol'] for etf in etf_list]
conn = duckdb.connect('file_storage/stocktrade_database.db')

high_price_etfs = []
for symbol in etf_symbols:
    try:
        query = f"SELECT MAX(\"Adj Close\") FROM \"{symbol}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
        result = conn.execute(query).fetchone()
        if result and result[0] and result[0] > 200:
            high_price_etfs.append({'symbol': symbol, 'max_price': float(result[0])})
    except:
        pass

conn.close()
high_price_etfs.sort(key=lambda x: x['max_price'], reverse=True)

print('__RESULT__:')
print(json.dumps({'count': len(high_price_etfs), 'etfs': high_price_etfs}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
