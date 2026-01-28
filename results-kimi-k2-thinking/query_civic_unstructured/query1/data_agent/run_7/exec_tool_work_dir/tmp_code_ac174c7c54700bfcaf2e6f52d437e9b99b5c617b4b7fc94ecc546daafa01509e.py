code = """import json

# Get data from storage
mongo_path = locals().get('var_functions.query_db:10')
funding_path = locals().get('var_functions.query_db:22')

# Load MongoDB data
mongo_docs = []
if mongo_path and isinstance(mongo_path, str) and mongo_path.endswith('.json'):
    with open(mongo_path, 'r') as f:
        mongo_docs = json.load(f)
elif mongo_path:
    mongo_docs = mongo_path

# Load funding data  
funding_records = []
if funding_path and isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_records = json.load(f)
elif funding_path:
    funding_records = funding_path

print('Loaded data. Docs:', len(mongo_docs), 'Funding records:', len(funding_records))

# Build funding list of projects over 50000
funded_projects = []
for rec in funding_records:
    amt = int(rec.get('Amount', 0))
    if amt > 50000:
        funded_projects.append(rec.get('Project_Name', ''))

print('Found', len(funded_projects), 'projects with funding over 50000')

# Extract design projects from MongoDB
design_names = []
for doc in mongo_docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        section = txt.split('Capital Improvement Projects (Design)')[1]
        # Look for project name patterns in this section
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 10:
                if not line.startswith('(') and not line.isupper():
                    if 'Page' not in line and 'Item' not in line:
                        if 'Public Works' not in line and 'Updates' not in line:
                            design_names.append(line)

print('Found', len(set(design_names)), 'potential design projects')

# Match by finding common words
common = set(['road','repair','project','improvements','and','the','repairs'])
matches = set()
for design in set(design_names):
    d_words = set(design.lower().split()) - common
    for funded in funded_projects:
        f_words = set(funded.lower().split()) - common
        if len(d_words.intersection(f_words)) >= 2:
            matches.add(funded)

result = json.dumps({'count': len(matches)})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
