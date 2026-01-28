code = """import json

# Get the file path from the previous result
result = var_functions.query_db:2

# Check if it's a file path (string) or direct data
if isinstance(result, str) and '.json' in result:
    # It's a file path
    with open(result, 'r') as f:
        metadata_records = json.load(f)
else:
    # It's direct data
    metadata_records = result

# Output basic stats
print('__RESULT__:')
print(json.dumps({
    'total_europe_articles': len(metadata_records),
    'available_fields': list(metadata_records[0].keys()) if metadata_records else [],
    'sample_articles': metadata_records[:3]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
