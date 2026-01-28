code = """import json
import re

# Debug: Check what we have
civic_docs = locals()['var_functions.query_db:2']
funding_records = locals()['var_functions.query_db:5']

# Build funding lookup
funding_lookup = {}
for record in funding_records:
    project_name = record.get('Project_Name', '').lower()
    amount = record.get('Amount', 0)
    if isinstance(amount, str):
        amount = int(amount) if amount.isdigit() else 0
    else:
        amount = int(amount) if amount else 0
    if project_name and amount > 0:
        funding_lookup[project_name] = amount

# Simple extraction of disaster projects with 2022
disaster_projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for lines with disaster indicators and 2022 dates
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        lower_line = line.lower()
        if any(marker in lower_line for marker in ['fema', 'caljpia', 'caloes']):
            # Check for 2022 date in next few lines
            if '2022' in text:
                disaster_projects_2022.append(line)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

# Find matching funding
matched_projects = []
total_funding = 0

for proj_name in disaster_projects_2022:
    proj_lower = proj_name.lower()
    if proj_lower in funding_lookup:
        amount = funding_lookup[proj_lower]
        total_funding += amount
        matched_projects.append({"project": proj_name, "amount": amount})
    else:
        # Try to find best match
        best_match = None
        best_ratio = 0
        for funding_name in funding_lookup:
            if proj_lower in funding_name or funding_name in proj_lower:
                amount = funding_lookup[funding_name]
                total_funding += amount
                matched_projects.append({"project": proj_name, "funding_match": funding_name, "amount": amount})
                break

result = {
    "total_funding": total_funding,
    "matched_projects": matched_projects,
    "disaster_projects_found": len(disaster_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
