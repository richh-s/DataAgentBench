code = """import json

# Load data from files
civic_docs_path = 'var_functions.query_db:20'
funding_path = 'var_functions.query_db:5'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding map
funding_map = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_map[name] = amount

print('Documents loaded:', len(civic_docs))
print('Funding records loaded:', len(funding_data))

# Find park-related projects completed in 2022 in civic documents
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 10:
            continue
        
        # Check for park-related projects
        lower_line = line.lower()
        if lower_line.find('park') >= 0 or lower_line.find('playground') >= 0:
            # Skip headings
            if lower_line.find('capital improvement') >= 0 or lower_line.find('prepared by') >= 0:
                continue
            
            # Check if completed in 2022
            start = max(0, i-10)
            end = min(len(lines), i+10)
            context = ' '.join(lines[start:end]).lower()
            
            if context.find('completed') >= 0 and context.find('2022') >= 0:
                clean = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                park_projects.append(clean)

# Remove duplicates
unique_projects = list(set(park_projects))
print('Found park projects completed in 2022:', len(unique_projects))
for proj in unique_projects:
    print('- ' + proj)

# Find funding for these projects
total_funding = 0
project_count = 0

for proj in unique_projects:
    # Direct match
    if proj in funding_map:
        total_funding += funding_map[proj]
        project_count += 1
        print('Found funding: ' + proj + ' = $' + str(funding_map[proj]))
        continue
    
    # Fuzzy match
    proj_lower = proj.lower()
    for funded_name in funding_map:
        if proj_lower in funded_name.lower() or funded_name.lower() in proj_lower:
            total_funding += funding_map[funded_name]
            project_count += 1
            print('Matched: ' + proj + ' -> ' + funded_name + ' = $' + str(funding_map[funded_name]))
            break

print('Total funding: $' + str(total_funding))
print('Projects with funding: ' + str(project_count))

# Create result
result = str(total_funding)
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
