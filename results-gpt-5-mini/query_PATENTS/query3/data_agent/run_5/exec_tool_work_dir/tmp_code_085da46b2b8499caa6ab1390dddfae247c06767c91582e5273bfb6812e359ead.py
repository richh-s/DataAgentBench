code = """import json, re
# var_call_TbERQfq1CXTEPXgS8smlyIUz is the key containing the UNIV CALIFORNIA rows file path
path = var_call_TbERQfq1CXTEPXgS8smlyIUz
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pubs = set()
for rec in data:
    pi = rec.get('Patents_info','')
    # look for patterns like 'pub. number XXX', 'publication number XXX', 'pub. number XXX.'
    m = re.findall(r'([A-Z]{2}-\d{4,}[-A-Z0-9]*)', pi)
    for x in m:
        pubs.add(x)
# also try to find patterns like 'pub. number (no. )?US123..' when no hyphen
m2 = re.findall(r'\b(US\d{7,}[-A-Z0-9]*)\b', ' '.join([r.get('Patents_info','') for r in data]))
for x in m2:
    pubs.add(x)
result = sorted(list(pubs))
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uprdDvuZVAABXUB9BzYSvOlA': ['publicationinfo'], 'var_call_PZlcITScnIvsTgc6qXOTEs6R': ['cpc_definition'], 'var_call_TbERQfq1CXTEPXgS8smlyIUz': 'file_storage/call_TbERQfq1CXTEPXgS8smlyIUz.json'}

exec(code, env_args)
