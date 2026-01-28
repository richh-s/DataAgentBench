code = """import json
import re

# Access the stored results
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:5']

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for park-related projects with 2022 completion
    if 'park' in text.lower() and '2022' in text and 'completed' in text.lower():
        # Search for specific patterns
        # Pattern 1: "Bluffs Park Shade Structure" section with completion in 2022
        sections = re.split(r'\n\s*\n', text)
        
        for section in sections:
            section_lower = section.lower()
            if 'park' in section_lower and '2022' in section and 'completed' in section_lower:
                # Extract project name (usually first line of section)
                lines = section.strip().split('\n')
                for line in lines:
                    line = line.strip()
                    if line and len(line) < 100 and 'park' in line.lower():
                        project_name = line.split('Updates:')[0].split('Project Description:')[0].strip()
                        if project_name and not project_name.startswith('('):
                            park_projects_2022.append(project_name)
                        break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Match with funding data
total_funding = 0
for fund in funding_data:
    fund_name = fund.get('Project_Name', '').lower()
    amount = int(fund.get('Amount', 0))
    
    for park_proj in park_projects_2022:
        if park_proj.lower() in fund_name:
            total_funding += amount

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': park_projects_2022,
    'total_funding': total_funding
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
