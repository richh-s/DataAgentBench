code = """import json
# Load the metadata query result from the stored file path variable
file_path = var_call_DmVudIOV502t5IH27ghYXMnM
with open(file_path, 'r') as f:
    records = json.load(f)
# Extract article_ids as integers
article_ids = [int(r['article_id']) for r in records]
import json
print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_call_DmVudIOV502t5IH27ghYXMnM': 'file_storage/call_DmVudIOV502t5IH27ghYXMnM.json'}

exec(code, env_args)
