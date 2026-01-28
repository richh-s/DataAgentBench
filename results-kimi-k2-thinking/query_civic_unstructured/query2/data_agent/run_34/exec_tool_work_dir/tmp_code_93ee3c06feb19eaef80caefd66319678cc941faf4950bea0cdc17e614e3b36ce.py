code = """import json

# Read civic documents
civic_docs = json.load(open(var_functions.query_db:0))

# Simple pattern matching for park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for park projects with 2022 completion
    if 'park' in text.lower() and '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line_lower = line.lower()
            if 'park' in line_lower and ('construction was completed' in line_lower or 'completed' in line_lower):
                if '2022' in line_lower:
                    park_projects_2022.append(line.strip())

# Remove duplicates and clean up
unique_projects = list(set(park_projects_2022))

# Try to extract project names more cleanly
project_names = []
for line in unique_projects:
    # Remove common prefixes/suffixes
    clean_line = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
    if len(clean_line) > 5:
        project_names.append(clean_line)

result = {'count': len(project_names), 'projects': project_names}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:40': ['civic_docs']}

exec(code, env_args)
