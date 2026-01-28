code = """import json

# Load the data
stockinfo_path = locals()['var_functions.query_db:0']
tables_path = locals()['var_functions.query_db:4']

with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

with open(tables_path, 'r') as f:
    tables_data = json.load(f)

# Create sets for easy comparison
stockinfo_symbols = {item['Symbol'] for item in stockinfo_data}
trade_tables = {item['table_name'] for item in tables_data}

# Find intersection
common_symbols = stockinfo_symbols.intersection(trade_tables)

print('__RESULT__:')
print(json.dumps({
    'nyse_non_etf_count': len(stockinfo_symbols),
    'trade_tables_count': len(trade_tables),
    'common_symbols_count': len(common_symbols),
    'sample_common': list(common_symbols)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'stockinfo_count': 234, 'tables_count': 2753, 'sample_stockinfo': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}], 'sample_tables': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}]}}

exec(code, env_args)
