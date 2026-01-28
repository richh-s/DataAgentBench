code = """import json
import re

# Load the data
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:7']

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Build funding lookup
fund_lookup = {}
for item in funding:
    name = item.get('Project_Name', '')
    amount = int(item.get('Amount', 0))
    fund_lookup[name] = fund_lookup.get(name, 0) + amount

# Find disaster projects with 2022 start dates
disaster_projs = []
for doc in civic_docs:
    text = doc.get('text', '')
    if any(keyword in text.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY', 'RECOVERY']):
        # Look for project sections
        lines = text.split('\n')
        curr_proj = None
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or line.startswith('(') or 'page' in line.lower():
                continue
                
            # Find project headers
            if i < len(lines)-1 and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                curr_proj = line
                
                # Check following lines for 2022 dates and disaster indicators
                is_disaster = False
                has_2022 = False
                
                for j in range(i+1, min(i+15, len(lines))):
                    check_line = lines[j].upper()
                    if any(k in check_line for k in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY', 'RECOVERY']):
                        is_disaster = True
                    if '2022' in check_line and any(s in check_line for s in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE']):
                        has_2022 = True
                
                if is_disaster and has_2022 and curr_proj:
                    disaster_projs.append(curr_proj)

# Calculate total funding
total_funding = 0
for proj_name in disaster_projs:
    for fund_name, amount in fund_lookup.items():
        # Match projects by name similarity
        if proj_name in fund_name or fund_name in proj_name:
            total_funding += amount
            break
        # Try partial match
        proj_parts = [p for p in proj_name.split() if len(p) > 7]
        for part in proj_parts:
            if part in fund_name:
                total_funding += amount
                break

result = {
    'total_funding': total_funding,
    'disaster_projects_count': len(disaster_projs),
    'sample_projects': disaster_projs[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
