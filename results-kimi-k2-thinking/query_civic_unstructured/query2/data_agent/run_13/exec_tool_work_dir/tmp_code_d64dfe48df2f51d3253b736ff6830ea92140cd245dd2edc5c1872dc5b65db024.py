code = """import json
import re

# Load civic documents
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open('var_functions.query_db:5', 'r') as f:
    funding_data = json.load(f)

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern 1: Look for "Construction was completed [Month] 2022" and capture the project name before it
    completed_pattern = r'Construction was completed[^\n]*2022[^\n]*'
    matches = re.finditer(completed_pattern, text, re.IGNORECASE)
    
    for match in matches:
        # Get the context before this completion notice
        completion_pos = match.start()
        before_text = text[:completion_pos]
        
        # Look for project name (usually a short line before the completion notice)
        lines = before_text.split('\n')
        for i in range(len(lines)-1, -1, -1):
            line = lines[i].strip()
            if line and not line.startswith('(') and len(line) < 150:
                # Check if it's park-related
                if 'park' in line.lower():
                    park_projects_2022.append(line)
                    break
                # Also check if it's a park project but "park" might only be in subsequent text
                # Break after finding a reasonable project name candidate
                break

# Remove duplicates while preserving order
seen = set()
unique_park_projects = []
for proj in park_projects_2022:
    if proj not in seen:
        seen.add(proj)
        unique_park_projects.append(proj)

# Match with funding data and sum amounts
total_funding = 0
matched_funding = []

for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    fund_amount = int(fund.get('Amount', 0))
    
    # Check if any of our park projects match this funding record
    for park_proj in unique_park_projects:
        # Direct match or close match
        if (park_proj.lower() in fund_name.lower() or 
            fund_name.lower() in park_proj.lower()):
            total_funding += fund_amount
            matched_funding.append({
                'project': park_proj,
                'fund_name': fund_name,
                'amount': fund_amount
            })
            # Don't break - a project might have multiple funding records

# Also try to find additional park projects by scanning for "Park" headings with 2022 completion
print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': unique_park_projects,
    'total_funding': total_funding,
    'funding_matches': matched_funding,
    'project_count': len(unique_park_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
