code = """import json
import pandas as pd
import re

# Load data
funding_data = json.load(open(locals()['var_function-call-10596372274131677177']))
funding_df = pd.DataFrame(funding_data)

docs = json.load(open(locals()['var_function-call-10596372274131674166']))

projects_found = []

for doc in docs:
    text = doc['text']
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if not line.startswith('(cid:190)') and 'Updates:' not in line:
            if i + 1 < len(lines) and lines[i+1].startswith('(cid:190)'):
                project_name = line
                project_text = ""
                i += 1
                while i < len(lines):
                    if not lines[i].startswith('(cid:190)') and \
                       (i + 1 < len(lines) and lines[i+1].startswith('(cid:190)')):
                        break
                    project_text += lines[i] + " "
                    i += 1
                
                projects_found.append({
                    'Project_Name': project_name,
                    'text': project_text
                })
                continue
        i += 1

completed_projects = []

for p in projects_found:
    name = p['Project_Name']
    text = p['text']
    
    # Check for Completed in 2022
    is_completed_2022 = False
    
    # Regex variations
    # 1. "Construction was completed[,] [in] [Month] 2022"
    if re.search(r'completed,?\s+(?:in\s+)?([A-Za-z]+)\s+2022', text, re.IGNORECASE):
        is_completed_2022 = True
            
    # 2. "Complete Construction: [Month] 2022"
    if not is_completed_2022:
        if re.search(r'Complete Construction:\s+([A-Za-z]+)\s+2022', text, re.IGNORECASE):
            is_completed_2022 = True
            
    # 3. "Construction completed [Month] 2022"
    if not is_completed_2022:
        if re.search(r'Construction completed\s+([A-Za-z]+)\s+2022', text, re.IGNORECASE):
            is_completed_2022 = True

    if is_completed_2022:
        completed_projects.append({'name': name, 'text': text[:200]}) # Preview text

print("__RESULT__:")
print(json.dumps(completed_projects))"""

env_args = {'var_function-call-15461874300401161107': ['civic_docs'], 'var_function-call-15461874300401161542': ['Funding'], 'var_function-call-10596372274131677177': 'file_storage/function-call-10596372274131677177.json', 'var_function-call-10596372274131674166': 'file_storage/function-call-10596372274131674166.json', 'var_function-call-14690968047652835103': {'total_funding': 21000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}]}}

exec(code, env_args)
