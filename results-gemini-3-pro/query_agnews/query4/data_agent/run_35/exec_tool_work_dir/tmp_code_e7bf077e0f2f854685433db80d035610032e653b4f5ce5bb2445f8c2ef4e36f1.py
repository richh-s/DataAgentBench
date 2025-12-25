code = """import json

file_path = locals()['var_function-call-17404740365086201769']
with open(file_path, 'r') as f:
    metadata_records = json.load(f)

ids = [int(r['article_id']) for r in metadata_records]
print("__RESULT__:")
print(json.dumps({"min": min(ids), "max": max(ids)}))"""

env_args = {'var_function-call-17404740365086201769': 'file_storage/function-call-17404740365086201769.json', 'var_function-call-2022338119452358264': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}}

exec(code, env_args)
