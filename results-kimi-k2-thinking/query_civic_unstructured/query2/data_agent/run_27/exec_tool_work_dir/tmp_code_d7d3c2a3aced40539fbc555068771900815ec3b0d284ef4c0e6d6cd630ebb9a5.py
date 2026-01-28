code = """import json, re

# Load data from files
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

# Find completed park projects in 2022
park_completions_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        # Check if line mentions completion in 2022
        if '2022' in line and ('completed' in line_lower or 'completion' in line_lower):
            # Look backwards for project name
            proj_name = None
            for j in range(i-1, max(0, i-6), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and len(prev_line) > 5:
                    # Clean up the line
                    proj_name = prev_line.replace('•', '').replace('◦', '').strip()
                    break
            
            if proj_name and 'park' in proj_name.lower():
                park_completions_2022.append(proj_name)

# Remove duplicates
park_completions_2022 = list(set(park_completions_2022))

print('Found park projects completed in 2022:', len(park_completions_2022))

# Match with funding data and calculate total
total_funding = 0
matched_projects = []

for park_name in park_completions_2022:
    for fund in funding_data:
        fund_name = fund['Project_Name']
        # Check if names match (simplified matching)
        park_key = park_name.lower().replace(' ', '').replace('-', '')
        fund_key = fund_name.lower().replace(' ', '').replace('-', '')
        
        if park_key in fund_key or fund_key in park_key:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'project': park_name,
                'funding_name': fund_name,
                'amount': amount
            })
            break

# Output final result
result = {
    'total_funding_dollars': total_funding,
    'project_count': len(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
