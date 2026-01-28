code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-1023604252681241279'], 'r') as f:
    funding_list = json.load(f)

with open(locals()['var_function-call-1023604252681243206'], 'r') as f:
    civic_docs = json.load(f)

# Create a map of Project Name to Funding Info
funding_df = pd.DataFrame(funding_list)
project_funding = {row['Project_Name']: row['Amount'] for _, row in funding_df.iterrows()}
known_projects = set(project_funding.keys())

# Parse logic
project_details = {} 

current_project = None
current_type_context = 'capital' 

# Regex for start date
# Escaping backslashes for safe execution
date_pattern = re.compile(r'(?:Begin Construction|Start Date|Construction Start|Advertise).*?(\\d{4})', re.IGNORECASE)

for doc in civic_docs:
    lines = doc['text'].split('\\n') # Escaping \n
    # Fallback if split fails or returns 1 item, try regular \n if the environment handles it.
    if len(lines) <= 1 and '\\n' not in doc['text']:
        lines = doc['text'].split('\n')

    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue

        if "Disaster Recovery Projects" in clean_line:
            current_type_context = 'disaster'
        elif "Capital Improvement Projects" in clean_line:
            current_type_context = 'capital'
        
        if clean_line in known_projects:
            current_project = clean_line
            p_type = current_type_context
            lower_name = clean_line.lower()
            if any(x in lower_name for x in ['fema', 'caloes', 'caljpia', 'woolsey']):
                p_type = 'disaster'
            
            if current_project not in project_details:
                project_details[current_project] = {'type': p_type, 'st': None}
            else:
                if p_type == 'disaster':
                    project_details[current_project]['type'] = 'disaster'
            continue
            
        if current_project:
            match = date_pattern.search(clean_line)
            if match:
                year = match.group(1)
                existing_st = project_details[current_project]['st']
                
                if "begin construction" in clean_line.lower():
                     project_details[current_project]['st'] = year
                elif existing_st is None:
                     project_details[current_project]['st'] = year

total_funding = 0
matches = []

for p_name, details in project_details.items():
    p_type = details['type']
    st = details['st']
    
    if p_type == 'disaster' and st == '2022':
        amount = int(project_funding.get(p_name, 0))
        total_funding += amount
        matches.append({'name': p_name, 'amount': amount, 'st': st})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'matches': matches}))"""

env_args = {'var_function-call-1023604252681241279': 'file_storage/function-call-1023604252681241279.json', 'var_function-call-1023604252681243206': 'file_storage/function-call-1023604252681243206.json'}

exec(code, env_args)
