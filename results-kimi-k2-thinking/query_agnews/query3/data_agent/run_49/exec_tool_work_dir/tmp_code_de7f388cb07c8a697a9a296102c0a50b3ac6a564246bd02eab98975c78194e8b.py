code = """import json

# Load the metadata results
metadata_path = var_functions.query_db:2
with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

print(f"Total Europe articles between 2010-2020: {len(metadata_records)}")

# Extract unique article IDs
article_ids = [rec['article_id'] for rec in metadata_records]
print(f"Number of unique article IDs: {len(article_ids)}")

# Show first few records
print("First 5 records:")
for rec in metadata_records[:5]:
    print(rec)

print('__RESULT__:')
print(json.dumps(str(len(article_ids))))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
