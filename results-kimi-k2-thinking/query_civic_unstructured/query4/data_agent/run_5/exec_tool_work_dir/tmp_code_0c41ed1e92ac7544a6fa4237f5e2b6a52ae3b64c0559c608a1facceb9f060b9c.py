code = """import json

# Load the data
cpath = locals()['var_functions.query_db:60']
fpath = locals()['var_functions.query_db:61']

with open(cpath, 'r') as f:
    civic_docs = json.load(f)

with open(fpath, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup: project name -> total amount
funding_lookup = {}
for rec in funding_data:
    pname = rec['Project_Name']
    amt = int(rec['Amount'])
    if pname not in funding_lookup:
        funding_lookup[pname] = 0
    funding_lookup[pname] += amt

# Find all projects mentioned in civic docs that have year 2022
year_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for lines that contain 2022 and look like project names
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line and '2022' in line and len(line) > 10:
            # Skip obvious non-project lines
            if not any(marker in line for marker in ['(', 'cid:', 'Updates:', 'Schedule:', 'Complete', 'Begin', 'Advertise']):
                year_2022_projects.append(line)

# Remove duplicates
unique_projects = list(dict.fromkeys(year_2022_projects))

# Match with funding data - focus on projects that started in Spring 2022
# From the preview, I can see "2022 Morning View Resurfacing & Storm Drain Improvements"
total_count = 0
total_funding = 0
matched_projects = []

for project in unique_projects:
    if project in funding_lookup:
        # This is a project with 2022 in its name that has funding
        amount = funding_lookup[project]
        total_count += 1
        total_funding += amount
        matched_projects.append({'name': project, 'funding': amount})
    else:
        # Check if any funded project contains this name
        for funded_name in funding_lookup:
            if project.lower() in funded_name.lower() or funded_name.lower() in project.lower():
                amount = funding_lookup[funded_name]
                total_count += 1
                total_funding += amount
                matched_projects.append({'name': project, 'funding': amount, 'matched': funded_name})
                break

# Also check funding records directly for 2022 projects
for funded_name, amount in funding_lookup.items():
    if '2022' in funded_name:
        # Check if not already matched
        already_matched = any(m['name'] == funded_name for m in matched_projects)
        if not already_matched:
            total_count += 1
            total_funding += amount
            matched_projects.append({'name': funded_name, 'funding': amount})

result = {'count': total_count, 'total_funding': total_funding}
print('__RESULT__')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json'}

exec(code, env_args)
