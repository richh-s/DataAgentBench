code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

funding = load_json_maybe(var_call_9VTcyE0rwaemK7cQ94kOlwa6)
docs = load_json_maybe(var_call_qSNM8svbdwVUOUeF2YIBUzBK)

funding_names = set(r['Project_Name'] for r in funding if r.get('Project_Name'))

hits = []
for d in docs:
    txt = d.get('text','') or ''
    if 'Disaster Recovery Projects' in txt:
        # find nearby project names that are in funding table
        for name in funding_names:
            if name in txt:
                hits.append((d.get('filename'), name))

# summarize top 30 hits
from collections import Counter
c = Counter([name for _,name in hits])
common = c.most_common(30)

print('__RESULT__:')
print(json.dumps({'docs_with_disaster_section': len([d for d in docs if 'Disaster Recovery Projects' in (d.get('text','') or '')]),
                  'unique_funding_projects_found_in_disaster_docs': len(c),
                  'top_projects': common}))"""

env_args = {'var_call_9VTcyE0rwaemK7cQ94kOlwa6': 'file_storage/call_9VTcyE0rwaemK7cQ94kOlwa6.json', 'var_call_qSNM8svbdwVUOUeF2YIBUzBK': 'file_storage/call_qSNM8svbdwVUOUeF2YIBUzBK.json', 'var_call_VEb87KrIX5pu8BEnQ3XJsuii': {'total_funding_usd': 0, 'matched_disaster_projects_started_2022_count': 0, 'matched_disaster_projects_started_2022': []}}

exec(code, env_args)
