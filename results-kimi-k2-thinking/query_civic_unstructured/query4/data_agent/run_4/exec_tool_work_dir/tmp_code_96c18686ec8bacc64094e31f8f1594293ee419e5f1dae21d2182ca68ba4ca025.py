code = """import json
import re

# Load data from file paths
civic_docs_path = var_functions.query_db:2
funding_path = var_functions.query_db:4

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Build funding lookup
funding_lookup = {}
for fund in funding_records:
    proj = fund.get('Project_Name', '')
    amt = int(fund.get('Amount', 0))
    if proj:
        funding_lookup[proj] = amt

# Find Spring 2022 projects
spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for project name patterns
            if len(line) > 10 and len(line) < 150:
                keywords = ['Project', 'Improvements', 'Repairs', 'Replacement']
                if any(k in line for k in keywords):
                    if not line.startswith('(') and not line.startswith('To:') and not line.startswith('From:'):
                        spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match with funding data
matches = []
total = 0
for proj in spring_projects:
    if proj in funding_lookup:
        amt = funding_lookup[proj]
        matches.append({'project': proj, 'funding': amt})
        total += amt
    else:
        # Try partial matching
        proj_lower = proj.lower()
        for fund_proj, amt in funding_lookup.items():
            if proj_lower in fund_proj.lower() or fund_proj.lower() in proj_lower:
                matches.append({'project': proj, 'matched_funding_name': fund_proj, 'funding': amt})
                total += amt
                break

# Remove duplicates
unique = {}
for m in matches:
    key = m.get('matched_funding_name', m['project'])
    unique[key] = m['funding']

final_list = [{'project': k, 'funding': v} for k, v in unique.items()]
result = {'count': len(final_list), 'total_funding': total, 'projects': final_list}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
