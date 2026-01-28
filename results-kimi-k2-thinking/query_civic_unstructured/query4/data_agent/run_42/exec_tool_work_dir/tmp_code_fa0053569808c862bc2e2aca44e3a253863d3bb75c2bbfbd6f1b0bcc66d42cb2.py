code = """import json
import re

# Read MongoDB results
mongo_file_path = 'var_functions.query_db:42'
funding_file_path = 'var_functions.query_db:4'

with open(mongo_file_path, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_file_path, 'r') as f:
    funding_records = json.load(f)

# Create funding lookup dictionary
funding_lookup = {}
for rec in funding_records:
    funding_lookup[rec['Project_Name']] = int(rec['Amount'])

# Extract Spring 2022 projects
spring_projects = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for Spring 2022 construction starts
    # Pattern: project name section followed by Begin Construction with Spring 2022
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Check if this line contains construction schedule with Spring 2022
        if 'Begin Construction' in line and '2022' in line and 'Spring' in line:
            # Look backwards to find project name (usually within previous 10 lines)
            for j in range(i-1, max(0, i-15), -1):
                prev_line = lines[j].strip()
                # Skip empty lines, page references, and metadata
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('Page'):
                    # Skip schedule/update lines
                    if 'Schedule' not in prev_line and 'Updates' not in prev_line:
                        # Skip section headers
                        if prev_line not in ['Capital Improvement Projects (Design)', 
                                           'Capital Improvement Projects (Construction)',
                                           'Capital Improvement Projects (Not Started)',
                                           'Capital Improvement Projects (Completed)',
                                           'Disaster Projects (Design)']:
                            spring_projects.add(prev_line)
                            break

# Match with funding data
matched_projects = []
for proj in spring_projects:
    if proj in funding_lookup:
        matched_projects.append({
            'project_name': proj,
            'funding_amount': funding_lookup[proj]
        })

# Calculate totals
total_count = len(matched_projects)
total_funding = sum(p['funding_amount'] for p in matched_projects)

# Format result
result = {
    'project_count': total_count,
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
