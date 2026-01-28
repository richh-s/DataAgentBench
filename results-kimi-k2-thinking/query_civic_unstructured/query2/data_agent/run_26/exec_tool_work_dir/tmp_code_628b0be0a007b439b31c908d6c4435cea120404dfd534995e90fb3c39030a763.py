code = """import json

# Load data
civic_docs = json.load(open('var_functions.query_db:20', 'r'))
funding_data = json.load(open('var_functions.query_db:5', 'r'))

# Build funding map
funding_map = {}
for r in funding_data:
    funding_map[r['Project_Name']] = int(r['Amount'])

# Find park projects completed in 2022
found_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 10:
            continue
        
        # Skip headings
        if line.lower().find('capital improvement') >= 0 or line.lower().find('prepared by') >= 0:
            continue
        
        # Check for park and 2022 completion
        if line.lower().find('park') >= 0 or line.lower().find('playground') >= 0:
            # Check context for completion in 2022
            context = ' '.join(lines[max(0,i-10):min(len(lines),i+10)]).lower()
            if context.find('completed') >= 0 and context.find('2022') >= 0:
                clean = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                found_projects.append(clean)

# Remove duplicates
unique = list(set(found_projects))

# Match with funding
total = 0
count = 0

for proj in unique:
    # Try to find exact match first
    if proj in funding_map:
        total += funding_map[proj]
        count += 1
        print(proj + ': $' + str(funding_map[proj]))
        continue
    
    # Try partial matching
    for funded in funding_map:
        if proj.lower().find(funded.lower()) >= 0 or funded.lower().find(proj.lower()) >= 0:
            total += funding_map[funded]
            count += 1
            print(proj + ' -> ' + funded + ': $' + str(funding_map[funded]))
            break

print('\nTotal: $' + str(total))
print('Count: ' + str(count))

# Return result
result = {'total_funding': total, 'project_count': count}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
