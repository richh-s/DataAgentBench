code = """import json

# Read metadata
file_path = locals()['var_function-call-17404740365086201769']
with open(file_path, 'r') as f:
    metadata_records = json.load(f)

ids = [int(r['article_id']) for r in metadata_records]
chunk_size = 500
batches = [ids[i:i + chunk_size] for i in range(0, len(ids), chunk_size)]

# Save batches
with open('batches.json', 'w') as f:
    json.dump(batches, f)

# Initialize result file
with open('articles_content.json', 'w') as f:
    json.dump([], f)

# Prepare query for batch 0
batch_0_ids = batches[0]
query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": batch_0_ids}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-17404740365086201769': 'file_storage/function-call-17404740365086201769.json', 'var_function-call-2022338119452358264': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_function-call-11041514137920419943': {'min': 13, 'max': 127570}, 'var_function-call-4989923397492992652': 'file_storage/function-call-4989923397492992652.json', 'var_function-call-14496419119669102525': 'file_storage/function-call-14496419119669102525.json'}

exec(code, env_args)
