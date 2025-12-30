code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-2604806260123295524'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2604806260123292981'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

def is_park_project(name, text):
    content = (name + " " + text).lower()
    if 'park' in content and 'parking' not in content:
        return True
    if 'playground' in content:
        return True
    return False

def is_completed_2022(text):
    text_lower = text.lower()
    lines = text_lower.split('\n')
    for line in lines:
        if 'completed' in line and '2022' in line:
            if 'design' in line:
                if 'construction' in line:
                    return True
            else:
                return True
    return False

projects = []

for doc in civic_docs:
    text = doc['text']
    # Regex to find project names which are lines followed by (cid:190)
    # Using specific character code might be tricky if encoding varies, but copy-paste from preview should work.
    # The preview showed "(cid:190)" text literal.
    pattern = re.compile(r'\n+([^\n]+)\n+\(cid:190\)')
    
    matches = list(pattern.finditer(text))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_index = match.end()
        
        if i < len(matches) - 1:
            end_index = matches[i+1].start()
        else:
            end_index = len(text)
            
        project_text = text[start_index:end_index]
        
        projects.append({
            'name': project_name,
            'text': project_text
        })

completed_park_projects = []
for p in projects:
    if is_park_project(p['name'], p['text']):
        if is_completed_2022(p['text']):
            completed_park_projects.append(p['name'])

completed_park_projects = list(set(completed_park_projects))
print(f"DEBUG: Found {len(completed_park_projects)} completed park projects: {completed_park_projects}")

total_funding = 0
matched_projects = []

for name in completed_park_projects:
    record = funding_df[funding_df['Project_Name'].str.strip() == name.strip()]
    if not record.empty:
        amount = record['Amount'].sum()
        total_funding += amount
        matched_projects.append(name)
    else:
        print(f"DEBUG: No funding found for {name}")

print("__RESULT__:")
print(json.dumps({"total_funding": int(total_funding), "projects": matched_projects}))"""

env_args = {'var_function-call-2604806260123295524': 'file_storage/function-call-2604806260123295524.json', 'var_function-call-2604806260123292981': 'file_storage/function-call-2604806260123292981.json'}

exec(code, env_args)
