code = """import json, re

# Load the data files
civic_docs = json.load(open('var_functions.query_db:16'))
funding_data = json.load(open('var_functions.query_db:17'))

print('Files loaded')

# Process civic documents to find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Look for completion dates in 2022
    for i in range(len(lines)):
        line = lines[i]
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look for park names in this area
            for j in range(max(0, i-5), min(len(lines), i+5)):
                check_line = lines[j].strip()
                if 'park' in check_line.lower() and len(check_line) > 5:
                    # Clean the project name
                    clean_name = re.sub(r'^[A-Z]\s+', '', check_line)
                    clean_name = clean_name.replace('•','').replace('◦','').strip()
                    if clean_name not in park_projects:
                        park_projects.append(clean_name)

print('Park projects found:', len(park_projects))
for p in park_projects:
    print('-', p)

# Calculate total funding
total_funding = 0
for park in park_projects:
    park_simple = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_data:
        fund_simple = fund['Project_Name'].lower().replace(' ', '').replace('-', '')
        if park_simple in fund_simple or fund_simple in park_simple:
            total_funding += int(fund['Amount'])
            print('Matched:', park, '->', fund['Project_Name'], '=', fund['Amount'])
            break

result = {'total_funding_dollars': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
