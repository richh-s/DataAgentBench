code = """import json
import os

# Load the funding data
funding_path = '/tmp/results/20250219_143343_sqlite_funding_database_query_12.json'
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents from 2022 search
mongo_path = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_26.json'  # This is the "limit 50" query
with open(mongo_path, 'r') as f:
    civic_docs = json.load(f)

print(f'Loaded {len(funding_data)} funding records')
print(f'Loaded {len(civic_docs)} civic documents')

# Based on manual review of documents with 2022 in filename or text, 
# identify projects scheduled for Spring 2022
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for Spring 2022 scheduling
    if '2022' in text and ('spring' in text.lower() or 'Spring' in text):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10:
                continue
            
            # Skip headers
            if any(skip in line for skip in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:', 'PREPARED BY', 'APPROVED BY', 'DATE PREPARED']):
                continue
            
            # Find project names (uppercase or with year)
            is_project = False
            if line.isupper() and len(line) > 15:
                is_project = True
            elif '2022' in line and len(line) > 10 and not line.startswith('Page'):
                is_project = True
            
            if is_project:
                # Check if following lines mention Spring 2022
                following = '\n'.join(lines[i:i+15])
                if '2022' in following and 'pring' in following.lower():
                    spring_2022_projects.append(line)

# Remove duplicates
unique_projects = []
seen = set()
for proj in spring_2022_projects:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

unique_projects.sort()
print(f'\nSpring 2022 projects found: {len(unique_projects)}')
for proj in unique_projects:
    print(f'  - {proj}')

# Calculate total funding
total_funding = 0
funding_found = []

for project_name in unique_projects:
    for funding in funding_data:
        if funding.get('Project_Name') == project_name:
            amount = int(funding.get('Amount', 0))
            total_funding += amount
            funding_found.append((project_name, amount))
            break

print(f'\nTotal funding: ${total_funding:,}')
print(f'Projects with funding data: {len(funding_found)}')
for proj, amt in funding_found:
    print(f'  - {proj}: ${amt:,}')

# Create answer
result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'funded_projects': funding_found
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:62': {'status': 'files_loaded'}}

exec(code, env_args)
