code = """import json, re
path = var_call_5hfOOzVekj2vU7HdE07OAzBp
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pub_nums = set()
# Try to extract patterns like US- followed by digits and optional -A etc, also other country codes
pattern = re.compile(r"[A-Z]{2}-\d{4,}[A-Z0-9-]*")
for rec in data:
    pi = rec.get('Patents_info','')
    for m in pattern.findall(pi):
        pub_nums.add(m)
# Also check citation field for publication_number entries inside citation arrays
for rec in data:
    cit = rec.get('citation','')
    try:
        citlist = json.loads(cit)
        for c in citlist:
            pn = c.get('publication_number')
            if pn:
                pub_nums.add(pn)
    except Exception:
        # fallback find tokens
        for m in pattern.findall(cit):
            pub_nums.add(m)
pubs = sorted(pub_nums)
import json
print('__RESULT__:')
print(json.dumps(pubs))"""

env_args = {'var_call_5hfOOzVekj2vU7HdE07OAzBp': 'file_storage/call_5hfOOzVekj2vU7HdE07OAzBp.json', 'var_call_DFteqp4XsyEXBwFVfnZA0IuA': []}

exec(code, env_args)
