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
    # Split lines using escaped newline
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this line is potentially a project title
        if not line.startswith('(cid:190)') and 'Updates:' not in line:
            # Look ahead for the bullet marker in the next line
            if i + 1 < len(lines) and lines[i+1].startswith('(cid:190)'):
                project_name = line
                project_text = ""
                i += 1
                while i < len(lines):
                    # Check for start of NEW project
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

matched_projects = []

for p in projects_found:
    name = p['Project_Name']
    text = p['text']
    
    # Check for Park related
    is_park = False
    if re.search(r'park', name, re.IGNORECASE) or \
       re.search(r'playground', name, re.IGNORECASE) or \
       re.search(r'recreation', name, re.IGNORECASE):
        is_park = True
    
    # Check for Completed in 2022
    completed_2022 = False
    
    # "Construction was completed[,] November 2022"
    # "Complete Construction: November 2022"
    
    m1 = re.search(r'completed,?\s+([A-Za-z]+)\s+(2022)', text, re.IGNORECASE)
    if m1:
        completed_2022 = True
            
    if not completed_2022:
        m2 = re.search(r'Complete Construction:\s+([A-Za-z]+)\s+(2022)', text, re.IGNORECASE)
        if m2:
            completed_2022 = True

    if is_park and completed_2022:
        matched_projects.append(name)

total_funding = 0
funded_projects_details = []

for pname in matched_projects:
    clean_pname = pname.strip()
    match = funding_df[funding_df['Project_Name'].str.strip() == clean_pname]
    
    if match.empty:
        match = funding_df[funding_df['Project_Name'].str.strip().str.lower() == clean_pname.lower()]
    
    if not match.empty:
        amount = pd.to_numeric(match['Amount']).sum()
        total_funding += amount
        funded_projects_details.append({'name': clean_pname, 'amount': amount})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'projects': funded_projects_details}))"""

env_args = {'var_function-call-15461874300401161107': ['civic_docs'], 'var_function-call-15461874300401161542': ['Funding'], 'var_function-call-10596372274131677177': 'file_storage/function-call-10596372274131677177.json', 'var_function-call-10596372274131674166': 'file_storage/function-call-10596372274131674166.json'}

exec(code, env_args)
