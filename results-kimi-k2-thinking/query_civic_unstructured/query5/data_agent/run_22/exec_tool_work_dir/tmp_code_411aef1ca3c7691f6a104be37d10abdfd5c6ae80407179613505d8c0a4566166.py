code = """import json

# Load data from files
f_path = locals()['var_functions.query_db:6']
c_path = locals()['var_functions.query_db:7']

with open(f_path) as f:
    funding = json.load(f)
with open(c_path) as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    n = r.get('Project_Name', '')
    amount = int(r.get('Amount', 0))
    if n:
        fund_map[n] = fund_map.get(n, 0) + amount

# Count disaster projects with 2022 dates
total_funding = 0
disaster_count = 0

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if document has disaster keywords
    has_disaster = any(k in text.upper() for k in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER'])
    
    # Check if document has 2022 dates in project context
    has_2022 = '2022' in text and any(w in text.upper() for w in ['DESIGN', 'CONSTRUCTION'])
    
    if has_disaster and has_2022:
        # Find project names in this document
        lines = text.split('\n')
        for i in range(len(lines)-1):
            line = lines[i].strip()
            if line and not line.startswith('(') and not 'page' in line.lower():
                if 'Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]:
                    project_name = line
                    if any(x in project_name.upper() for x in ['DISASTER', 'FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY']) or 'RECOVERY' in project_name.upper():
                        disaster_count += 1
                        # Find funding for this project
                        for fund_name, amount in fund_map.items():
                            if project_name in fund_name or fund_name in project_name:
                                total_funding += amount
                                break

result = {
    'total_funding_for_disaster_projects_2022': total_funding,
    'disaster_projects_count': disaster_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
