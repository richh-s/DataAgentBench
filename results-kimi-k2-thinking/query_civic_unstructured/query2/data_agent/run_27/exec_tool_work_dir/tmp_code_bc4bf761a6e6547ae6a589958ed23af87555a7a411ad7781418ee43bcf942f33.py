code = """import json
import re

# Load the data from the files
civic_docs_file = locals()['var_functions.query_db:16']
funding_file = locals()['var_functions.query_db:17']

civic_docs_text = open(civic_docs_file).read()
funding_text = open(funding_file).read()

civic_docs = json.loads(civic_docs_text)
funding_data = json.loads(funding_text)

print('Loaded', len(civic_docs), 'civic documents and', len(funding_data), 'funding records')

# Find park projects completed in 2022
park_projects_2022 = []

# Process each document
for doc in civic_docs:
    text = doc['text']
    
    # Look for park-related projects with completion in 2022
    # Search for patterns
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
                # Search nearby lines for park name
                for j in range(max(0, i-5), min(len(lines), i+5)):
                    nearby = lines[j].strip()
                    if 'park' in nearby.lower() and len(nearby) > 5:
                        clean_name = nearby.replace('•', '').replace('◦', '').strip()
                        clean_name = re.sub(r'^[A-Z]\.?\s+', '', clean_name)
                        if clean_name and clean_name not in park_projects_2022:
                            park_projects_2022.append(clean_name)

print('Found park projects completed in 2022:', len(park_projects_2022))

# Calculate total funding
total_funding = 0
for park in park_projects_2022:
    park_simple = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_simple = fund_name.lower().replace(' ', '').replace('-', '')
        if park_simple in fund_simple or fund_simple in park_simple:
            total_funding += int(fund['Amount'])
            break

result = {'total_funding_dollars': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
