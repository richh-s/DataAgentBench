code = """import json

# Read the full stockinfo data
stockinfo_path = locals()['var_functions.query_db:2']
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

# Get all NYSE non-ETF symbols
nyse_symbols = [item['Symbol'] for item in stockinfo_data]
print(f"Total NYSE non-ETF symbols: {len(nyse_symbols)}")

# Read the list of tables from stocktrade database
trade_tables_path = locals()['var_functions.list_db:6']
with open(trade_tables_path, 'r') as f:
    trade_tables_data = json.load(f)

print(f"Total tables in stocktrade database: {len(trade_tables_data)}")

# Find intersection
nyse_set = set(nyse_symbols)
trade_set = set(trade_tables_data)
common_symbols = nyse_set.intersection(trade_set)

print(f"Common symbols (NYSE non-ETF with price data): {len(common_symbols)}")
print(f"Sample common symbols: {list(common_symbols)[:10]}")

# Store the common symbols for next step
result = {
    'nyse_count': len(nyse_symbols),
    'trade_count': len(trade_tables_data),
    'common_count': len(common_symbols),
    'common_symbols': list(common_symbols)[:20]  # Just a sample for debugging
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'total_symbols': 234, 'sample_symbols': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'], ['AIZP', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
