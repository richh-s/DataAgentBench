code = """import json
import re

# Load data
civic_docs_path = var_functions.query_db:2
funding_path = var_functions.query_db:4

civic_docs = []
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

funding_records = []
with open(funding_path) as f:
    funding_records = json.load(f)

# Build funding map
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name')
    amount = int(rec.get('Amount', 0))
    if name:
        funding_map[name] = amount

# Find projects mentioned with Spring 2022
spring2022_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.splitlines()
        for line in lines:
            line = line.strip()
            # Skip empty or formatting lines
            if not line or line.startswith('(') or ':' in line[:10]:
                continue
            # Look for lines that contain project keywords
            if any(kw in line for kw in ['Project', 'Improvements', 'Repairs', 'Replacement']):
                if 10 < len(line) < 150:
                    spring2022_projects.add(line)

# Match projects with funding
matches = []
matched_names = set()
for proj in spring2022_projects:
    if proj in funding_map:
        amt = funding_map[proj]
        if proj not in matched_names:
            matches.append({'project': proj, 'funding': amt})
            matched_names.add(proj)
    else:
        # Check for partial matches
        proj_lower = proj.lower()
        for fund_name in funding_map:
            if (proj_lower in fund_name.lower() or fund_name.lower() in proj_lower):
                if fund_name not in matched_names:
                    amt = funding_map[fund_name]
                    matches.append({'project': proj, 'funding': amt})
                    matched_names.add(fund_name)
                break

total_funding = sum(m['funding'] for m in matches)

result = {
    'project_count': len(matches),
    'total_funding': total_funding,
    'projects': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
