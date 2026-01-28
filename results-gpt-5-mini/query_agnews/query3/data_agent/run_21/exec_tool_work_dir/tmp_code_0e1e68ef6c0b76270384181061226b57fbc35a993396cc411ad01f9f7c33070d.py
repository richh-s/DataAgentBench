code = """import json
# Load the metadata query result file
path = var_call_2rQ9dGfrtFxHN8lzY23MYLjM
with open(path, 'r') as f:
    records = json.load(f)
# Extract unique article_ids as ints
ids = sorted({int(r['article_id']) for r in records})
import json
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_YqinKIOyfwVYtDOpsyk3NNHW': ['articles'], 'var_call_e07lyV9DBwFNuOU5bvSqKSUM': ['authors', 'article_metadata'], 'var_call_2rQ9dGfrtFxHN8lzY23MYLjM': 'file_storage/call_2rQ9dGfrtFxHN8lzY23MYLjM.json'}

exec(code, env_args)
