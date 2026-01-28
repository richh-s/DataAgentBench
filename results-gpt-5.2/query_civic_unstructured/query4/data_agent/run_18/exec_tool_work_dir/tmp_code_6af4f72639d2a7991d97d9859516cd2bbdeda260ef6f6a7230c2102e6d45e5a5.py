code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

doc = load_json_maybe(var_call_hGjqlEFP5FEsURnqkLtIjuvn)[0]
text=str(doc.get('text',''))
lines=[ln.strip() for ln in text.splitlines()]

hits=[]
for i, ln in enumerate(lines):
    if 'Begin Construction' in ln:
        hits.append({'i':i,'ln':ln,'ctx':lines[max(0,i-3):i+3]})

print('__RESULT__:')
print(json.dumps(hits[:20]))"""

env_args = {'var_call_0f7yDI4ecmLKSKpoaVFu2vZD': 'file_storage/call_0f7yDI4ecmLKSKpoaVFu2vZD.json', 'var_call_27VpEJXZf7UZvZlIuZtK2xrL': 'file_storage/call_27VpEJXZf7UZvZlIuZtK2xrL.json', 'var_call_WYLUmmwObGXwduLEEijbEoV5': {'spring_2022_project_count': 0, 'spring_2022_total_funding_matched': 0, 'matched_project_count': 0, 'missing_funding_project_count': 0, 'missing_projects_sample': []}, 'var_call_XLDXr8FDGIphVyw4C4Q3qfWR': {'line_hits': 0, 'samples': []}, 'var_call_i92AmPWPnkGbKjl9Z3o4vfog': {'docs_with_spring2022': 4, 'samples': [' Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'dian Improvement\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Constructio']}, 'var_call_zCqf1WbLjtYkipYn3bBW8Sx6': {'projects_started_spring_2022': [], 'project_count': 0, 'total_funding_matched': 0, 'matched_count': 0, 'missing_count': 0, 'missing_projects': []}, 'var_call_9OVRbthoX8UjJjqhxVPnzzfM': {'docs': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt'], 'count_docs': 4}, 'var_call_hGjqlEFP5FEsURnqkLtIjuvn': 'file_storage/call_hGjqlEFP5FEsURnqkLtIjuvn.json', 'var_call_O8HZvF7xT1jHmIddur0w55jj': []}

exec(code, env_args)
