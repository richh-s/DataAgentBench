code = """import json, re
from pathlib import Path

civic_docs_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:2']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Look for park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find park-related sections
    if 'park' in text.lower() and 'completed' in text.lower() and '2022' in text:
        lines = text.split('\n')
        
        current_project = None
        for line in lines:
            line = line.strip()
            # Simple heuristic for project names
            if (len(line) > 5 and len(line) < 80 and line[0].isupper() and 
                'park' in line.lower() and not line.endswith(':') and 
                not any(x in line for x in ['To:', 'From:', 'Date:', 'Subject:'])):
                
                # Check if this project was completed in 2022
                line_idx = lines.index(line)
                context = ' '.join(lines[line_idx:line_idx+6])
                if 'completed' in context.lower() and '2022' in context:
                    park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))
print('Park projects completed in 2022:', unique_projects)

# Get funding for park projects
total_funding = 0

# First, check for projects we identified
for project in unique_projects:
    proj_lower = project.lower()
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '').lower()
        if proj_lower in fund_name or fund_name in proj_lower:
            total_funding += int(fund.get('Amount', 0))

# Also include any park funding records that mention 2022 or shade structures
for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    fund_lower = fund_name.lower()
    if 'park' in fund_lower and ('2022' in fund_name or 'shade' in fund_lower):
        total_funding += int(fund.get('Amount', 0))

answer = f"Total funding for park-related projects completed in 2022 is ${total_funding:,}"
print('ANSWER:', answer)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.list_db:17': ['Funding']}

exec(code, env_args)
