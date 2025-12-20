code = """import json

# Load the result from the previous step
with open(locals()['var_function-call-16631268004823778356'], 'r') as f:
    metadata_records = json.load(f)

# Count records
count = len(metadata_records)
print(f"Total records: {count}")

# Extract IDs (convert to int as per schema)
ids = [int(r['article_id']) for r in metadata_records]

# Preview IDs
print(f"IDs preview: {ids[:10]}")

# Prepare the mapping for later
id_year_map = {int(r['article_id']): r['year'] for r in metadata_records}

print("__RESULT__:")
print(json.dumps({"count": count, "ids": ids, "id_year_map": id_year_map}))"""

env_args = {'var_function-call-16631268004823778356': 'file_storage/function-call-16631268004823778356.json'}

exec(code, env_args)
