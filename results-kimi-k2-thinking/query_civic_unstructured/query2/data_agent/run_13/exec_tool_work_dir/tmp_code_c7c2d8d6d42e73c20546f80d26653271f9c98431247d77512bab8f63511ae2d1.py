code = """import json

# Load the data files
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

with open('var_functions.query_db:5', 'r') as f:
    funding_data = json.load(f)

# Find park projects completed in 2022 by simple text search
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        # Look for lines mentioning park and completion in 2022
        if 'park' in line_lower and '2022' in line_lower and ('completed' in line_lower or 'completion' in line_lower):
            # Get project name (usually the line before or same line)
            if i > 0:
                prev_line = lines[i-1].strip()
                if prev_line and len(prev_line) < 100 and not prev_line.startswith('('):
                    park_projects_2022.append(prev_line)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Match with funding data
total_funding = 0
for fund in funding_data:
    fund_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    for park_proj in park_projects_2022:
        if park_proj.lower() in fund_name:
            total_funding += fund_amount

print('__RESULT__:')
print(json.dumps({'park_projects_2022': park_projects_2022, 'total_funding': total_funding}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
