code = """import json
import re

# Load funding data
funding_data = json.load(open('file_storage/functions.query_db:5.json', 'r'))

# Load civic documents  
civic_docs = json.load(open('file_storage/functions.query_db:6.json', 'r'))

funding_count = len(funding_data)
civic_count = len(civic_docs)

# Build funding map
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Find disaster projects started in 2022
disaster_projects = []
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster']

for doc in civic_docs:
    text = doc['text']
    # Look for lines with project names
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 10:
            continue
            
        # Check for disaster indicators
        has_suffix = False
        has_keyword = False
        
        for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']:
            if suffix in line:
                has_suffix = True
                break
                
        for keyword in disaster_keywords:
            if keyword in line:
                has_keyword = True
                break
        
        if has_suffix or has_keyword:
            if '2022' in line:
                disaster_projects.append(line)
            else:
                # Check next 10 lines for 2022
                context = '\n'.join(lines[i:i+10])
                if '2022' in context:
                    disaster_projects.append(line)

disaster_count = len(disaster_projects)

# Match with funding data
matches = []
total_funding = 0

for project in disaster_projects:
    for funding_name, amount in funding_map.items():
        if project in funding_name or funding_name in project:
            matches.append((funding_name, amount))
            total_funding += amount

result = {"funding_count": funding_count, "civic_count": civic_count, "disaster_projects": disaster_count, "matches": matches, "total_funding": total_funding}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
