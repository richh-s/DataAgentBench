code = """import json
import re

# Load the data
mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Find park projects completed in 2022
park_projects_2022 = []

for doc in mongo_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Quick check if relevant keywords exist
    if 'park' in text_lower and 'completed' in text_lower and '2022' in text:
        lines = text.split('\n')
        
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line:
                continue
                
            line_lower = line.lower()
            
            # Check if line contains park
            if 'park' in line_lower:
                # Look ahead for completion in 2022
                found_completion = False
                for j in range(i+1, min(i+15, len(lines))):
                    next_line = lines[j]
                    if 'completed' in next_line.lower() and '2022' in next_line:
                        found_completion = True
                        break
                
                if found_completion:
                    # Clean the project name
                    clean_name = re.sub(r'^[•\-●■\s]+', '', line)
                    if clean_name and 5 < len(clean_name) < 200:
                        park_projects_2022.append(clean_name)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Match with funding and calculate total
funding_map = {}
for record in funding_records:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[name] = amount

total_funding = 0
matched_projects = []

for park_proj in park_projects_2022:
    for fund_name in funding_map:
        # Check for match (partial match in either direction)
        if (park_proj.lower() in fund_name.lower() or 
            fund_name.lower() in park_proj.lower()):
            amount = funding_map[fund_name]
            total_funding += amount
            matched_projects.append({
                'project_name': park_proj,
                'funding_name': fund_name,
                'amount': amount
            })

result = {
    'park_projects_2022': park_projects_2022,
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
