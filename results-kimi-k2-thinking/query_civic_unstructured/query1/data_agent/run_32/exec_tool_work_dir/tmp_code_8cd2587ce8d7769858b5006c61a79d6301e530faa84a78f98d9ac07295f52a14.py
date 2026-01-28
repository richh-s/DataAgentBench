code = """import json, re

# Load data files
docs = json.load(open(str(locals()['var_functions.query_db:5'])))
funding_recs = json.load(open(str(locals()['var_functions.query_db:30'])))

# Build funding map
funded = {rec['Project_Name']: int(rec['Amount']) for rec in funding_recs}

projects = set()

# Find capital design projects
for doc in docs:
    txt = doc.get('text', '')
    
    # Find design section
    pattern = r'Capital Improvement Projects \(Design\)(.*?)Capital Improvement Projects \(Construction\)'
    match = re.search(pattern, txt, re.DOTALL)
    
    if match:
        section = match.group(1)
        for line in section.split('\n'):
            clean = line.strip()
            if clean in funded and 'fema' not in clean.lower():
                projects.add(clean)

result = len(projects)
print('__RESULT__:')
print(str(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
