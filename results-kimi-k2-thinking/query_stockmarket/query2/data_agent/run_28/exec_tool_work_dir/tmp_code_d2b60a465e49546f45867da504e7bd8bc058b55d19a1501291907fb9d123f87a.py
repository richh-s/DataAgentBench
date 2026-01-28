code = """import json
import os

# Read the stored JSON files
stockinfo_path = 'var_functions.query_db:2'
stocktables_path = 'var_functions.list_db:5'

# Read the files
with open(stockinfo_path, 'r') as f:
    nyse_arca_etfs_raw = f.read()
    nyse_arca_etfs = json.loads(nyse_arca_etfs_raw)

with open(stocktables_path, 'r') as f:
    stocktrade_tables_raw = f.read()
    stocktrade_tables = json.loads(stocktrade_tables_raw)

# Extract symbols
nyse_arca_symbols = set([item['Symbol'] for item in nyse_arca_etfs])
stocktrade_symbols = set(stocktrade_tables)

# Find intersection
common_symbols = sorted(list(nyse_arca_symbols.intersection(stocktrade_symbols)))

# Create batch queries
batch_size = 25
batches = []
for i in range(0, len(common_symbols), batch_size):
    batch = common_symbols[i:i+batch_size]
    batches.append(batch)

# Save common symbols list for later use
with open('/tmp/common_symbols.json', 'w') as f:
    json.dump(common_symbols, f)

print('__RESULT__:')
print(json.dumps({
    'total_common_symbols': len(common_symbols),
    'batches_count': len(batches),
    'sample_symbols': common_symbols[:20],
    'batches': batches[:3]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5']}

exec(code, env_args)
