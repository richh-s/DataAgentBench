code = """import json

# Load data from files
civic_docs = json.load(open('/tmp/tmp5.json'))
funding_data = json.load(open('/tmp/tmp6.json'))

# Build funding lookup: project name -> total amount
funding_lookup = {}
for rec in funding_data:
    proj_name = rec['Project_Name']
    amount = int(rec['Amount'])
    funding_lookup[proj_name] = funding_lookup.get(proj_name, 0) + amount

# Find projects with 2022 in civic documents
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = [ln.strip() for ln in text.split('\n') if ln.strip()]
    
    for i in range(len(lines)):
        line = lines[i]
        # Look for project names containing 2022
        if '2022' in line and len(line) > 10:
            # Skip lines that are clearly schedule lines
            schedule_words = ['Complete:', 'Begin:', 'Advertise:', 'Construction:']
            if not any(word in line for word in schedule_words):
                projects_2022.append(line)

# Remove duplicates
unique_projects = list(dict.fromkeys(projects_2022))

# Match with funding data
count = 0
total = 0

for project in unique_projects:
    # Direct match
    if project in funding_lookup:
        count += 1
        total += funding_lookup[project]
    else:
        # Try partial match using first word
        first_word = project.split()[0] if project.split() else ''
        if len(first_word) > 5:  # avoid matching 'The', 'City' etc.
            for funded_name in funding_lookup:
                if funded_name.startswith(first_word):
                    count += 1
                    total += funding_lookup[funded_name]
                    break

# Also include funding records with 2022 in name
for funded_name, amount in funding_lookup.items():
    if '2022' in funded_name and funded_name not in unique_projects:
        if 'Morning View' in funded_name or 'Annual' in funded_name:
            count += 1
            total += amount

result = {
    'count': count,
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json'}

exec(code, env_args)
