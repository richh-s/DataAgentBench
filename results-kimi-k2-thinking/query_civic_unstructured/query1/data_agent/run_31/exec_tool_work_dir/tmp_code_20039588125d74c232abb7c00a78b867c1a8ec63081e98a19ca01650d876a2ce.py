code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:2
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic docs
civic_file = var_functions.query_db:5
with open(civic_file) as f:
    civic_docs = json.load(f)

# Find project names in civic docs
project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    if isinstance(text, str):
        # Look for capital projects in design phase
        if 'Capital Improvement Projects' in text or ('capital' in text.lower() and 'design' in text.lower()):
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                # Check if line looks like a project name (not metadata/status text)
                if 10 < len(line) < 80:
                    line_lower = line.lower()
                    # Skip metadata
                    if 'update' not in line_lower and 'schedule' not in line_lower:
                        # Look for infrastructure keywords
                        if 'road' in line_lower or 'avenue' in line_lower or 'drive' in line_lower or 'canyon' in line_lower or 'park' in line_lower or 'storm' in line_lower or 'bridge' in line_lower:
                            project_names.append(line)

# Remove duplicates
unique_projects = list(set(project_names))

# Get funding projects over $50k
funding_over_50k = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_over_50k[item['Project_Name']] = amount

# Count matches
match_count = 0
for project in unique_projects:
    proj_clean = project.lower()
    proj_clean = proj_clean.replace('(', '').replace(')', '')
    proj_clean = ''.join(c if c.isalnum() or c == ' ' else ' ' for c in proj_clean)
    proj_clean = ' '.join(proj_clean.split())
    
    for fund_name in funding_over_50k.keys():
        fund_clean = fund_name.lower()
        fund_clean = fund_clean.replace('(', '').replace(')', '')
        fund_clean = ''.join(c if c.isalnum() or c == ' ' else ' ' for c in fund_clean)
        fund_clean = ' '.join(fund_clean.split())
        
        if proj_clean in fund_clean or fund_clean in proj_clean:
            match_count += 1
            break

print('__RESULT__:')
print(json.dumps({'count': match_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
