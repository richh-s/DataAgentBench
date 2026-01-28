code = """import json

# Load NYSE Arca ETF symbols
nyse_arca_file = locals().get('var_functions.query_db:0', '')
if nyse_arca_file and not isinstance(nyse_arca_file, list):
    with open(nyse_arca_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = nyse_arca_file if isinstance(nyse_arca_file, list) else []

# Get available tables
all_tables_file = locals().get('var_functions.list_db:2', '')
if all_tables_file and not isinstance(all_tables_file, list):
    with open(all_tables_file, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_file if isinstance(all_tables_file, list) else []

# Filter for symbols that exist as tables
valid_symbols = [etf['Symbol'] for etf in nyse_arca_etfs if etf['Symbol'] in all_tables]

# Create SQL query to check for 2015 high prices above $200
queries = []
for symbol in valid_symbols[:50]:
    query_part = 'SELECT \'' + symbol + '\' as Symbol, MAX("Adj Close") as max_price FROM "' + symbol + '" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\''
    queries.append(query_part)

final_query = ' UNION ALL '.join(queries)

result_data = {
    'query_preview': final_query[:200] if final_query else '',
    'symbols_processed': len(queries)
}
print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_symbols_to_check': 1435, 'batch_size': 50, 'batches': 29}}

exec(code, env_args)
