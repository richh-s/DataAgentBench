code = """import json
# Load metadata results from the previous query stored in var_call_l6lMtIxOSgeKCkVENT08qPDd
path = var_call_l6lMtIxOSgeKCkVENT08qPDd
with open(path, 'r') as f:
    records = json.load(f)
# Extract unique article_ids and mapping to year
article_ids = sorted({int(r['article_id']) for r in records})
id_to_year = {str(int(r['article_id'])): int(r['publication_date'][:4]) for r in records}
result = {'article_ids': article_ids, 'id_to_year': id_to_year}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_l6lMtIxOSgeKCkVENT08qPDd': 'file_storage/call_l6lMtIxOSgeKCkVENT08qPDd.json'}

exec(code, env_args)
