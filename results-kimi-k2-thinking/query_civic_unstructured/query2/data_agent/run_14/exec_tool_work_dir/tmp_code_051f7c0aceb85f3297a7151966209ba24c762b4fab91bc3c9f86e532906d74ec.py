code = """import json
import os

# Load data from file paths
funding_path = 'var_functions.query_db:2'
civic_path = 'var_functions.query_db:4'

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded funding records:', len(funding_data))
print('Loaded civic documents:', len(civic_docs))

# Extract park projects completed in 2022
park_projects_2022 = []
park_keywords = ['park', 'playground', 'bluffs', 'landon', 'arbors', 'benches', 'walkway', 'skate park', 'shade structure']

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headers
        skip_words = ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'CITY OF', 'MALIBU CITY', 'CHAIR', 'MEMBERS']
        if any(skip in line for skip in skip_words):
            continue
            
        # Check if this is a project name (all caps, reasonable length)
        if line.isupper() and len(line) < 200:
            # Look ahead in the following lines for status and date
            next_lines = '\n'.join(lines[i+1:i+20])
            full_text = line + '\n' + next_lines
            text_lower = full_text.lower()
            
            # Check if park-related and completed in 2022
            is_park = any(kw in text_lower for kw in park_keywords)
            completed_2022 = ('completed' in text_lower and '2022' in full_text) or ('construction was completed' in text_lower and '2022' in full_text)
            
            if is_park and completed_2022:
                park_projects_2022.append({
                    'name': line,
                    'context': full_text
                })

print('\nPark projects completed in 2022 found:', len(park_projects_2022))
for p in park_projects_2022:
    print('- ' + p['name'])

# Create funding lookup by project name
funding_lookup = {}
for fund in funding_data:
    funding_lookup[fund['Project_Name'].lower()] = fund

# Match projects with funding
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    proj_name_lower = proj['name'].lower()
    
    # Direct match
    if proj_name_lower in funding_lookup:
        fund = funding_lookup[proj_name_lower]
        amount = int(fund['Amount'])
        total_funding += amount
        matched_projects.append({
            'project_name': proj['name'],
            'funding_name': fund['Project_Name'],
            'amount': amount,
            'source': fund['Funding_Source']
        })
    else:
        # Fuzzy match - check if any funded project contains this name
        for fund_name_lower, fund in funding_lookup.items():
            if proj_name_lower in fund_name_lower or fund_name_lower in proj_name_lower:
                amount = int(fund['Amount'])
                total_funding += amount
                matched_projects.append({
                    'project_name': proj['name'],
                    'funding_name': fund['Project_Name'],
                    'amount': amount,
                    'source': fund['Funding_Source']
                })
                break

print('\nMatched with funding:', len(matched_projects))
print('Total funding amount: $' + str(total_funding))

for m in matched_projects:
    print(f"- {m['project_name']}: ${m['amount']:,} ({m['source']})")

# Also check all park-related funding records
all_park_funding = []
for fund in funding_data:
    name_lower = fund['Project_Name'].lower()
    if any(kw in name_lower for kw in park_keywords):
        all_park_funding.append(int(fund['Amount']))

all_park_total = sum(all_park_funding)
print('\nAll park-related funding records:', len(all_park_funding))
print('Total of ALL park funding (not filtered by year): $' + str(all_park_total))

# Final result
result = {
    'park_projects_2022': len(park_projects_2022),
    'funding_matches': len(matched_projects),
    'total_funding_amount': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
