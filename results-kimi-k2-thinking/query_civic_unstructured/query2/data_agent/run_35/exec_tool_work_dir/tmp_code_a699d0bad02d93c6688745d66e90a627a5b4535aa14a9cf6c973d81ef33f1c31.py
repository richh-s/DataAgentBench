code = """import json
import pandas as pd

# Load the funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents (filtered for park, completed, 2022)
civic_file = locals()['var_functions.query_db:34']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for park-related project names
        if 'park' in line.lower() and len(line) > 10 and len(line) < 150:
            # Skip obvious headers/section titles
            if any(skip in line for skip in ['Project Schedule', 'Updates:', 'Project Description', 'Agenda', 'Page', 'RECOMMENDED ACTION', 'DISCUSSION', 'Subject:', 'To:', 'Prepared by:', 'Approved by:']):
                continue
            
            # Look ahead for completion notice with 2022
            for j in range(i, min(i+12, len(lines))):
                next_line = lines[j]
                if 'Construction was completed' in next_line and '2022' in next_line:
                    if line not in park_projects_2022:
                        park_projects_2022.append(line)
                    break

# Deduplicate list
unique_projects = []
for p in park_projects_2022:
    if p not in unique_projects:
        unique_projects.append(p)

# Create a DataFrame for funding data
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Match park projects with funding amounts
total_funding = 0
matches = []

for project_name in unique_projects:
    # Clean project name for matching (remove common suffixes)
    clean_name = project_name.split(' (')[0].strip()
    
    # Look for exact or partial matches in funding data
    matching_funds = df_funding[df_funding['Project_Name'].str.contains(clean_name, case=False, na=False)]
    
    if not matching_funds.empty:
        amount = matching_funds['Amount'].sum()
        total_funding += amount
        matches.append({
            'project': project_name,
            'matching_funding_name': matching_funds['Project_Name'].tolist(),
            'amount': amount
        })

result = {
    'park_projects_2022': unique_projects,
    'project_count': len(unique_projects),
    'funding_matches': matches,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
