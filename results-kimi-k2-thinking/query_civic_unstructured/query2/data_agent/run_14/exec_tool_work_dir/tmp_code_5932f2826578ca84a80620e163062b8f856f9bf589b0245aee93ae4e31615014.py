code = """import json

# Load funding data from file
funding_file = open('var_functions.query_db:2', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load civic documents from file
docs_file = open('var_functions.query_db:4', 'r')
civic_docs = json.load(docs_file)
docs_file.close()

print('Funding records count:', len(funding_data))
print('Civic documents count:', len(civic_docs))

# Extract park projects completed in 2022
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
            
        # Skip header lines
        skip_words = ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'CITY OF', 'MALIBU CITY']
        if any(skip in line for skip in skip_words):
            continue
            
        # Check if this is a project name (typically uppercase)
        if line.isupper() and len(line) < 200 and '...' not in line:
            # Process previous project if exists
            if current_project:
                proj_text_lower = current_project['text'].lower()
                is_park_project = any(kw in proj_text_lower for kw in park_keywords)
                completed_2022 = ('completed' in proj_text_lower or 'completion' in proj_text_lower) and '2022' in current_project['text']
                
                if is_park_project and completed_2022:
                    park_projects_2022.append(current_project)
            
            # Start new project
            current_project = {'name': line, 'text': ''}
        elif current_project:
            current_project['text'] += line + '\n'
    
    # Process last project in document
    if current_project:
        proj_text_lower = current_project['text'].lower()
        is_park_project = any(kw in proj_text_lower for kw in park_keywords)
        completed_2022 = ('completed' in proj_text_lower or 'completion' in proj_text_lower) and '2022' in current_project['text']
        
        if is_park_project and completed_2022:
            park_projects_2022.append(current_project)

print('\nPark projects completed in 2022 found:', len(park_projects_2022))
for i, p in enumerate(park_projects_2022[:10]):
    print(f"{i+1}. {p['name']}")

# Match with funding data
total_funding = 0
matches = []

# Create funding lookup by lowercase name
funding_lookup = {}
for fund in funding_data:
    key = fund['Project_Name'].lower()
    funding_lookup[key] = fund

for proj in park_projects_2022:
    proj_key = proj['name'].lower()
    
    # Try direct match first
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
    
    # Try partial matching
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

print('\nDirect funding matches:', len(matches))
print('Total funding amount:', total_funding)

for m in matches:
    print(f"- {m['project_name']}: ${m['amount']:,}")

# Also identify all park-related funding records for context
all_park_funding = []
for fund in funding_data:
    name_lower = fund['Project_Name'].lower()
    if any(kw in name_lower for kw in park_keywords):
        all_park_funding.append({
            'name': fund['Project_Name'],
            'amount': int(fund['Amount']),
            'source': fund['Funding_Source']
        })

all_park_total = sum(pf['amount'] for pf in all_park_funding)
print('\nAll park-related funding records:', len(all_park_funding))
print('Total of all park funding:', all_park_total)

result = {
    'park_projects_2022': len(park_projects_2022),
    'funding_matches': len(matches),
    'total_funding': total_funding,
    'all_park_records': len(all_park_funding),
    'all_park_total': all_park_total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
