code = """import json
import re

# Load data from files
funding_path = var_functions.query_db_2
civic_path = var_functions.query_db_5

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Map projects with funding > $50,000
funding_map = {}
for rec in funding_records:
    amount = int(rec.get('Amount', 0))
    if amount > 50000:
        project_name = rec.get('Project_Name', '')
        funding_map[project_name.lower()] = {
            'original_name': project_name,
            'amount': amount,
            'source': rec.get('Funding_Source')
        }

# Step 2: Simple pattern matching in civic documents
matched = []
total_text_to_search = ''

for doc in civic_docs:
    total_text_to_search += ' ' + doc.get('text', '')

text_lower = total_text_to_search.lower()

# Look for capital projects that are in design phase
for funded_name_lower in funding_map:
    funded_info = funding_map[funded_name_lower]
    original_name = funded_info['original_name']
    
    # First check if project name appears in text
    if original_name.lower() in text_lower:
        # Find the section where this project appears
        idx = text_lower.find(original_name.lower())
        surrounding_text = text_lower[max(0, idx-200):idx+400]
        
        # Check for design and capital indicators near the project name
        has_design = 'design' in surrounding_text or 'design' in text_lower
        has_capital = 'capital' in surrounding_text
        
        if has_design and has_capital:
            matched.append({
                'name': original_name,
                'funding': funded_info['amount']
            })

# Remove duplicates
unique_matched = []
seen = set()
for item in matched:
    if item['name'] not in seen:
        seen.add(item['name'])
        unique_matched.append(item)

print('Found', len(unique_matched), 'matching projects')
print('__RESULT__:')
print(json.dumps({'count': len(unique_matched), 'projects': unique_matched[:5]}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
