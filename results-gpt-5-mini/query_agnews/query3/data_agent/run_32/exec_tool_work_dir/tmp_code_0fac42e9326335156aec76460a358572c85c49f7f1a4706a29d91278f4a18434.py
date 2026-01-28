code = """import json
# var_call_KdEPq9ih9xbeyXXRjzKp75qz is provided in storage and contains the file path to the query result
path = var_call_KdEPq9ih9xbeyXXRjzKp75qz
with open(path, 'r') as f:
    records = json.load(f)
# extract unique article_ids as integers
ids = sorted({int(r['article_id']) for r in records})
import json
result = json.dumps(ids)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_7JiWDAT31e3Wk6vFOsyX4w2C': ['articles'], 'var_call_lScxeEEpq8xQx4Mbf73gwpIo': ['authors', 'article_metadata'], 'var_call_KdEPq9ih9xbeyXXRjzKp75qz': 'file_storage/call_KdEPq9ih9xbeyXXRjzKp75qz.json'}

exec(code, env_args)
