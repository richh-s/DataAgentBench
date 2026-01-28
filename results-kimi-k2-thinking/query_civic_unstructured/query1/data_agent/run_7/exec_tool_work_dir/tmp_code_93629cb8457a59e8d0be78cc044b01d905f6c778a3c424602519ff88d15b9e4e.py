code = """import json

# Load data from storage
mongo_result = locals().get('var_functions.query_db:10')
funding_result = locals().get('var_functions.query_db:22')

# Read files if paths are provided
mongo_docs = []
funding_records = []

if isinstance(mongo_result, str) and '.json' in mongo_result:
    with open(mongo_result, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_result or []

if isinstance(funding_result, str) and '.json' in funding_result:
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result or []

# Build funding map with amounts > 50000
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if name and amount > 50000:
        funding_map[name] = amount

# Extract design projects from MongoDB texts
design_project_candidates = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_part = parts[1]
        project_lines = [line.strip() for line in design_part.split('\n') if line.strip()]
        for line in project_lines:
            if len(line) > 8 and not line.startswith('(') and not line.endswith(':') and line == line.strip():
                skip_terms = ['Page', 'Item', 'Agenda', 'Public Works', 'Commission', 'Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction']
                if not any(term in line for term in skip_terms):
                    design_project_candidates.add(line)

print('Found {} design project candidates'.format(len(design_project_candidates)))

# Match design candidates with funded projects
def clean_words(name):
    words = name.lower().replace('project','').strip().split()
    common = {'road','repair','repairs','improvements','and','the','improvement','project'}
    return set(words) - common

matched_projects = []
for candidate in design_project_candidates:
    candidate_words = clean_words(candidate)
    for funded_name, amount in funding_map.items():
        funded_words = clean_words(funded_name)
        overlap = candidate_words.intersection(funded_words)
        if len(overlap) >= 2:
            if funded_name not in [p['name'] for p in matched_projects]:
                matched_projects.append({'name': funded_name, 'amount': amount, 'candidate': candidate})
            break

# Return final count
result = json.dumps({'count': len(matched_projects), 'sample': matched_projects[:3]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
