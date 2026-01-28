code = """import json
import pandas as pd

# Load funding data
funding_path = locals()['var_functions.query_db:4']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
civic_path = locals()['var_functions.query_db:5']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Process funding data
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Find park-related projects in funding data
park_keywords = ['park', 'playground', 'bluff']
park_mask = df_funding['Project_Name'].str.contains('|'.join(park_keywords), case=False, na=False)
park_projects = df_funding[park_mask]

# Extract project information from civic documents
def extract_project_info(text):
    projects = []
    lines = text.split('\\n')
    
    for line in lines:
        if 'Project Name:' in line or any(keyword in line.lower() for keyword in ['project', 'updates:', 'schedule:']):
            continue
    
    return projects

all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Simple extraction - look for project names and status
    projects = extract_project_info(text)
    all_projects.extend(projects)

# For now, let's focus on parsing the text for completed projects in 2022
completed_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for completion mentions in 2022
    if '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        # Extract project names - this is a simplified approach
        lines = text.split('\\n')
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if line_clean and not line_clean.startswith('(') and len(line_clean) > 10:
                if any(indicator in line_clean.lower() for indicator in ['construction was completed', 'notice of completion', 'completed']):
                    if '2022' in line_clean:
                        # Look backwards for project name
                        for j in range(i-1, max(0, i-5), -1):
                            prev_line = lines[j].strip()
                            if prev_line and not prev_line.startswith('(') and len(prev_line) > 5:
                                if 'updates:' not in prev_line.lower() and 'project description:' not in prev_line.lower():
                                    completed_2022_projects.append(prev_line)
                                    break

result = {
    'funding_records': len(df_funding),
    'civic_documents': len(civic_docs),
    'park_projects_found': len(park_projects),
    'total_park_funding': int(park_projects['Amount'].sum()),
    'completed_2022_projects_raw': len(completed_2022_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
