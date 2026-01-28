code = """import json

funding = json.load(open('/tmp/tmp8opjs8_m.json'))
civic_docs = json.load(open('/tmp/tmpg5k2n9mq.json'))

print('Funding records:', len(funding))
print('Civic documents:', len(civic_docs))

# Find all park projects
park_projects = []
for item in funding:
    if 'park' in item['Project_Name'].lower():
        park_projects.append(item)

print('\nPark projects in database:', len(park_projects))
for p in park_projects:
    print('-', p['Project_Name'], '$' + p['Amount'])

# Look for 2022 completions in documents
total_funding = 0
projects_found = []

for doc in civic_docs:
    text = doc['text']
    
    # Search patterns for completed park projects in 2022
    if 'Bluffs Park Shade Structure' in text:
        if 'November 2022' in text and 'completed' in text:
            print('\nFound: Bluffs Park Shade Structure completed in November 2022')
            # Find funding amount
            for p in park_projects:
                if p['Project_Name'] == 'Bluffs Park Shade Structure':
                    amount = int(p['Amount'])
                    total_funding += amount
                    projects_found.append(('Bluffs Park Shade Structure', amount))
                    print('Funding: $' + str(amount))

print('\nTotal funding:', total_funding)
print('Projects found:', len(projects_found))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
