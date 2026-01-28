code = """import json

# Load the symbols and tables
nyse_arca_file = locals().get('var_functions.query_db:0')
tables_file = locals().get('var_functions.list_db:2')

with open(nyse_arca_file, 'r') as f:
    nyse_arca_data = json.load(f)
with open(tables_file, 'r') as f:
    trade_tables = json.load(f)

# Get valid symbols (NYSE Arca ETFs with price data)
valid_symbols = []
for record in nyse_arca_data:
    symbol = record['Symbol']
    if symbol in trade_tables:
        valid_symbols.append(symbol)

# Build a query to check all symbols at once using UNION ALL
queries = []
for symbol in valid_symbols:
    query_part = "SELECT '" + symbol + "' as Symbol, MAX(\"Adj Close\") as max_adj_close FROM \"" + symbol + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    queries.append(query_part)

combined_query = " UNION ALL ".join(queries)
final_query = "SELECT Symbol, max_adj_close FROM (" + combined_query + ") WHERE max_adj_close > 200"

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(valid_symbols),
    'query_length': len(final_query)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_symbols_to_check': 1435, 'batch_size': 50, 'batches': 29}, 'var_functions.query_db:30': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'valid_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
