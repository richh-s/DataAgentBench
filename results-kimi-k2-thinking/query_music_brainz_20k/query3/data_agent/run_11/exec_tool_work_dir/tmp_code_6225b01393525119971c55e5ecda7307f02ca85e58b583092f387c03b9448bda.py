code = """import json

# Load sales data
with open(var_functions.query_db:0, 'r') as f:
    sales_data = json.load(f)

# Load tracks data
with open(var_functions.query_db:2, 'r') as f:
    tracks_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'sales_count': len(sales_data),
    'tracks_count': len(tracks_data),
    'first_few_sales': sales_data[:3],
    'first_few_tracks': tracks_data[:3]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
