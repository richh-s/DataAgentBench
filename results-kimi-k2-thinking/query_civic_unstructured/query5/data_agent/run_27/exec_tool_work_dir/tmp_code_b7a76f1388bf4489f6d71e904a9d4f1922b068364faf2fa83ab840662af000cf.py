code = """import json
import re

# Read funding data directly from the file
funding_data = json.load(open('file_storage/functions.query_db:5.json', 'r'))

# Read civic docs
civic_docs = json.load(open('file_storage/functions.query_db:6.json', 'r'))

print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

print("\nSample funding map entries:")
count = 0
for name, amount in funding_map.items():
    if count < 5:
        print("  " + name + ": $" + str(amount))
        count += 1

# Parse civic documents to find disaster projects that started in 2022
disaster_projects_2022 = []

# Patterns to identify disaster-related keywords
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster']

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Check if line contains disaster indicators
        has_disaster_suffix = any(suffix in line for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)'])
        has_disaster_keyword = any(keyword in line for keyword in disaster_keywords)
        
        if has_disaster_suffix or has_disaster_keyword:
            if '2022' in line:
                disaster_projects_2022.append(line)
            else:
                context = '\n'.join(lines[i:i+10])
                if '2022' in context:
                    disaster_projects_2022.append(line)

print("\nFound", len(disaster_projects_2022), "potential disaster projects:")
for proj in disaster_projects_2022[:15]:
    print("  - " + proj)

result_info = {"disaster_count": len(disaster_projects_2022), "funding_count": len(funding_data)}
print("__RESULT__:")
print(json.dumps(result_info))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
