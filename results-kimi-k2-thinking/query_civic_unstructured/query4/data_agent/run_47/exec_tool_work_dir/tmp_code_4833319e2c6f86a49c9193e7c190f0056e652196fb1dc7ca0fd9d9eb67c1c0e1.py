code = """import json
import os

# Load the data files
civic_file_path = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_68.json'
funding_file_path = '/tmp/results/20250219_143343_sqlite_funding_database_query_12.json'

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Extract project names from documents with 2022 references
projects_2022 = set()
search_terms = ['2022', 'Spring', 'spring', 'Advertise', 'Begin']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip header lines
        skip_patterns = ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:', 'PREPARED BY', 'APPROVED BY', 'DATE PREPARED', 'DISCUSSION:']
        should_skip = False
        for pattern in skip_patterns:
            if pattern in line:
                should_skip = True
                break
        
        if should_skip:
            continue
        
        # Look for project names
        if line.isupper() and len(line) > 15:
            # Check following lines for 2022 Spring scheduling
            following = '\n'.join(lines[i:i+15])
            has_2022 = '2022' in following
            has_spring = 'pring' in following.lower() or 'Spring' in following
            if has_2022 and has_spring:
                projects_2022.add(line)
        elif '2022' in line and len(line) > 10 and not line.startswith('Page'):
            projects_2022.add(line)

# Clean projects
final_projects = []
for proj in projects_2022:
    if len(proj) > 15 and not proj.startswith('PAGE'):
        final_projects.append(proj)

# Get total funding
total_funding = 0
for proj in final_projects:
    for fund in funding_data:
        if fund.get('Project_Name') == proj:
            total_funding += int(fund.get('Amount', 0))

result = {
    'project_count': len(final_projects),
    'total_funding': total_funding,
    'projects': sorted(final_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:62': {'status': 'files_loaded'}, 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
