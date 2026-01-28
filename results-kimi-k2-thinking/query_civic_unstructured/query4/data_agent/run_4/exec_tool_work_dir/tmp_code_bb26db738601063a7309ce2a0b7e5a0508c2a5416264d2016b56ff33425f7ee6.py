code = """import json
import re

# Load data from the stored file paths
civic_docs = json.load(open(var_functions.query_db:50))
funding_data = json.load(open(var_functions.query_db:52))

# Build funding lookup dictionary
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(fund.get('Amount', 0))

# Find Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if this document mentions Spring 2022
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Extract project names (simple heuristic)
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip empty lines and formatting
            if not line or len(line) < 10 or len(line) > 200:
                continue
            if line.startswith('(') or line.startswith('To:') or line.startswith('From:'):
                continue
                
            # Look for project indicators
            project_keywords = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Installation', 'System']
            if any(keyword in line for keyword in project_keywords):
                # Check if this project has funding
                if line in funding_lookup:
                    spring_2022_projects.append({'name': line, 'funding': funding_lookup[line], 'type': 'exact'})
                else:
                    # Try partial match
                    for fund_name in funding_lookup:
                        # Check if one is substring of the other (allowing some difference in length)
                        if (line.lower() in fund_name.lower() or fund_name.lower() in line.lower()):
                            if abs(len(line) - len(fund_name)) < 50:  # Avoid matching completely different names
                                spring_2022_projects.append({'name': line, 'funding': funding_lookup[fund_name], 'type': 'partial', 'matched': fund_name})
                                break

# Remove duplicates while preserving highest funding amount
unique_projects = {}
for proj in spring_2022_projects:
    name = proj['name']
    funding = proj['funding']
    if name not in unique_projects or funding > unique_projects[name]['funding']:
        unique_projects[name] = proj

final_projects = list(unique_projects.values())
total_funding = sum(p['funding'] for p in final_projects)

result = {
    'spring_2022_project_count': len(final_projects),
    'total_funding_amount': total_funding,
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}], 'var_functions.list_db:56': ['civic_docs']}

exec(code, env_args)
