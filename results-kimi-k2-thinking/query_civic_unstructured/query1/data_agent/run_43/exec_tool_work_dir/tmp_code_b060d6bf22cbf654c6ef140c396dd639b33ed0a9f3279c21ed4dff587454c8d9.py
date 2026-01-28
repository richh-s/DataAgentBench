code = """import json, os

# Get all JSON files in tmp directory
files = [f for f in os.listdir('/root/tmp') if f.endswith('.json')]

# Load the files - find them by checking content
funding_data = None
civic_docs = None

for filename in files:
    path = os.path.join('/root/tmp', filename)
    with open(path) as f:
        data = json.load(f)
    
    # Check if this looks like funding data (has Amount field)
    if isinstance(data, list) and len(data) > 0 and 'Amount' in (data[0] if data else {}):
        funding_data = data
    # Otherwise it's likely civic docs (has text field)
    elif isinstance(data, list) and len(data) > 0 and 'text' in (data[0] if data else {}):
        civic_docs = data

# Build funding map with amounts > 50000
funding_map = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_map[item['Project_Name']] = amount

# Find design capital projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and 'Page' not in line:
                design_projects.add(line.replace('•', '').strip())

# Count matches
count = 0
for proj in design_projects:
    for funded_name, amount in funding_map.items():
        p_lower = proj.lower()
        f_lower = funded_name.lower()
        if (p_lower in f_lower or f_lower in p_lower) and abs(len(proj) - len(funded_name)) < 40:
            count += 1
            break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
