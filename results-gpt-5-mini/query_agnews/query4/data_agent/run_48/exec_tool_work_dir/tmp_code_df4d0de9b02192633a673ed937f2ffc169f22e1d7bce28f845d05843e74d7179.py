code = """import json

# var_call_R20vNc28puBoUd6uKETzGfrO is provided in storage and contains the file path to the metadata results
path = var_call_R20vNc28puBoUd6uKETzGfrO
with open(path, 'r') as f:
    data = json.load(f)

# extract article_ids and mapping to region
article_ids = []
regions = {}
for rec in data:
    aid = int(rec['article_id'])
    article_ids.append(aid)
    regions[str(aid)] = rec['region']

# make unique article_ids
article_ids = sorted(list(set(article_ids)))

out = {'article_ids': article_ids, 'regions': regions}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_R20vNc28puBoUd6uKETzGfrO': 'file_storage/call_R20vNc28puBoUd6uKETzGfrO.json'}

exec(code, env_args)
