code = """import json, os, re

# Path to funding data
funding_path = locals().get('var_functions.query_db:14')
print('Funding data path:', type(funding_path))
print(funding_path)

# Read the JSON files
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals().get('var_functions.query_db:14', [])

# Path to civic docs data
civic_path = locals().get('var_functions.query_db:8')
print('Civic docs path:', type(civic_path))
print(civic_path)

# Read civic data
if isinstance(civic_path, str) and civic_path.endswith('.json'):
    with open(civic_path, 'r') as f:
        civic_data = json.load(f)
else:
    civic_data = locals().get('var_functions.query_db:8', [])

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_data))

# Extract project info from documents
projects = []
for doc in civic_data:
    text = doc.get('text', '')
    # Look for project entries with dates
    # Pattern: project name followed by various date formats
    project_blocks = re.findall(r'([A-Z][^\n]+?(?:2022[^\n]*))', text, re.MULTILINE)
    for block in project_blocks:
        lines = block.split('\n')
        if len(lines) > 0:
            name = lines[0].strip()
            # Check if disaster-related
            is_disaster = any(keyword in name for keyword in ['(FEMA', '(CalJPIA', '(CalOES', 'Fire', 'Emergency'])
            # Extract dates mentioning 2022
            start_date = ''
            date_patterns = [r'2022[^\n]*', r'Start[^\n]*2022[^\n]*', r'Begin[^\n]*2022[^\n]*']
            for pattern in date_patterns:
                match = re.search(pattern, block, re.IGNORECASE)
                if match:
                    start_date = match.group(0).strip()
                    break
            if is_disaster and '2022' in start_date:
                projects.append({
                    'name': name,
                    'start_date': start_date,
                    'is_disaster': is_disaster
                })

print('Disaster projects with 2022 dates:', len(projects))
for p in projects[:10]:
    print(p['name'], '->', p['start_date'])

# Map to funding data
funding_dict = {f['Project_Name'].lower(): int(f['Amount']) for f in funding_data}
total = 0
matched = []

for project in projects:
    proj_name = project['name']
    # Try exact match and variations
    for key, amount in funding_dict.items():
        if key in proj_name.lower() or proj_name.lower() in key or proj_name.replace('(FEMA Project)', '').strip().lower() in key:
            total += amount
            matched.append((proj_name, amount))
            break

print('Matched funding projects:', len(matched))
print('Total funding for disaster projects starting in 2022:', total)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
