code = """import json
# Load data
mongo_key = 'var_functions.query_db:10'
funding_key = 'var_functions.query_db:22'
mongo_docs = locals()[mongo_key] if mongo_key in locals() else []
funding_recs = locals()[funding_key] if funding_key in locals() else []

# If they are file paths, load them
if isinstance(mongo_docs, str) and '.json' in mongo_docs:
    with open(mongo_docs, 'r') as f:
        mongo_docs = json.load(f)

if isinstance(funding_recs, str) and '.json' in funding_recs:
    with open(funding_recs, 'r') as f:
        funding_recs = json.load(f)

# Build funding map
funding_map = {}
for rec in funding_recs:
    name = rec['Project_Name']
    amount = int(rec['Amount'])
    if amount > 50000:
        funding_map[name] = amount

# Extract design projects from MongoDB text
design_projects = []
for doc in mongo_docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        part = text.split('Capital Improvement Projects (Design)')[1]
        for line in part.split('\n'):
            line = line.strip()
            if line and len(line) > 8 and not line.startswith('(') and 'Page' not in line:
                if 'Public Works' not in line and 'Commission' not in line and 'Updates:' not in line:
                    design_projects.append(line)

# Match projects by checking word overlap
def clean_words(name):
    return set(name.lower().replace('project', '').split()) - {'road','repair','improvements','and','the'}

matched = []
for design in design_projects:
    ds = clean_words(design)
    for funded in funding_map:
        fs = clean_words(funded)
        if len(ds.intersection(fs)) >= 2:
            if funded not in [m['name'] for m in matched]:
                matched.append({'name': funded, 'amount': funding_map[funded]})
                break

print('__RESULT__:')
print(json.dumps({'count': len(matched)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
