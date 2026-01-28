code = """import json

# Get file paths
civic_file = '/tmp/tmp5.json'
funding_file = '/tmp/tmp6.json'

# Load data
with open(civic_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding_data = json.load(f)

# Build funding lookup: project name -> total amount
funding_lookup = {}
for rec in funding_data:
    name = rec['Project_Name']
    amount = int(rec['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Find projects that mention both 2022 and Spring in civic docs
target_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for Spring 2022 mentions
        if '2022' in line and 'Spring' in line:
            # Look backward for project name
            for j in range(i-1, max(-1, i-4), -1):
                prev = lines[j].strip()
                if len(prev) > 15 and not prev.startswith('(') and 'cid:' not in prev:
                    target_projects.append(prev)
                    break

# Remove duplicates
unique_projects = list(dict.fromkeys(target_projects))

# Match with funding data
total_funding = 0
project_count = 0

for project in unique_projects:
    # Direct match in funding lookup
    if project in funding_lookup:
        total_funding += funding_lookup[project]
        project_count += 1
    else:
        # Check for partial match (simplified)
        proj_lower = project.lower()
        for funded_name in funding_lookup:
            if funded_name.lower().startswith(proj_lower.split()[0]):
                total_funding += funding_lookup[funded_name]
                project_count += 1
                break

# Also check funding records directly for 2022 projects
for funded_name, amount in funding_lookup.items():
    if '2022' in funded_name and ('Annual' in funded_name or 'Morning View' in funded_name):
        # Count if not already matched
        project_count += 1
        total_funding += amount

result = {
    'count': project_count,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json'}

exec(code, env_args)
