code = """import json, os, sys

# Get file paths from the tool results
funding_path = '/root/tmp/c_20240926150451_query_db_60.json'  # This is what the tool returned
civic_path = '/root/tmp/c_20240926145917_query_db_6.json'    # This is what the tool returned

# If the files don't exist at these exact paths, find them
if not os.path.exists(funding_path):
    # Look for similar files
    tmp_dir = '/root/tmp'
    files = os.listdir(tmp_dir)
    funding_files = [f for f in files if 'query_db_60' in f]
    civic_files = [f for f in files if 'query_db_6' in f and '_60' not in f]
    if funding_files:
        funding_path = os.path.join(tmp_dir, funding_files[0])
    if civic_files:
        civic_path = os.path.join(tmp_dir, civic_files[0])

# Load data
funding_data = json.load(open(funding_path))
civic_docs = json.load(open(civic_path))

# Build funding map
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Find design projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and not line.startswith('Page'):
                design_projects.add(line.replace('•', '').strip())

# Count with funding > 50000
count = 0
for proj in design_projects:
    for funded_name, amount in funding_map.items():
        if amount > 50000:
            p_lower = proj.lower()
            f_lower = funded_name.lower()
            if p_lower in f_lower or f_lower in p_lower:
                if abs(len(proj) - len(funded_name)) < 30:
                    count += 1
                    break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
