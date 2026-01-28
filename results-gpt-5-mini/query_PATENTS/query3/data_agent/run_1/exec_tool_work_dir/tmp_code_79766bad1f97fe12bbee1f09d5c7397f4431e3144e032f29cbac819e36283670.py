code = """import json, re
path = var_call_5hfOOzVekj2vU7HdE07OAzBp
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pubs = set()
pattern = re.compile(r"[A-Z]{2}-[0-9A-Z\-]{4,}")
for rec in data:
    pi = rec.get('Patents_info','')
    for m in pattern.findall(pi):
        pubs.add(m)
# Also try to find patterns like 'publication number US-...' explicitly
pattern2 = re.compile(r"publication number\s*([A-Z]{2}-[0-9A-Z\-]{4,})", re.IGNORECASE)
for rec in data:
    pi = rec.get('Patents_info','')
    for m in pattern2.findall(pi):
        pubs.add(m)
pubs_list = sorted(pubs)
print('__RESULT__:')
print(json.dumps(pubs_list))"""

env_args = {'var_call_5hfOOzVekj2vU7HdE07OAzBp': 'file_storage/call_5hfOOzVekj2vU7HdE07OAzBp.json', 'var_call_DFteqp4XsyEXBwFVfnZA0IuA': [], 'var_call_QOLBEdXL0t1VbQxpCf3TvTwd': 'file_storage/call_QOLBEdXL0t1VbQxpCf3TvTwd.json', 'var_call_ve2g86unmpIwbOrX6CUCNLSm': 'file_storage/call_ve2g86unmpIwbOrX6CUCNLSm.json'}

exec(code, env_args)
