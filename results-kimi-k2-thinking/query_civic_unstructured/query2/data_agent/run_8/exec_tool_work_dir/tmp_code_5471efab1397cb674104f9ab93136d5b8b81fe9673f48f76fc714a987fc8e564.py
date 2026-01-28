code = """import json
import pandas as pd
import re

civic_docs_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

civic_docs = json.load(open(civic_docs_path))
funding = json.load(open(funding_path))

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if (line.isupper() or 'Project' in line) and 10 < len(line) < 200:
            current_project = line
        
        if current_project:
            status = None
            et = None
            topic = ''
            
            lower_line = line.lower()
            if 'completed' in lower_line:
                status = 'completed'
                year_match = re.search(r'(20\d\d)', line)
                if year_match:
                    et = year_match.group(1)
            
            if 'park' in current_project.lower():
                topic = 'park'
            
            if status and et and topic:
                projects.append({
                    'Project_Name': current_project,
                    'status': status,
                    'et': et,
                    'topic': topic
                })

projects_df = pd.DataFrame(projects)
park_2022 = projects_df[
    (projects_df['topic'] == 'park') & 
    (projects_df['status'] == 'completed') & 
    (projects_df['et'] == '2022')
]

project_names = park_2022['Project_Name'].unique()
total_funding = 0
for name in project_names:
    matches = funding_df[funding_df['Project_Name'].str.contains('park', case=False, na=False)]
    for _, row in matches.iterrows():
        if any(word in row['Project_Name'].lower() for word in name.lower().split()[:3]):
            total_funding += row['Amount']

result = {'total_funding': int(total_funding)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
