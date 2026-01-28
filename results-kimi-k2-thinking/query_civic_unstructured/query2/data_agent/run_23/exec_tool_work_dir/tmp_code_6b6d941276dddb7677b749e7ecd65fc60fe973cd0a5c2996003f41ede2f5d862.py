code = """import json
import re

# Load civic documents
civic_docs_result = locals()['var_functions.query_db:14']
if isinstance(civic_docs_result, str):
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_result

# Load funding data
funding_result = locals()['var_functions.query_db:38']
if isinstance(funding_result, str):
    with open(funding_result, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_result

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding), 'funding records')

# First, extract all project names from funding that are park-related and have reasonable amounts
park_funding_candidates = []
for fund in funding:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    
    if amount <= 0 or amount > 1000000:
        continue
    
    name_lower = name.lower()
    park_keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume', 'canyon', 'arbors', 'paver']
    
    if any(kw in name_lower for kw in park_keywords):
        park_funding_candidates.append({
            'name': name,
            'amount': amount
        })

print('Found', len(park_funding_candidates), 'park-related funding candidates')

# Now check which of these were completed in 2022 by searching civic docs
park_projects_completed_2022 = []

for candidate in park_funding_candidates:
    project_name = candidate['name']
    
    for doc in civic_docs:
        text = doc.get('text', '')
        if not text:
            continue
        
        # Check if project is mentioned and completed in 2022
        if project_name in text and '2022' in text:
            text_lower = text.lower()
            # Look for completion indicators
            if 'completed' in text_lower or 'completion' in text_lower or 'notice of completion' in text_lower:
                # Check date patterns
                if 'november 2022' in text_lower or '2022' in text:
                    park_projects_completed_2022.append(candidate)
                    break

# Calculate total funding
total_funding = 0
for proj in park_projects_completed_2022:
    total_funding += proj['amount']

print('Park projects completed in 2022:', len(park_projects_completed_2022))
print('Total funding:', total_funding)

result = {
    'total_funding': total_funding,
    'project_count': len(park_projects_completed_2022),
    'projects': park_projects_completed_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
