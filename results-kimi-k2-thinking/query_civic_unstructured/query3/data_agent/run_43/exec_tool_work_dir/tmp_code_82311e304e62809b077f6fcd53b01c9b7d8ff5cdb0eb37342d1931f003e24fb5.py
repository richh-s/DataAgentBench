code = """import json
import re
import pandas as pd

# Load MongoDB documents
mongo_file = locals()['var_functions.query_db:0']
with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

# Load funding data
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Convert funding to DataFrame
df_funding = pd.DataFrame(funding_records)

# Extract project information
all_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project patterns
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Detect project names (typically uppercase or title case)
        if re.match(r'^[A-Z][a-zA-Z\s&\-]+(?:\([^)]*\))?$', line) and len(line) > 10:
            project_name = line
            
            # Check if this is related to emergency or FEMA
            if 'emergency' in project_name.lower() or 'fema' in project_name.lower():
                project = {
                    'Project_Name': project_name,
                    'topic': 'emergency' if 'emergency' in project_name.lower() else 'FEMA', 
                    'type': 'disaster'
                }
                
                # Look for status in surrounding text
                surrounding_text = ' '.join(lines[max(0,i-3):min(len(lines),i+4)])
                if 'completed' in surrounding_text.lower():
                    project['status'] = 'completed'
                elif 'design' in surrounding_text.lower():
                    project['status'] = 'design'
                else:
                    project['status'] = 'unknown'
                
                # Look for dates
                date_match = re.search(r'(20\d{2}-\w+)', text)
                project['st'] = date_match.group(1) if date_match else ''
                project['et'] = ''
                
                all_projects.append(project)

# Filter for unique projects
unique_projects = []
seen_names = set()
for proj in all_projects:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

# Merge with funding data
results = []
for proj in unique_projects:
    # Find funding records for this project
    matching_funding = df_funding[df_funding['Project_Name'] == proj['Project_Name']]
    
    if not matching_funding.empty:
        for _, fund in matching_funding.iterrows():
            result = {
                'Project_Name': proj['Project_Name'],
                'Funding_Source': fund.get('Funding_Source', 'Not specified'),
                'Amount': float(fund.get('Amount', 0)),
                'Status': proj['status'],
                'Type': proj['type'],
                'Topic': proj['topic']
            }
            results.append(result)
    else:
        # Check for partial matches (project name without suffixes)
        base_name = re.sub(r'\s*\([^)]*\)\s*$', '', proj['Project_Name'])
        matching_funding = df_funding[df_funding['Project_Name'].str.contains(base_name, na=False)]
        
        if not matching_funding.empty:
            for _, fund in matching_funding.iterrows():
                result = {
                    'Project_Name': proj['Project_Name'],
                    'Funding_Source': fund.get('Funding_Source', 'Not specified'),
                    'Amount': float(fund.get('Amount', 0)),
                    'Status': proj['status'],
                    'Type': proj['type'],
                    'Topic': proj['topic']
                }
                results.append(result)

# Return results in JSON format
final_result = json.dumps(results, ensure_ascii=False, indent=2)
print('__RESULT__:')
print(final_result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
