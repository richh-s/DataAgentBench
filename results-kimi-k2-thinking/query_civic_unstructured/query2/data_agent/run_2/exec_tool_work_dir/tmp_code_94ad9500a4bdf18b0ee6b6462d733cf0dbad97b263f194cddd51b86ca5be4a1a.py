code = """import json, re

# Open data files
civic_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:2']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

print('Data loaded:', len(civic_docs), 'docs,', len(funding), 'funding records')

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    if 'completed' in lower_text and '2022' in text and 'park' in lower_text:
        lines = text.split('\n')
        for line in lines:
            line_stripped = line.strip()
            if line_stripped and len(line_stripped) < 80:
                first_char = line_stripped[0] if line_stripped else ''
                if first_char.isupper() and 'park' in line_stripped.lower():
                    park_projects.append(line_stripped)

# Remove duplicates
unique_parks = list(set(park_projects))

# Get funding amounts
total = 0
matched = set()

for project in unique_parks:
    proj_lower = project.lower()
    for fund in funding:
        fund_name = fund.get('Project_Name', '')
        if fund_name not in matched:
            fund_lower = fund_name.lower()
            amount = int(fund.get('Amount', 0))
            
            if 'park' in fund_lower:
                if proj_lower in fund_lower or fund_lower in proj_lower:
                    total += amount
                    matched.add(fund_name)
                elif any(word in fund_lower for word in ['shade', 'structure', 'bluff']):
                    if '2022' in fund_name or 'Malibu' in fund_name:
                        total += amount
                        matched.add(fund_name)

print('Total funding:', total)
print('Records matched:', len(matched))
final_answer = 'Total funding for park-related projects completed in 2022 is $' + str(total)
print('__RESULT__:' + final_answer)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.list_db:17': ['Funding']}

exec(code, env_args)
