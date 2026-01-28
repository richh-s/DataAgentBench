code = """import json
import re

# Read the civic documents
file_path = var_functions.query_db:12
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f'Total documents: {len(civic_docs)}')

# Find disaster projects
# Look for FEMA, CalOES, CalJPIA in project names or descriptions
disaster_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check for disaster-related keywords
    if any(keyword in text for keyword in ['FEMA', 'CalOES', 'CalJPIA']):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for project-like lines near disaster keywords
            if len(line) > 10 and len(line) < 150:
                if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA']):
                    # Clean up the line
                    clean_line = re.sub(r'[^\w\s\-\(\)]+', '', line).strip()
                    disaster_projects.append(clean_line)

# Remove duplicates
disaster_projects = list(set(disaster_projects))

print(f'Found {len(disaster_projects)} disaster-related projects')
for proj in disaster_projects[:10]:
    print(f'- {proj}')

# Now check which ones have 2022 in the document
projects_with_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        for proj in disaster_projects:
            if proj in text:
                projects_with_2022.append(proj)

projects_with_2022 = list(set(projects_with_2022))
print(f'\nDisaster projects with 2022 references: {len(projects_with_2022)}')
for proj in projects_with_2022:
    print(f'- {proj}')

result = {
    'disaster_projects_2022': projects_with_2022,
    'count': len(projects_with_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:4': [], 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
