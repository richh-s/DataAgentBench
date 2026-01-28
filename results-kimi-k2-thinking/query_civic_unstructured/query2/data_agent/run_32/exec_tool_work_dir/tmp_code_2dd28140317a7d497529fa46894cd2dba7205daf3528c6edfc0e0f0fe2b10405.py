code = """import json
import pandas as pd

# Load data
f_path = locals()['var_functions.query_db:4']
c_path = locals()['var_functions.query_db:5']

with open(f_path, 'r') as f:
    funding_raw = json.load(f)
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Process funding data
funding_df = pd.DataFrame(funding_raw)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for completion statements with 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look backwards for project name (up to 5 lines back)
            for j in range(i-1, max(-1, i-6), -1):
                prev_line = lines[j].strip()
                # Filter out metadata and formatting
                if (prev_line and len(prev_line) > 10 and 
                    not prev_line.startswith('(') and not prev_line.startswith('•')):
                    prev_lower = prev_line.lower()
                    # Skip header/metadata lines
                    skip_terms = ['project schedule', 'project description', 'updates:', 'to:', 'from:', 'subject:', 'prepared by:', 'approved by:']
                    if not any(term in prev_lower for term in skip_terms):
                        # Check if it's park-related
                        if any(keyword in prev_lower for keyword in ['park', 'playground', 'bluff', 'bluffs']):
                            park_projects_2022.add(prev_line)
                            break
        
        # Also look for specific patterns
        if 'construction was completed' in line.lower() and '2022' in line:
            for j in range(i-1, max(-1, i-6), -1):
                prev_line = lines[j].strip()
                if (prev_line and len(prev_line) > 10 and 
                    not prev_line.startswith('(')):
                    prev_lower = prev_line.lower()
                    skip_terms = ['project schedule', 'project description', 'updates:']
                    if not any(term in prev_lower for term in skip_terms):
                        if any(keyword in prev_lower for keyword in ['park', 'playground', 'bluff', 'bluffs']):
                            park_projects_2022.add(prev_line)
                            break
        
        i += 1

# Now match these projects with funding data
park_projects_2022_list = list(park_projects_2022)
matched_projects = []
total_funding = 0

for park_project in park_projects_2022_list:
    park_proj_lower = park_project.lower()
    # Find matching funding record
    for idx, row in funding_df.iterrows():
        funding_name = row['Project_Name'].lower()
        # Check for match (funding name contains project name or vice versa)
        if (park_proj_lower in funding_name or funding_name in park_proj_lower):
            total_funding += row['Amount']
            matched_projects.append(row['Project_Name'])

result = {
    'total_funding_parks_2022': int(total_funding),
    'matched_projects': list(set(matched_projects)),
    'unique_park_projects_found': len(park_projects_2022_list)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_documents': 5, 'park_projects_found': 21, 'total_park_funding': 1123000, 'completed_2022_projects_raw': 2}}

exec(code, env_args)
