code = """import json
import re

# Load data from storage
civic_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding = json.load(f)

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for park-related projects with completion in 2022
    if 'park' in text.lower() and '2022' in text:
        # Check if it mentions completion
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if 'park' in line_lower and 'completed' in line_lower and '2022' in line_lower:
                project_name = line.strip()
                # Get previous line if this seems like a status update
                if i > 0 and lines[i-1].strip().isupper():
                    project_name = lines[i-1].strip()
                park_projects_2022.append(project_name)

# Remove duplicates and clean
park_projects_2022 = list(set([p for p in park_projects_2022 if len(p) > 5]))

# Find funding for these projects
total_funding = 0
funding_matches = []

for project in park_projects_2022:
    project_key = project.split()[0].lower()
    for fund in funding:
        fund_name = fund['Project_Name'].lower()
        if 'park' in fund_name and project_key in fund_name:
            amount = int(fund['Amount'])
            total_funding += amount
            funding_matches.append({
                'project': project,
                'funding_record': fund['Project_Name'],
                'amount': amount
            })

result = {
    'total_funding': total_funding,
    'projects_found': len(park_projects_2022),
    'matches': len(funding_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
