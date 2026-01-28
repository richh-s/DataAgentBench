code = """import json

# Get data from storage
mongo_path = locals().get('var_functions.query_db:47')
funding_path = locals().get('var_functions.query_db:46')

# Load MongoDB data
mongo_docs = []
if mongo_path and isinstance(mongo_path, str) and '.json' in mongo_path:
    with open(mongo_path, 'r') as f:
        mongo_docs = json.load(f)
elif mongo_path and isinstance(mongo_path, list):
    mongo_docs = mongo_path

# Load funding data  
funding_recs = []
if funding_path and isinstance(funding_path, str) and '.json' in funding_path:
    with open(funding_path, 'r') as f:
        funding_recs = json.load(f)
elif funding_path and isinstance(funding_path, list):
    funding_recs = funding_path

print('Loaded {0} docs and {1} funding records'.format(len(mongo_docs), len(funding_recs)))

# Build funding map for projects > 50000
funding_map = {}
for rec in funding_recs:
    amount = int(rec.get('Amount', 0))
    name = rec.get('Project_Name', '')
    if amount > 50000 and name:
        funding_map[name] = amount

print('Funding map size:', len(funding_map))

# Extract design projects from MongoDB texts
design_candidates = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for design section
    if 'Capital Improvement Projects (Design)' in text:
        # Get everything after the design marker
        design_section = text.split('Capital Improvement Projects (Design)')[1]
        # Cut off before construction section if present
        if 'Capital Improvement Projects (Construction)' in design_section:
            design_section = design_section.split('Capital Improvement Projects (Construction)')[0]
        
        # Extract candidate project names
        for line in design_section.split('\n'):
            line = line.strip()
            # Skip noise
            if not line or len(line) < 5:
                continue
            if line.startswith('(') or line.endswith(':'):
                continue
            if any(skip in line for skip in ['Updates:', 'Schedule:', 'Page', 'Item', 'Public Works', 'Commission', 'Agenda', 'Subject:', 'To:', 'From:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Capital Improvement']):
                continue
            if line.isupper():
                continue
            
            design_candidates.add(line)

print('Design candidates found:', len(design_candidates))

# Match projects using word overlap
def get_key_words(name):
    words = set(name.lower().split())
    stop_words = {'road', 'repair', 'repairs', 'improvements', 'improvement', 'and', 'the', 'project', 'drain', 'drainage', 'storm'}
    return words - stop_words

matched_projects = []
for design in design_candidates:
    design_keys = get_key_words(design)
    if not design_keys:
        continue
    
    for funded_name in funding_map:
        funded_keys = get_key_words(funded_name)
        
        # Check overlap
        overlap = design_keys.intersection(funded_keys)
        if len(overlap) >= 2:
            matched_projects.append(funded_name)
            break

# Count unique matches
unique_count = len(set(matched_projects))
print('Total matches:', unique_count)

# Return result
result = json.dumps({'count': unique_count, 'matched_projects': list(set(matched_projects))[:10]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:47': 'file_storage/functions.query_db:47.json'}

exec(code, env_args)
