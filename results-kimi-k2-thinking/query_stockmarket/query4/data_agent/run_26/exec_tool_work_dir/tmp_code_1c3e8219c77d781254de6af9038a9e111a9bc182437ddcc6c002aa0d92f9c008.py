code = """# First identify which NYSE stocks exist as tables in stocktrade database
# Read both the stockinfo data and the list of tables
import json

with open('file_storage/functions.query_db:18.json', 'r') as f:
    stockinfo_data = json.load(f)

with open('file_storage/functions.list_db:10.json', 'r') as f:
    all_tables = json.load(f)

# Create NYSE stock symbols set
nyse_symbols = {item['Symbol'] for item in stockinfo_data}
print("Total NYSE symbols from stockinfo:", len(nyse_symbols))

# Find intersection with available tables
available_stock_tables = nyse_symbols.intersection(all_tables)
print("Available NYSE tables in stocktrade database:", len(available_stock_tables))

# Check some sample tables to see if they have 2017 data
sample_symbols = list(available_stock_tables)[:5]
print("Sample symbols:", sample_symbols)

# Store the valid symbols
valid_nyse_symbols = list(available_stock_tables)

result = {
    'total_nyse_symbols': len(nyse_symbols),
    'available_tables': len(valid_nyse_symbols),
    'sample_symbols': sample_symbols
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
