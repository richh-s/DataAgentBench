code = """import json, re
# var_call_5hfOOzVekj2vU7HdE07OAzBp is available as variable and is a filepath to the JSON result
path = var_call_5hfOOzVekj2vU7HdE07OAzBp
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pubs = set()
pattern = re.compile(r"\b[A-Z]{2}-\d{4,}[A-Z0-9-]*\b")
for rec in data:
    pi = rec.get('Patents_info','')
    found = pattern.findall(pi)
    for x in found:
        pubs.add(x)
# Also check if some records have publication_number in other fields? titles? but above should capture
pubs_list = sorted(pubs)
import json
print('__RESULT__:')
print(json.dumps(pubs_list))"""

env_args = {'var_call_5hfOOzVekj2vU7HdE07OAzBp': 'file_storage/call_5hfOOzVekj2vU7HdE07OAzBp.json'}

exec(code, env_args)
