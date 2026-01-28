code = """import json
import pandas as pd

# Read the stockinfo query result
stockinfo_file = var_functions.query_db:0
with open(stockinfo_file, 'r') as f:
    stockinfo_data = json.load(f)

# Extract symbols and create mapping
symbols = [row['Symbol'] for row in stockinfo_data]
company_names = {row['Symbol']: row['Company Description'] for row in stockinfo_data}

print('__RESULT__:')
print(json.dumps({
    'symbol_count': len(symbols),
    'first_few_symbols': symbols[:10],
    'company_names_sample': {k: company_names[k] for k in list(company_names.keys())[:3]}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
