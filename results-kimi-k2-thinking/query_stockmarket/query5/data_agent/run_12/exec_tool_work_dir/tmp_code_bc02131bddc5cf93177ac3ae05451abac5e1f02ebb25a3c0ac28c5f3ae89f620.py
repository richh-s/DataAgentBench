code = """import json
import pandas as pd

# Access the stored results directly
nasdaq_cap_symbols = locals()['var_functions.query_db:0']
available_tables = locals()['var_functions.list_db:2']

# Create a set of available symbols for quick lookup
available_symbols = set(available_tables)

# Filter to only include symbols that have data tables
valid_symbols = [{'symbol': item['Symbol'], 'description': item['Company Description']} 
                for item in nasdaq_cap_symbols 
                if item['Symbol'] in available_symbols]

print('__RESULT__:')
print(json.dumps({
    'total_nasdaq_cap_symbols': len(nasdaq_cap_symbols),
    'symbols_with_data': len(valid_symbols),
    'sample_symbols': valid_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
