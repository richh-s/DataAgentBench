code = """import json
import re

# Read civic documents with Spring 2022 filters
civic_file = locals()['var_functions.query_db:38']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Total civic documents loaded:', len(civic_docs))

# Read funding data
funding_file = locals()['var_functions.query_db:36']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Total funding records loaded:', len(funding_data))

# Create funding map
funding_map = {}
for item in funding_data:
    proj_name = item['Project_Name'].lower()
    amount = int(item['Amount'])
    funding_map[proj_name] = amount

print('Funding map created with', len(funding_map), 'entries')

# Look for Spring 2022 projects in the civic documents
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Find project sections - look for project names followed by schedules
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty or special lines
        if not line or line.startswith('(') or 'cid:' in line or '_' in line:
            continue
            
        # Look for project schedule lines with Spring 2022
        if re.search(r'Begin[^:]*(?:Spring|March|April|May)[^\n]*2022', line, re.IGNORECASE):
            # Look backwards for project name (previous non-empty line that's not a header)
            for j in range(i-1, max(0, i-10), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not 'cid:' in prev_line and len(prev_line) < 100:
                    # Check if this looks like a project name (not a category)
                    if not any(cat in prev_line for cat in ['Capital Improvement', 'Disaster Projects', 'Design', 'Construction', 'Not Started', 'Completed']):
                        spring_projects.append(prev_line.lower())
                        break

print('Found', len(spring_projects), 'Spring 2022 projects')

# Match with funding
matched_projects = []
matched_names = set()

for proj_name in spring_projects:
    if proj_name in funding_map:
        if proj_name not in matched_names:
            matched_projects.append({
                'name': proj_name,
                'funding': funding_map[proj_name]
            })
            matched_names.add(proj_name)

# Calculate totals
total_funding = sum(p['funding'] for p in matched_projects)

print('Matched projects:', len(matched_projects))
print('Total funding: $', total_funding)

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
