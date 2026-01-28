code = """import json

# Load data files
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

print("Loaded data successfully")

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for park projects with 2022 completion
    lines = text.split('\n')
    for i in range(len(lines)):
        if '2022' in lines[i] and \
           ('completed' in lines[i].lower() or 'completion' in lines[i].lower()):
            
            # Look nearby for park project names
            for j in range(max(0,i-5), min(len(lines), i+5)):
                project_line = lines[j].strip()
                if 'park' in project_line.lower() and len(project_line) > 10:
                    # Clean up the project name
                    clean_name = project_line.replace('•', '').replace('◦', '').strip()
                    if clean_name not in park_projects:
                        park_projects.append(clean_name)

print("Found projects:", len(park_projects))

# Calculate total funding for these projects
total_funding = 0
for park in park_projects:
    park_normalized = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_data:
        fund_normalized = fund['Project_Name'].lower().replace(' ', '').replace('-', '')
        if park_normalized in fund_normalized or fund_normalized in park_normalized:
            total_funding += int(fund['Amount'])
            print("Match:", park, "->", fund['Project_Name'], "=", fund['Amount'])

result = {"total_funding_dollars": total_funding}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
