code = """import json

# Get file paths from storage
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

# Load civic documents
civic_docs_text = open(civic_docs_path).read()
civic_docs = json.loads(civic_docs_text)

# Load funding data
funding_text = open(funding_path).read()
funding_data = json.loads(funding_text)

print('Data loaded successfully')

# Now process to find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for completion in 2022
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        if '2022' in line and ('completed' in line_lower or 'completion' in line_lower):
            # Look for park project name nearby
            for j in range(max(0,i-5), min(len(lines), i+5)):
                proj_line = lines[j].strip()
                if 'park' in proj_line.lower() and len(proj_line) > 5:
                    clean_name = proj_line.replace('•', '').replace('◦', '').strip()
                    if clean_name and clean_name not in park_projects:
                        park_projects.append(clean_name)

print('Found {} park projects completed in 2022'.format(len(park_projects)))

# Calculate total funding amount
total_amount = 0
for park in park_projects:
    park_name = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower().replace(' ', '').replace('-', '')
        if park_name in fund_name or fund_name in park_name:
            total_amount += int(fund['Amount'])

result = {'total_funding_dollars': total_amount}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
