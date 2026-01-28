code = """import json, re
path = var_call_bvwscKjgXSiVzmcGDY8sDDH7
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
text = json.dumps(records)
# find patterns like US-2022074631-A1, TW-201925402-A, US-11421276-B2
pat = re.compile(r"[A-Z]{2}-\d{4,}[-A-Z0-9]*")
found = sorted(set(pat.findall(text)))
# also find patterns like US-11466906-B2 already matched.
result = {'uc_pub_numbers': found, 'count_records': len(records)}
print('__RESULT__:')
import json
print(json.dumps(result))"""

env_args = {'var_call_vMO4SSFPl5xkRPbQmRvesVNp': ['publicationinfo'], 'var_call_XjK1ao19p1kMAkNjSWtWLtsL': ['cpc_definition'], 'var_call_bvwscKjgXSiVzmcGDY8sDDH7': 'file_storage/call_bvwscKjgXSiVzmcGDY8sDDH7.json', 'var_call_1wUCiArK5fhy4meeI5gcsEYD': {'uc_pub_numbers': []}}

exec(code, env_args)
