code = """import json
import pandas as pd

def load_tool_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

docs = load_tool_result(var_call_Qnz8631zTgIET1P1nCy1dME9)
fund = load_tool_result(var_call_kkzM7d1OdECbngMczMndwQkA)

completed_2022_park_projects = set()

keywords = ['park', 'playground', 'bluffs park', 'legacy park', 'skate park', 'trancas canyon park']

for d in docs:
    text = d.get('text','')
    low = text.lower()
    if 'completed' not in low or '2022' not in low:
        continue
    # Check each funded project name; if appears near completion language and is park-related, include
    for rec in fund:
        name = rec['Project_Name']
        nlow = name.lower()
        if not any(k in nlow for k in ['park','playground','bluffs','legacy','skate','trancas']):
            continue
        if nlow in low:
            # require also completion in 2022 somewhere in doc; assume ok
            completed_2022_park_projects.add(name)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = fund_df['total_amount'].astype(float)
sel = fund_df[fund_df['Project_Name'].isin(sorted(completed_2022_park_projects))]

out = {
    'projects': sel.sort_values('Project_Name').to_dict(orient='records'),
    'total_funding': float(sel['total_amount'].sum()),
    'project_count': int(sel.shape[0])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FHupFkqHl4OgYoZHCOffbKXN': ['Funding'], 'var_call_eyeG8LC6azKhVNC26QjWhYTj': ['civic_docs'], 'var_call_Qnz8631zTgIET1P1nCy1dME9': 'file_storage/call_Qnz8631zTgIET1P1nCy1dME9.json', 'var_call_kkzM7d1OdECbngMczMndwQkA': 'file_storage/call_kkzM7d1OdECbngMczMndwQkA.json'}

exec(code, env_args)
