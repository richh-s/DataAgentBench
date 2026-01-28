code = """import json
import re

# Load civic documents
civic_path = locals()['var_functions.query_db:22']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = locals()['var_functions.query_db:19']
with open(funding_path, 'r') as f:
    funding_list = json.load(f)

# Create funding lookup
funding_lookup = {item['Project_Name']: int(item['Total_Amount']) for item in funding_list}

# Find Spring 2022 mentions
spring_2022_projects = []
checked_projects = set()

for doc in civic_docs:
    text = doc['text']
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 15:
                is_title = line.istitle() or line.isupper()
                has_keywords = 'Project' in line or 'Improvements' in line or 'Repair' in line
                
                if is_title and has_keywords:
                    if line not in checked_projects:
                        checked_projects.add(line)
                        base_name = line.split('(')[0].strip()
                        
                        funding_amount = 0
                        if line in funding_lookup:
                            funding_amount = funding_lookup[line]
                        elif base_name in funding_lookup:
                            funding_amount = funding_lookup[base_name]
                        
                        spring_2022_projects.append({
                            'project': line,
                            'funding': funding_amount
                        })

# Calculate totals
projects_with_funding = [p for p in spring_2022_projects if p['funding'] > 0]
total_funding = sum(p['funding'] for p in projects_with_funding)

print('__RESULT__:')
print(json.dumps({
    'project_count': len(projects_with_funding),
    'total_funding': total_funding,
    'projects': projects_with_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}]}

exec(code, env_args)
