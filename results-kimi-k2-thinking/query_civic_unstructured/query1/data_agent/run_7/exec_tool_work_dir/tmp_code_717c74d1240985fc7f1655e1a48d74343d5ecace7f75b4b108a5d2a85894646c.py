code = """import json

# Load data
mongo_data = locals().get('var_functions.query_db:10')
funding_data = locals().get('var_functions.query_db:22')

# Read files if needed
mongo_docs = []
funding_records = []

if mongo_data and isinstance(mongo_data, str) and '.json' in mongo_data:
    with open(mongo_data, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_data or []

if funding_data and isinstance(funding_data, str) and '.json' in funding_data:
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data or []

# Build set of funded projects
funded_projects = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if name and amount > 50000:
        funded_projects[name] = amount

# Extract design projects from text
all_design_projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    # Simple extraction of project names from Design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_text = parts[1].split('Capital Improvement Projects (Construction)')[0]
        lines = [l.strip() for l in design_text.split('\n') if l.strip()]
        # Add lines that appear to be project names
        for line in lines:
            if len(line) > 10 and not line.startswith('(') and 'Page' not in line and 'Item' not in line and 'Public Works' not in line:
                if line not in all_design_projects:
                    all_design_projects.append(line)

# Count matches more conservatively
matched_names = []
for design_proj in all_design_projects:
    design_key = design_proj.lower().replace('project','').strip()
    
    for funded_name in funded_projects:
        funded_key = funded_name.lower().replace('project','').strip()
        
        # Check for common words overlap
        design_words = set(design_key.split())
        funded_words = set(funded_key.split())
        
        # Remove very common words
        common = {'road','repair','repairs','improvements','and','the','improvement','project'}
        key_overlap = design_words.intersection(funded_words) - common
        
        # If 2+ key words match, count it
        if len(key_overlap) >= 2:
            if funded_name not in matched_names:
                matched_names.append(funded_name)
            break

# Build result
result = json.dumps({
    'count': len(matched_names),
    'projects': [{'name': name, 'amount': funded_projects[name]} for name in matched_names[:5]]
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
