code = """import json, re
# var_call_bvwscKjgXSiVzmcGDY8sDDH7 is the path to the JSON file containing the query result
path = var_call_bvwscKjgXSiVzmcGDY8sDDH7
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
pubs = set()
regex = re.compile(r"\b[A-Z]{2}-\d{4,}[A-Z0-9\-/]*\b")
for r in records:
    info = r.get('Patents_info','') or ''
    found = regex.findall(info)
    for m in found:
        pubs.add(m)
# Also check for patterns like 'publication number US-11421276-B2' with no country hyphen? Already covered.
result = {'uc_pub_numbers': sorted(pubs)}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vMO4SSFPl5xkRPbQmRvesVNp': ['publicationinfo'], 'var_call_XjK1ao19p1kMAkNjSWtWLtsL': ['cpc_definition'], 'var_call_bvwscKjgXSiVzmcGDY8sDDH7': 'file_storage/call_bvwscKjgXSiVzmcGDY8sDDH7.json'}

exec(code, env_args)
