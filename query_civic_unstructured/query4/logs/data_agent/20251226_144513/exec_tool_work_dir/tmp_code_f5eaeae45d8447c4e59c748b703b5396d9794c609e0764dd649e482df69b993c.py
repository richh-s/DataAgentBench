code = """import pandas as pd
import json
with open(var_call_usJ0nbbAK2N7EiCmfIIXqONs, 'r') as f:
    civic_docs_records = json.load(f)
with open(var_call_o4kb2aLG9S4b1PdKnbxaMxz7, 'r') as f:
    funding_records = json.load(f)

# Extract project names scheduled to start in Spring 2022
project_names = set()
for doc in civic_docs_records:
    raw_text = doc['text']
    lines = raw_text.replace('\\n','\n').split('\n')
    current_project = None
    for line in lines:
        l = line.strip()
        if l.endswith('Project') and not l.lower().startswith('agenda item'):
            current_project = l.replace('Project', '').strip()
        elif l.startswith('Project Name:'):
            current_project = l.replace('Project Name:', '').strip()
        if ('Spring 2022' in l or 'spring 2022' in l) and ('Begin Construction' in l or 'Complete Design' in l or 'Advertise' in l or 'Begin Design' in l or 'Estimated Schedule' in l):
            if current_project:
                project_names.add(current_project)
project_names = [p for p in project_names if p]
funding_df = pd.DataFrame(funding_records)
num_projects = 0
total_funding = 0
matched_names = []
for p in project_names:
    matches = funding_df[funding_df['Project_Name'].str.lower().str.contains(p.lower(), regex=False)]
    if not matches.empty:
        num_projects += 1
        total_funding += int(matches['Total_Amount'].astype(int).sum())
        matched_names.append(str(p))
result = {'num_projects': int(num_projects), 'total_funding': int(total_funding), 'projects': matched_names}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_usJ0nbbAK2N7EiCmfIIXqONs': 'file_storage/call_usJ0nbbAK2N7EiCmfIIXqONs.json', 'var_call_o4kb2aLG9S4b1PdKnbxaMxz7': 'file_storage/call_o4kb2aLG9S4b1PdKnbxaMxz7.json'}

exec(code, env_args)
