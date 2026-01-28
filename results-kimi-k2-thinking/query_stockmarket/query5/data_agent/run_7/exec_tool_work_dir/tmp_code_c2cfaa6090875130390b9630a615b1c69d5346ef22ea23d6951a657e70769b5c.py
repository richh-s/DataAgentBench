code = """import json
# Load tickers
with open('file_storage/functions.query_db:18.json', 'r') as f:
    stockinfo_data = json.load(f)
symbols = [rec['Symbol'] for rec in stockinfo_data]
# Load tables
with open('file_storage/functions.list_db:2.json', 'r') as f:
    tables = json.load(f)
common = [s for s in symbols if s in tables]

# Build union query
parts = []
for sym in common:
    # Quote table name with double quotes
    parts.append("SELECT '" + sym + "' as symbol, COUNT(*) as cnt FROM \"" + sym + "\" WHERE STRFTIME('%Y', Date) = '2019' AND (\"High\" - \"Low\") > 0.2 * \"Low\"")
union_query = "\nUNION ALL\n".join(parts)
full_query = f"WITH sub AS ({union_query})\nSELECT symbol, cnt FROM sub ORDER BY cnt DESC LIMIT 5"
print('__RESULT__:')
print(full_query)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:8': {'p1': 'file_storage/functions.query_db:0.json', 'p2': 'file_storage/functions.list_db:2.json'}, 'var_functions.execute_python:10': {'symbol_count': 86, 'table_count': 2753, 'common_count': 86}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
