code = """import json
import re

# Load data from the stored file paths
civic_docs = json.load(open(var_functions.query_db_50))
funding_data = json.load(open(var_functions.query_db_60))

# Build funding lookup dictionary
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(fund.get('Amount', 0))

print(f'Loaded {len(civic_docs)} civic documents and {len(funding_lookup)} funded projects')

# Find Spring 2022 projects and match with funding
spring_2022_projects = []
used_funding_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if this document mentions Spring 2022
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Look for project names in the text
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty or formatting lines
            if not line or len(line) < 10 or len(line) > 200:
                continue
            if line.startswith('(') or line.startswith('To:') or line.startswith('From:'):
                continue
                
            # Look for project indicators
            project_keywords = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Installation', 'System', 'Facility']
            if any(keyword in line for keyword in project_keywords):
                # Try to match with funding data
                # First try exact match
                if line in funding_lookup and line not in used_funding_names:
                    amount = funding_lookup[line]
                    spring_2022_projects.append({'name': line, 'funding': amount})
                    used_funding_names.add(line)
                else:
                    # Try partial matching
                    line_lower = line.lower()
                    for fund_name in funding_lookup:
                        if fund_name in used_funding_names:
                            continue
                        # Check if one is substring of the other
                        if (line_lower in fund_name.lower() or fund_name.lower() in line_lower):
                            # Avoid matching very different lengths
                            if abs(len(line) - len(fund_name)) < 50:
                                amount = funding_lookup[fund_name]
                                spring_2022_projects.append({'name': line, 'matched_funding': fund_name, 'funding': amount})
                                used_funding_names.add(fund_name)
                                break

# Remove duplicates by project name
unique_projects = {}
for proj in spring_2022_projects:
    proj_name = proj['name']
    funding_amt = proj['funding']
    if proj_name not in unique_projects:
        unique_projects[proj_name] = funding_amt

final_count = len(unique_projects)
final_total = sum(unique_projects.values())

result = {
    'project_count': final_count,
    'total_funding': final_total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}], 'var_functions.list_db:56': ['civic_docs'], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
