code = """import json

# Get file paths
if 'var_functions.query_db:22' not in locals() or 'var_functions.query_db:19' not in locals():
    print('__RESULT__:')
    print(json.dumps({'error': 'Data not available'}))
    exit()

civic_path = locals()['var_functions.query_db:22']
funding_path = locals()['var_functions.query_db:19']

# Load data
civic_docs = []
funding_list = []

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_list = json.load(f)

# Create funding map
funding = {}
for item in funding_list:
    funding[item['Project_Name']] = int(item['Total_Amount'])

# Extract Spring 2022 projects
spring_projects = set()
for doc in civic_docs:
    for line in doc['text'].split('\n'):
        line = line.strip()
        if '2022' in line:
            if ('Morning View' in line or 'Project' in line) and len(line) > 20:
                clean = line.split('\n')[0].strip()
                if clean and not clean.startswith('Page'):  
                    spring_projects.add(clean)

# Match with funding
matched = []
total = 0
for proj in spring_projects:
    amount = 0
    if proj in funding:
        amount = funding[proj]
    elif '2022 Morning View Resurfacing & Storm Drain Improvements'.startswith(proj[:20]):
        amount = funding.get('2022 Morning View Resurfacing & Storm Drain Improvements', 0)
    
    if amount > 0:
        matched.append({'name': proj, 'funding': amount})
        total += amount

result = {'count': len(matched), 'total_funding': total, 'projects': matched}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}]}

exec(code, env_args)
