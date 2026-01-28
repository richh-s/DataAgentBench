code = """import json
import re

# Get file paths
civic_docs_file = locals()['var_functions.query_db:16']
funding_file = locals()['var_functions.query_db:17']

# LoadJSON data
with open(civic_docs_file) as f:
    civic_docs = json.load(f)
with open(funding_file) as f:
    funding_data = json.load(f)

# Find park projects completed in 2022
park_list = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        # Look for completion in 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Search near this line for park project names
            for j in range(max(0,i-5), min(len(lines), i+5)):
                context = lines[j].strip()
                if 'park' in context.lower() and len(context) > 5 and not context.startswith('('):
                    # Clean name
                    clean_name = context.replace('•','').replace('◦','').strip()
                    if clean_name not in park_list:
                        park_list.append(clean_name)

# Calculate funding
funded_amount = 0
for park in park_list:
    park_key = park.lower().replace(' ','')
    for fund in funding_data:
        fund_key = fund['Project_Name'].lower().replace(' ','')
        if park_key in fund_key or fund_key in park_key:
            funded_amount += int(fund['Amount'])
            break

result = {'total_funding': funded_amount}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
