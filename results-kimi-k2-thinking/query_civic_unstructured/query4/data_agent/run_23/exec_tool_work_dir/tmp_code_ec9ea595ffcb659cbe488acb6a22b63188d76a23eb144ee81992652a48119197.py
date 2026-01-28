code = """import json
import pandas as pd
import re

# Access data
civic_docs_file = locals()['var_functions.query_db:16']
funding_file = locals()['var_functions.query_db:17']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

# Create funding DataFrame
df_funding = pd.DataFrame(funding)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Extract projects with start dates from civic documents
projects_with_dates = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project patterns more carefully
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if this line looks like a project name
        if (len(line) > 10 and len(line) < 150 and 
            not line.startswith('To:') and not line.startswith('From:') and
            not line.startswith('Date:') and not line.startswith('Page') and
            not line.startswith('Item') and not line.startswith('Prepared by:') and
            not line.startswith('Approved by:') and not line.startswith('Subject:')):
            
            # Check if next few lines contain schedule info
            next_lines = ' '.join(lines[i+1:i+4]).lower()
            
            # Spring 2022 patterns
            spring_patterns = [
                r'2022[-\s]spring',
                r'2022[-\s]march',
                r'2022[-\s]april',
                r'2022[-\s]may',
                r'2022[-\s]03',
                r'2022[-\s]04',
                r'2022[-\s]05'
            ]
            
            has_spring_2022 = any(re.search(pattern, next_lines) for pattern in spring_patterns)
            
            if has_spring_2022:
                current_project = line
                # Clean project name
                current_project = re.sub(r'^[\d\.]+\s*', '', current_project)
                current_project = re.sub(r'\s+', ' ', current_project).strip()
                
                projects_with_dates.append({
                    'Project_Name': current_project,
                    'Start_Date_Info': 'Spring 2022',
                    'doc_id': doc.get('_id')
                })

# Deduplicate by project name
unique_projects = []
seen_names = set()
for proj in projects_with_dates:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

df_projects = pd.DataFrame(unique_projects)

print('__RESULT__:')
print(json.dumps({
    'spring_2022_projects_found': len(df_projects),
    'sample_projects': df_projects.head(10).to_dict('records') if not df_projects.empty else []
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:22': {'civic_docs_count': 5, 'funding_count': 500, 'sample_civic_doc_filename': 'malibucity_agenda_03222023-2060.txt', 'total_funding_available': 28094000}}

exec(code, env_args)
