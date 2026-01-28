code = """import json
f = open('var_functions.query_db:2', 'r')
funding_data = json.load(f)
f.close()

d = open('var_functions.query_db:4', 'r')
civic_docs = json.load(d)
d.close()

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

park_projects_2022 = []
park_keywords = ['park', 'playground', 'bluffs', 'landon', 'arbors', 'benches', 'walkway', 'skate park']

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        skip_words = ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'CITY OF', 'MALIBU CITY']
        if any(skip in line for skip in skip_words):
            continue
            
        if line.isupper() and len(line) < 200 and '...' not in line:
            if current_project:
                text_lower = current_project['text'].lower()
                is_park = any(kw in text_lower for kw in park_keywords)
                completed_2022 = ('completed' in text_lower or 'completion' in text_lower) and '2022' in current_project['text']
                if is_park and completed_2022:
                    park_projects_2022.append(current_project)
            
            current_project = {'name': line, 'text': ''}
        elif current_project:
            current_project['text'] += line + '\n'
    
    if current_project:
        text_lower = current_project['text'].lower()
        is_park = any(kw in text_lower for kw in park_keywords)
        completed_2022 = ('completed' in text_lower or 'completion' in text_lower) and '2022' in current_project['text']
        if is_park and completed_2022:
            park_projects_2022.append(current_project)

print('\nPark projects completed in 2022:', len(park_projects_2022))
for idx, p in enumerate(park_projects_2022[:10]):
    print(str(idx+1) + '. ' + p['name'])

funding_lookup = {}
for fund in funding_data:
    funding_lookup[fund['Project_Name'].lower()] = fund

total_funding = 0
matches = []

for proj in park_projects_2022:
    proj_key = proj['name'].lower()
    
    if proj_key in funding_lookup:
        fund = funding_lookup[proj_key]
        amount = int(fund['Amount'])
        total_funding += amount
        matches.append({
            'project_name': proj['name'],
            'funding_name': fund['Project_Name'],
            'amount': amount,
            'source': fund['Funding_Source']
        })
        continue
    
    for fund_key, fund in funding_lookup.items():
        if proj_key in fund_key or fund_key in proj_key:
            amount = int(fund['Amount'])
            total_funding += amount
            matches.append({
                'project_name': proj['name'],
                'funding_name': fund['Project_Name'],
                'amount': amount,
                'source': fund['Funding_Source']
            })
            break

print('\nMatching funding records:', len(matches))
print('Total funding amount:', total_funding)

for m in matches:
    print('- ' + m['project_name'] + ': $' + str(m['amount']))

all_park_funding = []
for fund in funding_data:
    name_lower = fund['Project_Name'].lower()
    if any(kw in name_lower for kw in park_keywords):
        all_park_funding.append({
            'name': fund['Project_Name'],
            'amount': int(fund['Amount'])
        })

all_park_total = sum(pf['amount'] for pf in all_park_funding)
print('\nAll park funding records count:', len(all_park_funding))
print('Total all park funding:', all_park_total)

result = {
    'park_projects_2022': len(park_projects_2022),
    'direct_funding_matches': len(matches),
    'total_funding_matched': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
