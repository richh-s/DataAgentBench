code = """import json

# Access the stored results directly as variables
civic_docs = locals()['var_functions.query_db:20']
funding_records = locals()['var_functions.query_db:5']

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Build funding map
funding_map = {}
for rec in funding_records:
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
        lower_line = line.lower()
        if lower_line.find('park') >= 0 or lower_line.find('playground') >= 0:
            # Skip headings
            if lower_line.find('capital improvement') >= 0 or lower_line.find('prepared by') >= 0:
                continue
            
            # Look for completion in 2022 in context
            start = max(0, i-8)
            end = min(len(lines), i+8)
            context = []
            for j in range(start, end):
                context.append(lines[j])
            context_text = ' '.join(context).lower()
            
            if 'completed' in context_text and '2022' in context_text:
                clean_name = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                park_projects.append(clean_name)

# Remove duplicates
unique_projects = list(set(park_projects))
print('\nFound projects:', len(unique_projects))
for p in unique_projects:
    print(p)

# Match with funding
total = 0
count = 0

for proj in unique_projects:
    if proj in funding_map:
        total += funding_map[proj]
        count += 1
        print('Funding: ' + proj + ' = $' + str(funding_map[proj]))
    else:
        # Try partial match
        proj_lower = proj.lower()
        for funded in funding_map:
            if proj_lower in funded.lower():
                total += funding_map[funded]
                count += 1
                print('Matched: ' + proj + ' -> ' + funded + ' = $' + str(funding_map[funded]))
                break

print('\nTotal: $' + str(total))
print('Count: ' + str(count))

result = str(total)
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
