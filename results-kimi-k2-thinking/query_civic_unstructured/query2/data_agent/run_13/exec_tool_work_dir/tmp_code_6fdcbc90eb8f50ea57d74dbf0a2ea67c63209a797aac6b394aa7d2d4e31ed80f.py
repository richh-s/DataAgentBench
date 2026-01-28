code = """import json
import re

civic_docs = json.load(open('var_functions.query_db:2'))
funding_data = json.load(open('var_functions.query_db:5'))

# Extract park projects completed in 2022
park_projects = []

# Pattern to find park projects with 2022 completion
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for "Construction was completed" patterns
    pattern = r'(\b[A-Z][^.\n]*?\b[Pp]ark\b[^.\n]*?)\n[^\n]*?Construction was completed[^\n]*?2022'
    matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
    
    for match in matches:
        proj_name = match.group(1).strip()
        if proj_name and len(proj_name) < 150:
            park_projects.append(proj_name)

# Remove duplicates
park_projects = list(set(park_projects))

# Match with funding
total_funding = 0
for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    fund_amount = int(fund.get('Amount', 0))
    
    for park_proj in park_projects:
        if park_proj.lower() in fund_name.lower():
            total_funding += fund_amount

print('__RESULT__:')
print(json.dumps({
    'projects': park_projects,
    'total_funding': total_funding,
    'count': len(park_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
