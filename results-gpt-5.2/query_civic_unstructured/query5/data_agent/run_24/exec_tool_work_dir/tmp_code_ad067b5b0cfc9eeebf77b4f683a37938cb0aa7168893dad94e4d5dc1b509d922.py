code = """import json

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_PMr5zq0ajEpSTgyvqBA9I0b5)
fund = load_json_maybe(var_call_YiusZ3QcF3T7rRofI85mNe2T)

fund_map = {r['Project_Name']: float(r['total_amount']) for r in fund}

# Heuristic: disaster-related projects in Funding table often include FEMA/CalOES/CalJPIA
# Determine which of those started in 2022 by checking civic docs for 'Begin Construction: ...2022' near the project name.

def started_in_2022(text, project_name):
    idx = text.find(project_name)
    if idx == -1:
        return False
    window = text[idx: idx+1500]
    return ('Begin Construction' in window or 'Begin construction' in window) and ('2022' in window)

started_projects=set()
for d in docs:
    t = d.get('text','') or ''
    for pname in fund_map.keys():
        if pname in started_projects:
            continue
        if started_in_2022(t, pname):
            # ensure it's disaster-related by keyword in name
            if any(k in pname for k in ['FEMA', 'CalOES', 'CalJPIA', 'Disaster']):
                started_projects.add(pname)

# Sum funding for those projects
total = sum(fund_map[p] for p in started_projects)

out = {'total_funding_disaster_projects_started_2022': int(total), 'projects': sorted(started_projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WTMkebJ5tBXmyNTIG44oaAgK': ['Funding'], 'var_call_JtXuQbLdcCW8xiMPGowlZXtS': ['civic_docs'], 'var_call_PMr5zq0ajEpSTgyvqBA9I0b5': 'file_storage/call_PMr5zq0ajEpSTgyvqBA9I0b5.json', 'var_call_YiusZ3QcF3T7rRofI85mNe2T': 'file_storage/call_YiusZ3QcF3T7rRofI85mNe2T.json'}

exec(code, env_args)
