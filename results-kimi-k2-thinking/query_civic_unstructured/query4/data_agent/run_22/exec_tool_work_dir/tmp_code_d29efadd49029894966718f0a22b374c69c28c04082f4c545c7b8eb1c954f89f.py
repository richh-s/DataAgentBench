code = """import json
import re

# Read civic documents
civic_docs_path = locals()['var_functions.query_db:5']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data  
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Create a mapping of project names to funding amounts
funding_map = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records}

# Extract projects from civic documents
spring_2022_projects = []

for doc in civic_docs:
    text = doc['text']
    
    patterns = [
        r'([^\n]+?)\n\(cid:190\) Project Schedule:\n[^\n]*(?:st:|Start|Complete Design|Advertise|Begin Construction|Construction)[^\n]*?(?:2022-Spring|Spring 2022|2022-March|2022-April|2022-May|March 2022|April 2022|May 2022)',
        r'([^\n]+?)\n\(cid:190\) Project Schedule:\n(?:[^\n]*\n){0,3}[^\n]*(?:2022-Spring|Spring 2022|2022-March|2022-April|2022-May|March 2022|April 2022|May 2022)',
        r'(\d{4} [^\n]+?)\n[^\n]*(?:2022-Spring|Spring 2022|2022-March|2022-April|2022-May)',
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            project_name = match.group(1).strip()
            if len(project_name) > 0 and project_name not in ['Capital Improvement Projects', 'Disaster Recovery Projects']:
                if project_name not in [p['name'] for p in spring_2022_projects]:
                    amount = funding_map.get(project_name, 0)
                    spring_2022_projects.append({
                        'name': project_name,
                        'funding': amount
                    })

# Also check for projects with 2022 in the name (they likely started in 2022)
year_in_name = [
    '2022 Morning View Resurfacing & Storm Drain Improvements',
    '2022 Annual Street Maintenance'
]

for proj_name in year_in_name:
    if proj_name in str(civic_docs):
        if proj_name not in [p['name'] for p in spring_2022_projects]:
            amount = funding_map.get(proj_name, 0)
            spring_2022_projects.append({
                'name': proj_name,
                'funding': amount
            })

# Calculate totals
total_projects = len(spring_2022_projects)
total_funding = sum(p['funding'] for p in spring_2022_projects)

result = {
    'project_count': total_projects,
    'total_funding': total_funding,
    'projects': spring_2022_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json'}

exec(code, env_args)
