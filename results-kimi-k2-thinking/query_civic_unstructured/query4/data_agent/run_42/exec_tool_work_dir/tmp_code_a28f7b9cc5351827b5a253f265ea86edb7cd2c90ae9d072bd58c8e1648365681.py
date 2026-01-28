code = """import json
import re

# Access the MongoDB and funding data from the stored variables
mongo_data = var_functions.query_db:14
funding_data = var_functions.query_db:4

# Load JSON data
mongo_docs = json.loads(open(mongo_data).read())
funding_recs = json.loads(open(funding_data).read())

# Create funding lookup dictionary
funding_lookup = {}
for rec in funding_recs:
    funding_lookup[rec['Project_Name']] = int(rec['Amount'])

# Extract projects starting in Spring 2022
spring_projects = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for projects with Spring 2022 construction start
    # Pattern: Find project names followed by construction schedule
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'Begin Construction' in line and '2022' in line:
            # Look backwards to find project name (within previous 10 lines)
            for j in range(i-1, max(0, i-12), -1):
                prev_line = lines[j].strip()
                # Valid project name: not empty, not metadata, not a section header
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('Page'):
                    if 'Schedule' not in prev_line and 'Updates' not in prev_line:
                        if len(prev_line) > 5 and prev_line not in ['Capital Improvement Projects (Design)', 'Disaster Projects (Design)']:
                            spring_projects.add(prev_line)
                            break

# Match projects with funding data
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

# Format final answer
result = {
    'project_count': total_count,
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
