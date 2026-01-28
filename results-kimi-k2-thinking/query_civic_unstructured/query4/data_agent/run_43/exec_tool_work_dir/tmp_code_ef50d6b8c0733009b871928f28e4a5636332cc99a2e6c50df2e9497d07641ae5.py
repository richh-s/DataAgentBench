code = """import json

# Load civic documents
civic_docs = []
with open(locals()['var_functions.query_db:22'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_data = []
with open(locals()['var_functions.query_db:19'], 'r') as f:
    funding_data = json.load(f)

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Total_Amount'])

# Find Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc['text']
    
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            
            if len(line) > 15 and (line.istitle() or line.isupper()):
                if 'Project' in line or 'Improvements' in line or 'Repair' in line:
                    spring_2022_projects.append(line)

# Count unique projects and find funding
unique_projects = list(set(spring_2022_projects))

total_funding = 0
matched_projects = []

for project in unique_projects:
    clean_name = project.strip()
    
    if clean_name in funding_lookup:
        amount = funding_lookup[clean_name]
        total_funding += amount
        matched_projects.append({'name': clean_name, 'funding': amount})
    else:
        base_name = clean_name.split('(')[0].strip()
        if base_name in funding_lookup:
            amount = funding_lookup[base_name]
            total_funding += amount
            matched_projects.append({'name': clean_name, 'funding': amount, 'base': base_name})

result = {
    "project_count": len(matched_projects),
    "total_funding": total_funding,
    "sample_projects": matched_projects[:10]
}

print("__RESULT__:")
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}]}

exec(code, env_args)
