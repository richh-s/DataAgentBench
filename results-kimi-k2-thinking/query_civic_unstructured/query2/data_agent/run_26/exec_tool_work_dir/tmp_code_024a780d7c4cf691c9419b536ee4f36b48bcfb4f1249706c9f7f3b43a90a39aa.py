code = """import json

# Load data
civic_docs = json.load(open('var_functions.query_db:20', 'r'))
funding_data = json.load(open('var_functions.query_db:5', 'r'))

print('Documents:', len(civic_docs))
print('Funding records:', len(funding_data))

# Build funding map
funding_map = {}
for record in funding_data:
    funding_map[record['Project_Name']] = int(record['Amount'])

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headings
        if any(x in line.lower() for x in ['capital improvement', 'prepared by', 'approved by', 'agenda', 'page']):
            continue
        
        # Check if park-related
        if 'park' in line.lower() or 'playground' in line.lower():
            # Look for completion in 2022 nearby
            context_start = max(0, i-10)
            context_end = min(len(lines), i+10)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'completed' in context and '2022' in context:
                clean_name = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                park_projects.append(clean_name)

# Remove duplicates
unique_projects = list(set(park_projects))
print('\nPark projects completed in 2022:', len(unique_projects))
for p in unique_projects:
    print('- ' + p)

# Match with funding
matched = []
total = 0

for proj in unique_projects:
    best_match = None
    max_common = 0
    
    proj_words = set(proj.lower().replace('(', '').replace(')', '').split())
    
    for funded in funding_map:
        funded_words = set(funded.lower().replace('(', '').replace(')', '').split())
        common = len(proj_words.intersection(funded_words))
        
        if common > max_common and common >= 2:
            max_common = common
            best_match = funded
    
    if best_match:
        amount = funding_map[best_match]
        matched.append((proj, best_match, amount))
        total += amount

print('\nMatched projects with funding:')
for proj, funded, amount in matched:
    print('- %s: $%d' % (proj, amount))

print('\nTotal funding: $%d' % total)

# Return result
result = {'total_funding': total, 'project_count': len(matched)}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
