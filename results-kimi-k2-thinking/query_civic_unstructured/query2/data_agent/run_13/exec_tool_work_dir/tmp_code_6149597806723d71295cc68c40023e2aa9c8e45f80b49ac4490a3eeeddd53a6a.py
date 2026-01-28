code = """import json
import re

# Load data
civic_docs = json.load(open('var_functions.query_db:2'))
funding_data = json.load(open('var_functions.query_db:5'))

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Search for completion notices with 2022
    if 'Construction was completed' in text and '2022' in text:
        # Check if park is mentioned in nearby context
        sections = text.split('Construction was completed')
        for i, section in enumerate(sections[:-1]):
            # Look backwards for project name
            before_section = sections[i]
            
            # Check if this section mentions park
            if 'park' in before_section[-500:].lower():
                # Get last few lines as potential project names
                lines = before_section.split('\n')
                for line in reversed(lines):
                    line = line.strip()
                    if line and len(line) < 100 and not line.startswith('('):
                        park_projects_2022.append(line)
                        break

# Clean results
park_projects_2022 = list(set(park_projects_2022))

# Match with funding
total_funding = 0
matches = []

for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    
    for park_proj in park_projects_2022:
        if park_proj and park_proj.lower() in fund_name.lower():
            total_funding += amount
            matches.append({'project': park_proj, 'fund_name': fund_name, 'amount': amount})

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding, 'projects_found': len(park_projects_2022)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
