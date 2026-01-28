code = """import json
import re

# Read funding data
with open('var_functions.query_db:2', 'r') as f:
    funding_data_str = f.read()
funding_data = json.loads(funding_data_str)

# Read civic documents
with open('var_functions.query_db:4', 'r') as f:
    civic_docs_str = f.read()
civic_docs = json.loads(civic_docs_str)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Process civic documents to extract projects
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headers
        if any(skip in line for skip in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'CITY OF']):
            continue
            
        # Check if this is a project name (uppercase and not too long)
        if line.isupper() and len(line) < 150:
            # Save previous project
            if current_project:
                # Check if it's park-related and completed in 2022
                if current_project['is_park'] and current_project['completed_2022']:
                    park_projects_2022.append(current_project)
            
            # Start new project
            current_project = {
                'name': line,
                'text': '',
                'is_park': False,
                'completed_2022': False,
                'amount': 0
            }
        elif current_project:
   current_project['text'] += line + '\n'
    
    # Don't forget the last project
  if current_project and current_project['is_park'] and current_project['completed_2022']:
        park_projects_2022.append(current_project)

# Now analyze each project
for proj in park_projects_2022:
    text = proj['text'].lower()
    
    # Check if park-related
    if any(kw in text for kw in ['park', 'playground', 'bluffs', 'landon', 'arbors', 'benches', 'walkway']):
  proj['is_park'] = True
    
    # Check if completed in 2022
    if ('completed' in text or 'completion' in text or 'construction was completed' in text) and '2022' in proj['text']:
        proj['completed_2022'] = True

# Filter only true park projects completed in 2022
park_projects_2022 = [p for p in park_projects_2022 if p['is_park'] and p['completed_2022']]

print('\nPark projects completed in 2022:', len(park_projects_2022))
for p in park_projects_2022:
    print('-', p['name'])

# Match with funding
total_funding = 0
matches = []

# Create index of funding by lowercase name
funding_index = {}
for fund in funding_data:
    funding_index[fund['Project_Name'].lower()] = fund

for proj in park_projects_2022:
    proj_name_lower = proj['name'].lower()
    
    # Direct match
    if proj_name_lower in funding_index:
       fund = funding_index[proj_name_lower]
        amount = int(fund['Amount'])
        total_funding += amount
        matches.append({
      'project': proj['name'],
            'funding_record': fund['Project_Name'],
  'amount': amount,
            'source': fund['Funding_Source']
        })
        continue
    
    # Partial match - check if project name exists in any funding record
    for fund_name_lower, fund in funding_index.items():
   if proj_name_lower in fund_name_lower or fund_name_lower in proj_name_lower:
            amount = int(fund['Amount'])
      total_funding += amount
   matches.append({
         'project': proj['name'],
  'funding_record': fund['Project_Name'],
       'amount': amount,
    'source': fund['Funding_Source']
          })
            break

print('\nFunding matches found:', len(matches))
print('Total funding:', total_funding)

for m in matches:
    print(f"- {m['project']}: ${m['amount']:,} ({m['source']})")

# Also check for park-related projects in funding that mention 2022
additional_park_funding = []
park_keywords = ['park', 'bluffs', 'playground', 'landon', 'arbors', 'benches', 'walkway', 'shade structure']

for fund in funding_data:
   proj_name = fund['Project_Name'].lower()
    if any(kw in proj_name for kw in park_keywords):
        project_info = {
  'name': fund['Project_Name'],
' amount': int(fund['Amount']),
         'source': fund['Funding_Source']
        }
        additional_park_funding.append(project_info)

additional_total = sum(p['amount'] for p in additional_park_funding)
print('\nAll park-related funding records:', len(additional_park_funding))
print('Total all park funding (not filtered by year):', additional_total)

# Return results
result = {
    'park_projects_2022_count': len(park_projects_2022),
    'direct_funding_matches': len(matches),
   'total_funding_for_matches': total_funding,
    'all_park_funding_records': len(additional_park_funding),
    'total_all_park_funding': additional_total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
