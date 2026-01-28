code = """import json

# Read the files from the paths stored in variables
civic_docs_file = 'var_functions.query_db:20'
funding_file = 'var_functions.query_db:5'

# Load civic documents
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding records  
with open(funding_file, 'r') as f:
    funding_recs = json.load(f)

print('Loaded %d civic documents' % len(civic_docs))
print('Loaded %d funding records' % len(funding_recs))

# Build funding map
funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10:
            continue
        
        # Check if park-related
        lower = line.lower()
        if lower.find('park') >= 0 or lower.find('playground') >= 0:
            # Skip headings
            if lower.find('capital improvement') >= 0 or lower.find('prepared by') >= 0:
                continue
            
            # Look for completion in 2022 in context
            context_start = max(0, i-8)
            context_end = min(len(lines), i+10)
            context = []
            for j in range(context_start, context_end):
                context.append(lines[j])
            context_text = ' '.join(context).lower()
            
            if context_text.find('completed') >= 0 and context_text.find('2022') >= 0:
                clean_name = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                park_projects.append(clean_name)

# Remove duplicates
unique_projects = list(set(park_projects))
print('\nFound %d park projects completed in 2022:' % len(unique_projects))
for p in unique_projects:
    print('- ' + p)

# Match with funding and calculate total
total_funding = 0
for proj in unique_projects:
    if proj in funding_map:
        total_funding += funding_map[proj]
    else:
        # Try partial matching
        proj_lower = proj.lower()
        for funded_name in funding_map:
            funded_lower = funded_name.lower()
            if proj_lower in funded_lower or funded_lower in proj_lower:
                total_funding += funding_map[funded_name]
                break

print('\nTotal funding: $%d' % total_funding)

# Return result
result_value = '$%d' % total_funding
print('\n__RESULT__:')
print(json.dumps(result_value))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
