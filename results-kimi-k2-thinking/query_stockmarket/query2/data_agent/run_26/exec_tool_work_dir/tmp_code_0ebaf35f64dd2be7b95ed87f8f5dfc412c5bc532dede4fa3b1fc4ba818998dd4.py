code = """# Access the NYSE Arca ETFs from the storage
nyse_arca_etfs = var_functions.query_db_2

print("__RESULT__:")
print(json.dumps({
    "count": len(nyse_arca_etfs),
    "sample_symbols": [etf['Symbol'] for etf in nyse_arca_etfs[:10]]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
