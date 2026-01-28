code = """import json, pandas as pd, re

# Load data from file paths
civic_docs = json.load(open(locals()['var_functions.query_db:0'], 'r'))
funding = json.load(open(locals()['var_functions.query_db:1'], 'r'))

# Prepare funding DataFrame
funding_df = pd.DataFrame(funding)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Extract projects from civic documents
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Find project names
        if (line.isupper() or 'Project' in line) and 10 < len(line) < 200:
            current_project = line
        
        if current_project:
            # Check status
            status = None
            lower_line = line.lower()
            if 'completed' in lower_line:
                status = 'completed'
            
            # Check year
            et = None
            if status == 'completed':
                year_match = re.search(r'(20\d{2})', line)
                if year_match:
                    et = year_match.group(1)
            
            # Check if park-related
            topic = ''
            if 'park' in current_project.lower():
                topic = 'park'
            
            if status or et or topic:
                projects.append({
                    'Project_Name': current_project,
                    'status': status,
                    'et': et,
                    'topic': topic
                })

# Filter park projects completed in 2022
projects_df = pd.DataFrame(projects)
park_2022 = projects_df[
    (projects_df['topic'] == 'park') & 
    (projects_df['status'] == 'completed') & 
    (projects_df['et'] == '2022')
]

# Match with funding
project_names = park_2022['Project_Name'].unique()
total_funding = 0
matched_projects = []

for name in project_names:
    # Search for funding records
    matches = funding_df[funding_df['Project_Name'].str.contains(name.split()[0], case=False, na=False)]
    if not matches.empty and 'park' in matches.iloc[0]['Project_Name'].lower():
        funding_sum = matches['Amount'].sum()
        total_funding += funding_sum
        matched_projects.append({
            'project': name,
            'funding': int(funding_sum)
        })

result = {
    'total_funding': int(total_funding),
    'project_count': len(project_names),
    'matches': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
