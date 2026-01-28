code = """import json

# Get the list of NYSE Arca ETF symbols
nyse_arca_file = locals().get('var_functions.query_db:0')
if nyse_arca_file and isinstance(nyse_arca_file, str):
    with open(nyse_arca_file, 'r') as f:
        nyse_arca_data = json.load(f)
else:
    nyse_arca_data = []

# Get all available tables from stocktrade database
tables_file = locals().get('var_functions.list_db:2')
if tables_file and isinstance(tables_file, str):
    with open(tables_file, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = []

# Filter for symbols that exist as tables in the stocktrade database
valid_symbols = []
for record in nyse_arca_data:
    symbol = record.get('Symbol')
    if symbol and symbol in trade_tables:
        valid_symbols.append(symbol)

# Build batch query for first 50 symbols
BATCH_SIZE = 50
queries = []
for i in range(min(BATCH_SIZE, len(valid_symbols))):
    symbol = valid_symbols[i]
    query_part = "SELECT '" + symbol + "' as Symbol, MAX(\"Adj Close\") as max_price FROM \"" + symbol + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    queries.append(query_part)

combined_query = " UNION ALL ".join(queries)

result = {
    'total_nyse_arca_etfs': len(nyse_arca_data),
    'symbols_with_data': len(valid_symbols),
    'batch_size': min(BATCH_SIZE, len(valid_symbols)),
    'query_preview': combined_query[:300]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_symbols_to_check': 1435, 'batch_size': 50, 'batches': 29}, 'var_functions.query_db:30': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
