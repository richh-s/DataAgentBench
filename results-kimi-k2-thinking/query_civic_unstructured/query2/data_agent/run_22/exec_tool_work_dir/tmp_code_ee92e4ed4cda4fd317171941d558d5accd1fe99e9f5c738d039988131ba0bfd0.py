code = """import json, re

civic_path = var_functions.query_db_6
funding_path = var_functions.query_db_8

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Extract park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all park projects mentioned
    park_pattern = r'[A-Za-z\s]*Park[A-Za-z\s]*(?::|\n|$)'
    park_names = re.findall(park_pattern, text, re.IGNORECASE)
    
    for park_name in park_names:
        park_name = park_name.strip()
        if len(park_name) < 100 and len(park_name) > 5:
            # Check if this park was completed in 2022
            # Look for completion indicators near the park name
            if 'completed' in text.lower() and '2022' in text:
                if park_name not in park_projects:
                    park_projects.append(park_name)

# Match with funding records
funding_amounts = []

for project in park_projects:
    proj_lower = project.lower()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        
        # Check for match
        if proj_lower == fund_name:
            funding_amounts.append(int(fund['Amount']))
        elif fund_name.startswith(proj_lower):
            funding_amounts.append(int(fund['Amount']))

total_funding = sum(funding_amounts)
result = {'total_funding': total_funding, 'num_park_projects': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
