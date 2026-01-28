code = """import json
import re

# Read the civic documents from the file
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Simple extraction: look for park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find all occurrences of park and 2022
    if 'park' in text and '2022' in text and 'completed' in text:
        # Extract lines containing park and 2022
        lines = text.split('\n')
        for line in lines:
            if 'park' in line and '2022' in line and ('completed' in line or 'completion' in line):
                # Extract simple project name
                proj = line.split('updates:')[0].strip()
                proj = proj.split('\n')[0].strip()
                if proj and 10 < len(proj) < 200:
                    park_projects_2022.append(proj)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Read funding data
with open('var_functions.query_db:5', 'r') as f:
    funding_data = json.load(f)

# Match park projects with funding
total_funding = 0

for fund in funding_data:
    fund_name = fund.get('Project_Name', '').lower()
    for park_proj in park_projects_2022:
        if park_proj.lower() in fund_name:
            total_funding += int(fund.get('Amount', 0))

result = {
    'park_projects_2022': park_projects_2022,
    'total_funding': total_funding,
    'count': len(park_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
