code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

doc = load_json_maybe(var_call_hGjqlEFP5FEsURnqkLtIjuvn)[0]
text = str(doc.get('text',''))
lines=[ln.rstrip() for ln in text.splitlines()]

pat = re.compile(r"Begin\s+Construction\s*:\s*(Spring\s*2022|Spring/Summer\s*2022|Spring\s*/\s*Summer\s*2022|Spring\s*2022)\b", re.IGNORECASE)

hits=[]
for i, ln in enumerate(lines):
    if pat.search(ln):
        # find previous non-empty line as name
        j=i-1
        while j>=0 and not lines[j].strip():
            j-=1
        # walk back to find a project title separated by blank line
        # take first non-empty line above a blank line boundary within 10 lines
        name=None
        for k in range(j, max(-1,j-20), -1):
            if not lines[k].strip():
                # next non-empty above is likely title
                m=k-1
                while m>=0 and not lines[m].strip():
                    m-=1
                if m>=0:
                    name=lines[m].strip()
                break
        if name is None and j>=0:
            name=lines[j].strip()
        hits.append({'line': ln.strip(), 'name_guess': name, 'idx': i})

print('__RESULT__:')
print(json.dumps(hits))"""

env_args = {'var_call_0f7yDI4ecmLKSKpoaVFu2vZD': 'file_storage/call_0f7yDI4ecmLKSKpoaVFu2vZD.json', 'var_call_27VpEJXZf7UZvZlIuZtK2xrL': 'file_storage/call_27VpEJXZf7UZvZlIuZtK2xrL.json', 'var_call_WYLUmmwObGXwduLEEijbEoV5': {'spring_2022_project_count': 0, 'spring_2022_total_funding_matched': 0, 'matched_project_count': 0, 'missing_funding_project_count': 0, 'missing_projects_sample': []}, 'var_call_XLDXr8FDGIphVyw4C4Q3qfWR': {'line_hits': 0, 'samples': []}, 'var_call_i92AmPWPnkGbKjl9Z3o4vfog': {'docs_with_spring2022': 4, 'samples': [' Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'dian Improvement\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Constructio']}, 'var_call_zCqf1WbLjtYkipYn3bBW8Sx6': {'projects_started_spring_2022': [], 'project_count': 0, 'total_funding_matched': 0, 'matched_count': 0, 'missing_count': 0, 'missing_projects': []}, 'var_call_9OVRbthoX8UjJjqhxVPnzzfM': {'docs': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt'], 'count_docs': 4}, 'var_call_hGjqlEFP5FEsURnqkLtIjuvn': 'file_storage/call_hGjqlEFP5FEsURnqkLtIjuvn.json'}

exec(code, env_args)
