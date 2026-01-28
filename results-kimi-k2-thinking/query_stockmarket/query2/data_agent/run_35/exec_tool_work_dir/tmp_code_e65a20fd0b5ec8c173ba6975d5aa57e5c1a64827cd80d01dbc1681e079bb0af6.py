code = """import json

# Get the list of NYSE Arca ETFs from the query result
def get_nyse_arca_etfs():
    # Read the query result which is stored as a file path
    # Based on the preview, it's a JSON array of objects with Symbol field
    # Let's access it properly
    etf_data = locals()['var_functions.query_db:10']
    
    # Extract symbols
    symbols = [item['Symbol'] for item in etf_data]
    return symbols

nyse_arca_etfs = get_nyse_arca_etfs()
print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs),
    'sample_symbols': nyse_arca_etfs[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:8': {'count': 38, 'sample': 'file_stora', 'first_record': 'f'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:11': 'file_storage/functions.list_db:11.json'}

exec(code, env_args)
