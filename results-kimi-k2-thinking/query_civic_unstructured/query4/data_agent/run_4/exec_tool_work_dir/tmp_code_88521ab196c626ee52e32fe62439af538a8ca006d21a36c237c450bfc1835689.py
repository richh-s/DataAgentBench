code = """import json

# Load data files
civic_file = var_functions.query_db:2
funding_file = var_functions.query_db:4

civic_docs = json.load(open(civic_file))
funding = json.load(open(funding_file))

# Build funding lookup
funding_lookup = {}
for item in funding:
    name = item.get('Project_Name')
    if name:
        funding_lookup[name] = int(item.get('Amount', 0))

# Count Spring 2022 projects that have funding
spring_2022_with_funding = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Look for project names in the text
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Simple pattern matching for project names
            if len(line) > 10 and any(k in line for k in ['Project', 'Improvements', 'Repairs']):
                # Check if this project has funding
                if line in funding_lookup:
                    if line not in [p['name'] for p in spring_2022_with_funding]:
                        spring_2022_with_funding.append({'name': line, 'funding': funding_lookup[line]})
                else:
                    # Try partial match
                    for fund_name in funding_lookup:
                        if line.lower() in fund_name.lower() or fund_name.lower() in line.lower():
                            if fund_name not in [p['name'] for p in spring_2022_with_funding]:
                                spring_2022_with_funding.append({'name': fund_name, 'funding': funding_lookup[fund_name]})
                            break

count = len(spring_2022_with_funding)
total_funding = sum(p['funding'] for p in spring_2022_with_funding)

result = {'count': count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
