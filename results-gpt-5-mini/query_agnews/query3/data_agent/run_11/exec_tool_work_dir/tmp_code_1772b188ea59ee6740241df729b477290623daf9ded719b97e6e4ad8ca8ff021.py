code = """import json
# var_call_mMPfuHOhSWZTJsArBYyeF59A is a path to the full JSON result file
path = var_call_mMPfuHOhSWZTJsArBYyeF59A
with open(path, 'r') as f:
    data = json.load(f)
# extract unique article_ids as ints
article_ids = sorted({int(rec['article_id']) for rec in data})
# Also keep mapping article_id -> publication_date
id_to_date = {int(rec['article_id']): rec['publication_date'] for rec in data}
output = {'article_ids': article_ids, 'id_to_date': id_to_date}
import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_mMPfuHOhSWZTJsArBYyeF59A': 'file_storage/call_mMPfuHOhSWZTJsArBYyeF59A.json'}

exec(code, env_args)
