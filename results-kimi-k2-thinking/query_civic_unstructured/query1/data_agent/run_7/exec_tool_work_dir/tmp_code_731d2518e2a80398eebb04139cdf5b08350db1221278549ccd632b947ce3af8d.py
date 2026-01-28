code = """import json

# Get the data directly from storage
mongo_docs = locals().get('var_functions.query_db:10', [])
funding_records = locals().get('var_functions.query_db:22', [])

# Check if these are file paths or actual data
if mongo_docs and isinstance(mongo_docs, list) and len(mongo_docs) > 0 and isinstance(mongo_docs[0], dict):
    pass
else:
    mongo_docs = []

if funding_records and isinstance(funding_records, list) and len(funding_records) > 0 and isinstance(funding_records[0], dict):
    pass
else:
    funding_records = []

print('Using', len(mongo_docs), 'documents and', len(funding_records), 'funding records')

# Build set of funded projects over 50000
funded_names = set()
amounts = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amt = int(rec.get('Amount', 0))
    if name and amt > 50000:
        funded_names.add(name)
        amounts[name] = amt

# Find design projects from text
design_candidates = []
common_terms = ['Public Works', 'Commission', 'Agenda', 'Updates:', 'Schedule:', 'Complete Design', 'Advertise', 'Begin Construction', 'Page', 'Item']

for doc in mongo_docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        section = txt.split('Capital Improvement Projects (Design)')[1].split('Capital Improvement Projects (Construction)')[0]
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 8 and not any(term in line for term in common_terms):
                if not line.startswith('(') and not line.isupper():
                    design_candidates.append(line)

# Match projects
def get_key_words(name):
    return set(name.lower().replace('project', '').split()) - {'road','repair','improvements','and','the'}

matched = []
for design in set(design_candidates):
    dkey = get_key_words(design)
    for funded in funded_names:
        fkey = get_key_words(funded)
        if len(dkey.intersection(fkey)) >= 2:
            matched.append(funded)
            break

result = json.dumps({'count': len(matched)})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
