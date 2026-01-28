code = """import json

# Load the NYSE Arca ETF symbols file path
etf_file = locals().get('var_functions.query_db:0')
if etf_file and isinstance(etf_file, str):
    with open(etf_file, 'r') as f:
        nyse_arca_data = json.load(f)
else:
    nyse_arca_data = []

# Load the stocktrade tables file path  
tables_file = locals().get('var_functions.list_db:2')
if tables_file and isinstance(tables_file, str):
    with open(tables_file, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = []

# Filter for ETFs that have trading data
valid_etfs = []
for item in nyse_arca_data:
    symbol = item.get('Symbol')
    if symbol and symbol in trade_tables:
        valid_etfs.append(symbol)

# Build union query for first 100 ETFs
queries = []
for i in range(min(100, len(valid_etfs))):
    symbol = valid_etfs[i]
    query = 'SELECT \'SYM\' as ticker, MAX(\"Adj Close\") as high_price FROM \"SYM\" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\''
    query = query.replace('SYM', symbol)
    queries.append(query)

union_query = ' UNION ALL '.join(queries)
filter_query = 'SELECT ticker, high_price FROM (' + union_query + ') WHERE high_price > 200'

result = {
    'valid_etf_count': len(valid_etfs),
    'preview_query': union_query[0:200] if union_query else '',
    'full_query_length': len(filter_query)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_symbols_to_check': 1435, 'batch_size': 50, 'batches': 29}}

exec(code, env_args)
