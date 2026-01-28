code = """import json

# Get file paths from storage
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

# Load civic documents
civic_docs = []
with open(civic_docs_path) as f:
    for line in f:
        if line.strip():
            civic_docs.extend(json.loads(line))

# Load funding data
funding_data = []
with open(funding_path) as f:
    for line in f:
        if line.strip():
            funding_data.extend(json.loads(line))

print('Loaded', len(civic_docs), 'civic docs and', len(funding_data), 'funding records')

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Look for completion in 2022
        if '2022' in line and ('completed' in line_lower or 'completion' in line_lower):
            # Look for park project name in surrounding lines
            for j in range(max(0,i-5), min(len(lines), i+5)):
                proj_line = lines[j].strip()
                if 'park' in proj_line.lower() and len(proj_line) > 5:
                    # Clean the name
                    clean_name = proj_line.replace('•', '').replace('◦', '').strip()
                    clean_name = clean_name[2:].strip() if len(clean_name) > 2 and clean_name[0].isalpha() and clean_name[1] == ' ' else clean_name
                    
                    if clean_name and clean_name not in park_projects:
                        park_projects.append(clean_name)
                        break

print('Found park projects completed in 2022:', len(park_projects))

# Calculate total funding
total_funding = 0
for park in park_projects:
    park_simple = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_data:
        fund_simple = fund['Project_Name'].lower().replace(' ', '').replace('-', '')
        if park_simple in fund_simple or fund_simple in park_simple:
            total_funding += int(fund['Amount'])
            break

result = {'total_funding_dollars': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
