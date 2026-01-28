code = """import json

# Load NYSE Arca ETF symbols
etf_file = locals().get('var_functions.query_db:0')
if etf_file and isinstance(etf_file, str):
    with open(etf_file, 'r') as openfile:
        nyse_arca_data = json.load(openfile)
else:
    nyse_arca_data = []

# Load available trading tables  
tables_file = locals().get('var_functions.list_db:2')
if tables_file and isinstance(tables_file, str):
    with open(tables_file, 'r') as openfile:
        trade_tables = json.load(openfile)
else:
    trade_tables = []

# Get valid ETFs that have price data
etf_list = []
for record in nyse_arca_data:
    sym = record.get('Symbol')
    if sym and sym in trade_tables:
        etf_list.append(sym)

# Create batch query for first 50 ETFs
batch_size = 50
queries = []
for etf_symbol in etf_list[0:batch_size]:
    query_text = "SELECT '{}' as ticker, MAX(\"Adj Close\") as max_adj_close FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(etf_symbol, etf_symbol)
    queries.append(query_text)

combined_query = " UNION ALL ".join(queries)

output_struct = {
    'total_etfs': len(etf_list),
    'batch_query': combined_query[0:300],
    'batch_symbols': etf_list[0:5]
}

print('__RESULT__:')
print(json.dumps(output_struct))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': {'nyse_arca_etf_count': 1435, 'total_tables': 2753, 'common_symbols_count': 1435, 'sample_symbols': ['VTI', 'GII', 'SPSM', 'VPU', 'FLQE', 'FXF', 'GUSH', 'SSPY', 'BIBL', 'DNL']}, 'var_functions.execute_python:10': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_symbols_to_check': 1435, 'batch_size': 50, 'batches': 29}}

exec(code, env_args)
