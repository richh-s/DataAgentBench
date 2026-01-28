code = """import json
import os

# Load ETF symbols from file
symbols_file = locals().get('var_functions.query_db:8')
with open(symbols_file, 'r') as f:
    etf_list = json.load(f)

symbols = [item['Symbol'] for item in etf_list]

# Build the large query
query_parts = []
for symbol in symbols:
    # Escape single quotes in symbol (though unlikely)
    safe_symbol = symbol.replace("'", "''")
    part = f"SELECT DISTINCT '{safe_symbol}' AS Symbol FROM \"{safe_symbol}\" WHERE \"Adj Close\" > 200 AND Date BETWEEN '2015-01-01' AND '2015-12-31'"
    query_parts.append(part)

full_query = " UNION ALL ".join(query_parts) + ";"

# Write query to a file for debugging if needed
# For now, just output the query length and a snippet
print('__RESULT__:')
print(json.dumps({
    'query_length': len(full_query),
    'snippet': full_query[:500]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'count': 1435, 'sample': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
