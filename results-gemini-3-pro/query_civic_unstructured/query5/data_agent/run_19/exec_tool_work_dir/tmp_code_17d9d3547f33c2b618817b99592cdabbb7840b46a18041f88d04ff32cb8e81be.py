code = """import sqlite3
import pandas as pd
import json
import re

# Load Funding data
con = sqlite3.connect('funding_database.db')
funding_data = pd.read_sql_query("SELECT * FROM Funding", con)
funding_data['Amount'] = pd.to_numeric(funding_data['Amount'])

# Load Civic Docs
with open(locals()['var_function-call-1716930988388569207'], 'r') as f:
    civic_docs = json.load(f)

# Identify Disaster Projects
def is_disaster_project(name):
    keywords = ['FEMA', 'CalOES', 'CalJPIA']
    return any(k in name for k in keywords)

disaster_funding = funding_data[funding_data['Project_Name'].apply(is_disaster_project)].copy()

def get_base_name(name):
    # Remove suffixes like (FEMA Project)
    return re.sub(r'\s*\(.*?(FEMA|CalOES|CalJPIA).*?\)\s*$', '', name).strip()

disaster_funding['Base_Name'] = disaster_funding['Project_Name'].apply(get_base_name)

# Parse Civic Docs
project_start_years = {}

# Build normalized map of project names
known_projects = set(funding_data['Project_Name'].unique())
known_base_names = set(disaster_funding['Base_Name'].unique())
all_names = known_projects.union(known_base_names)
normalized_names = {n.lower().strip(): n for n in all_names}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        norm_line = line_clean.lower()
        
        # Check if line is a project name
        if norm_line in normalized_names:
            current_project = normalized_names[norm_line]
            continue
            
        if current_project:
            # Check for start indicators in 2022
            # Look for "Begin Construction ... 2022" or "Construction ... completed ... 2022"
            if '2022' in line_clean:
                # Check for keywords
                if re.search(r'(?i)(begin|start|advertise).*?construction', line_clean) or \
                   re.search(r'(?i)construction.*?completed', line_clean) or \
                   re.search(r'(?i)advertise', line_clean):
                    
                    # Found a relevant 2022 date
                    project_start_years[current_project] = 2022

total_funding = 0
funded_projects = []

for index, row in disaster_funding.iterrows():
    p_name = row['Project_Name']
    b_name = row['Base_Name']
    amount = row['Amount']
    
    started = False
    if p_name in project_start_years and project_start_years[p_name] == 2022:
        started = True
    elif b_name in project_start_years and project_start_years[b_name] == 2022:
        started = True
        
    if started:
        total_funding += amount
        funded_projects.append({'name': p_name, 'amount': amount})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'funded_projects': funded_projects, 'debug_starts': list(project_start_years.keys())}))"""

env_args = {'var_function-call-3449562557564616894': 'file_storage/function-call-3449562557564616894.json', 'var_function-call-3449562557564617795': 'file_storage/function-call-3449562557564617795.json', 'var_function-call-1716930988388569207': 'file_storage/function-call-1716930988388569207.json'}

exec(code, env_args)
