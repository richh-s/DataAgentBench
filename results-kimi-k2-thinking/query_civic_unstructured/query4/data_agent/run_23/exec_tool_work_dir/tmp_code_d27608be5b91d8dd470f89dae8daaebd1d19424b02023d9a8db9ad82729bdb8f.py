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
    
    # Look for project patterns - project name followed by schedule info
    # Pattern: project name on its own line, then schedule info
    project_blocks = re.findall(r'([A-Za-z0-9\s&\-\(\)]+?)\n.*?project schedule.*?\n([^\n]+)', text, re.IGNORECASE|re.DOTALL)
    
    for project_name, schedule_text in project_blocks:
        project_name = project_name.strip()
        if project_name and len(project_name) < 200:  # Filter out garbage
            # Clean up project name
            project_name = re.sub(r'^[\d\.]+\s*', '', project_name)  # Remove leading numbers like "4.B."
            project_name = re.sub(r'\s+', ' ', project_name)  # Normalize whitespace
            
            # Check for Spring 2022 dates
            schedule_lower = schedule_text.lower()
            
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
            
            has_spring_2022 = any(re.search(pattern, schedule_lower) for pattern in spring_patterns)
            
            if has_spring_2022:
                projects_with_dates.append({
                    'Project_Name': project_name,
                    'Start_Date_Info': schedule_text.strip(),
                    'doc_id': doc.get('_id')
                })

# Create DataFrame of projects starting in Spring 2022
df_projects = pd.DataFrame(projects_with_dates)

print('__RESULT__:')
print(json.dumps({
    'projects_found': len(df_projects),
    'sample_projects': df_projects.head(10).to_dict('records') if not df_projects.empty else []
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:22': {'civic_docs_count': 5, 'funding_count': 500, 'sample_civic_doc_filename': 'malibucity_agenda_03222023-2060.txt', 'total_funding_available': 28094000}}

exec(code, env_args)
