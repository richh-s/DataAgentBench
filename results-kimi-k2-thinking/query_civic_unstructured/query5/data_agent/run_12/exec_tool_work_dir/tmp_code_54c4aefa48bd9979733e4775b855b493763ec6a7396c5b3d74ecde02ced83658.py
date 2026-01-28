code = """import json
import pandas as pd
import re

# Load funding data
funding_file_path = locals()['var_functions.query_db:5']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_file_path = locals()['var_functions.query_db:0']
with open(civic_file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Process funding data
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Find disaster-related projects
disaster_mask = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Cal OES|disaster', case=False, na=False)
disaster_projects = funding_df[disaster_mask]

# Process civic docs to find projects with 2022 start dates
disaster_projects_with_dates = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for project sections
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        # Check if this section mentions both disaster/FEMA and 2022
        has_disaster = re.search(r'FEMA|Cal.?OES|CalJPIA|disaster|recovery', section, re.IGNORECASE)
        has_2022 = re.search(r'2022', section)
        
        if has_disaster and has_2022:
            # Extract project names from this section
            lines = section.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) < 150 and not line.startswith(('(', '•', '-', '●')):
                    # Check if this line looks like a project name
                    if any(keyword in line.lower() for keyword in ['project', 'improvement', 'repair', 'replacement']):
                        disaster_projects_with_dates.append({
                            'project_line': line,
                            'section': section[:200] + '...' if len(section) > 200 else section
                        })

# Create a list of disaster project names to match with funding
project_names = []
for project in disaster_projects.to_dict('records'):
    project_names.append(project['Project_Name'])

result = {
    'total_disaster_projects': len(disaster_projects),
    'total_disaster_funding': int(disaster_projects['Amount'].sum()),
    'sample_disaster_project_names': project_names[:10],
    'projects_with_2022_mentions': len(disaster_projects_with_dates),
    'sample_2022_mentions': disaster_projects_with_dates[:5]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
