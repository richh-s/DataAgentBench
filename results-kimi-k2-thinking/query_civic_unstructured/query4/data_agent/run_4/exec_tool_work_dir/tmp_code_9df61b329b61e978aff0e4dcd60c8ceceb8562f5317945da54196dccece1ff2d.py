code = """import json

# Load the data from the files
civic_docs = []
with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

funding_records = []
with open(var_functions.query_db:4, 'r') as f:
    funding_records = json.load(f)

# Create funding lookup
funding_lookup = {}
for fund in funding_records:
    proj_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    if proj_name:
        funding_lookup[proj_name] = amount

# Extract project names from civic docs that mention Spring 2022
spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Extract project names
        import re
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 10 and len(line) < 150:
                if 'Project' in line or 'Improvements' in line or 'Repairs' in line or 'Replacement' in line:
                    if not line.startswith('(') and not line.startswith('To:') and not line.startswith('From:'):
                        spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match with funding
matches = []
total_funding = 0
for proj in spring_projects:
    if proj in funding_lookup:
        matches.append({'project': proj, 'funding': funding_lookup[proj]})
        total_funding += funding_lookup[proj]
    else:
        # Try partial matches
        proj_lower = proj.lower()
        for fund_proj, amount in funding_lookup.items():
            if proj_lower in fund_proj.lower() or fund_proj.lower() in proj_lower:
                matches.append({'project': proj, 'matched': fund_proj, 'funding': amount})
                total_funding += amount
                break

# Remove duplicates
unique = {}
for m in matches:
    key = m.get('matched', m['project'])
    unique[key] = m['funding']

final_matches = [{'project': k, 'funding': v} for k, v in unique.items()]
result = {
    'count': len(final_matches),
    'total_funding': total_funding,
    'projects': final_matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
