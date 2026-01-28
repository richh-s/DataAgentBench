code = """import json
import re

# Get the file paths from storage
civic_docs_file = locals()['var_functions.query_db:14']
funding_file = locals()['var_functions.query_db:2']

# Load data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Find park projects completed in 2022
park_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for completion with 2022 in text
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 10 and not line.startswith('(') and not line.startswith('•'):
                if 'Project' in line or 'Improvements' in line:
                    if 'park' in line.lower():
                        # Check nearby lines for 2022 completion
                        for j in range(i+1, min(i+15, len(lines))):
                            next_line = lines[j]
                            if '2022' in next_line and ('completed' in next_line.lower() or 'completion' in next_line.lower()):
                                park_projects.add(line)
                                break

# Create funding lookup
funding_dict = {}
for fund in funding_data:
    fund_name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    funding_dict[fund_name] = amount

# Match projects with funding
total_funding = 0
matched = 0

for project_name in park_projects:
    # Direct match
    if project_name in funding_dict:
        total_funding += funding_dict[project_name]
        matched += 1
    else:
        # Partial match
        proj_lower = project_name.lower()
        for fund_name, amount in funding_dict.items():
            fund_lower = fund_name.lower()
            if proj_lower in fund_lower or fund_lower in proj_lower:
                total_funding += amount
                matched += 1
                break

result_json = json.dumps({'total_funding': total_funding, 'matched': matched, 'projects_found': len(park_projects)})

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
