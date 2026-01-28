code = """import json

# Access the data from the tool results
civic_docs_var = locals()['var_functions.query_db:6']

# Load civic documents
civic_docs = []
if isinstance(civic_docs_var, str) and civic_docs_var.endswith('.json'):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(civic_docs_var)

# Load funding data
funding_var = locals()['var_functions.query_db:7']
funding_data = []
if isinstance(funding_var, str) and funding_var.endswith('.json'):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = list(funding_var)

# Build lookup for disaster-related funding
disaster_lookup = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    if '(FEMA' in name or '(CalOES' in name or '(CalJPIA' in name:
        disaster_lookup[name.strip()] = int(record.get('Amount', 0))

# Find disaster projects with 2022 dates
found_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        # Check for disaster markers
        has_disaster = '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line
        if has_disaster:
            proj_name = line.strip()
            # Check context for 2022
            context_start = max(0, i-5)
            context_end = min(len(lines), i+6)
            for j in range(context_start, context_end):
                if '2022' in lines[j]:
                    indicators = ['Start', 'Schedule', 'Complete', 'Begin', 'Design', 'Construction', 'Advertise']
                    for indicator in indicators:
                        if indicator in lines[j]:
                            found_projects.add(proj_name)
                            break
                    break

# Match with funding
matched = []
total = 0
for proj_name in found_projects:
    if proj_name in disaster_lookup:
        amount = disaster_lookup[proj_name]
        matched.append({'name': proj_name, 'amount': amount})
        total += amount
    else:
        for funding_name in disaster_lookup.keys():
            if proj_name in funding_name or funding_name in proj_name:
                amount = disaster_lookup[funding_name]
                matched.append({'name': funding_name, 'amount': amount})
                total += amount
                break

# Add projects with 2022 in name from funding data
for funding_name in disaster_lookup.keys():
    has_2022 = '2022' in funding_name
    already_included = any(m['name'] == funding_name for m in matched)
    if has_2022 and not already_included:
        amount = disaster_lookup[funding_name]
        matched.append({'name': funding_name, 'amount': amount})
        total += amount

result = {
    'projects': matched,
    'total_funding': total,
    'project_count': len(matched)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
