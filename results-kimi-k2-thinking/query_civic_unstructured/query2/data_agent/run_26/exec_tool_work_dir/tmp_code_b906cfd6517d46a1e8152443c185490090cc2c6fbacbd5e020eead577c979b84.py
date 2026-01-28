code = """import json

# Load data from files
civic_docs_file = 'var_functions.query_db:20'
funding_file = 'var_functions.query_db:5'

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Loaded %d civic documents' % len(civic_docs))
print('Loaded %d funding records' % len(funding_records))

# Build funding map
funding_dict = {}
for rec in funding_records:
    funding_dict[rec['Project_Name']] = int(rec['Amount'])

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10:
            continue
        
        # Check if park-related (avoid headings)
        lower = line.lower()
        if lower.find('park') >= 0 and lower.find('capital improvement') < 0:
            # Check context for completion in 2022
            context_start = max(0, i-8)
            context_end = min(len(lines), i+8)
            context_parts = []
            for j in range(context_start, context_end):
                context_parts.append(lines[j])
            context = ' '.join(context_parts).lower()
            
            if context.find('completed') >= 0 and context.find('2022') >= 0:
                clean_name = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                park_projects.append(clean_name)

# Remove duplicates
unique_projects = list(set(park_projects))
print('\nFound %d park projects completed in 2022' % len(unique_projects))
for proj in unique_projects:
    print('- ' + proj)

# Match with funding
total_funding = 0
count = 0

for project_name in unique_projects:
    # Try direct match
    if project_name in funding_dict:
        amount = funding_dict[project_name]
        total_funding += amount
        count += 1
        print('Direct match: ' + project_name + ' = $' + str(amount))
        continue
    
    # Try partial match
    proj_lower = project_name.lower()
    for funded_name in funding_dict:
        if proj_lower in funded_name.lower():
            amount = funding_dict[funded_name]
            total_funding += amount
            count += 1
            print('Partial match: ' + project_name + ' -> ' + funded_name + ' = $' + str(amount))
            break

print('\nTotal funding: $%d' % total_funding)
print('Projects with funding: %d' % count)

# Prepare result
result = str(total_funding)
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
