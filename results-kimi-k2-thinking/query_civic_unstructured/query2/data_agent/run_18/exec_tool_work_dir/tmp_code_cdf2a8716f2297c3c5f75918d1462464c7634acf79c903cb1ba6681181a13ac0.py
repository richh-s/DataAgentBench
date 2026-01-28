code = """import json

# Load the data
funding_data = json.load(open('/tmp/tmp8opjs8_m.json'))
civic_docs_data = json.load(open('/tmp/tmpg5k2n9mq.json'))

# Find park projects in funding data
park_projects = [item for item in funding_data if 'park' in item['Project_Name'].lower()]

print('Park projects in funding data:')
for p in park_projects:
    print(p['Project_Name'], '- $' + p['Amount'])

# Search civic docs for completed park projects in 2022
print('\nSearching civic documents for park projects completed in 2022...')

# Key document mentions for 2022 completion
matches = []
for doc in civic_docs_data:
    text = doc['text']
    
    # Check for Bluffs Park Shade Structure
    if 'Bluffs Park Shade Structure' in text and 'completed November 2022' in text:
        matches.append('Bluffs Park Shade Structure')
        
    # Check for Marie Canyon Green Streets (has park-related aspects)
    if 'Marie Canyon Green Streets' in text and 'completed, January 2023' in text:
        # January 2023 notice for November 2022 completion
        if 'construction was completed' in text:
            matches.append('Marie Canyon Green Streets')

print('\nProjects completed in 2022:', matches)

# Calculate total funding
total = 0
for project in matches:
    for fund in park_projects:
        if fund['Project_Name'] == project:
            amount = int(fund['Amount'])
            total += amount
            print('Matched:', project, '- $' + str(amount))

print('\nTotal funding for park projects completed in 2022: $' + str(total))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
