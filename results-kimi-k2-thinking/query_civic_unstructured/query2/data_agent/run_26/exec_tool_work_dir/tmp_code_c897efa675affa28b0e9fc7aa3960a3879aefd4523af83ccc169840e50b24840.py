code = """import json

# The data is stored as strings with file paths
# Let me read the actual data from the stored keys

civic_docs_key = 'var_functions.query_db:46'
funding_key = 'var_functions.query_db:48'

# Since these are file paths, I need to read them
with open(civic_docs_key, 'r') as f:
    civic_docs_content = f.read()

with open(funding_key, 'r') as f:
    funding_content = f.read()

# Parse the JSON content
civic_docs = json.loads(civic_docs_content)
funding_recs = json.loads(funding_content)

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_recs))

# Build funding map
funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Look for park projects completed in 2022
park_projects_2022 = []

# From manual review of the text:
# Looking for patterns like "Bluffs Park Shade Structure" completed November 2022
# and other park projects with 2022 completion dates

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look specifically for completed park projects in 2022
    # Pattern: Park name followed by completion info
    
    if 'Bluffs Park Shade Structure' in text and 'November 2022' in text:
        park_projects_2022.append('Bluffs Park Shade Structure')
    
    if 'Malibu Bluffs Park South Walkway' in text and '2022' in text:
        # Check if completed
        if 'completed' in text.lower():
            park_projects_2022.append('Malibu Bluffs Park South Walkway')
    
    if 'Legacy Park' in text and '2022' in text:
        if 'completed' in text.lower():
            # Extract specific legacy park projects
            if 'Legacy Park Benches and Arbors Renovation' in text:
                park_projects_2022.append('Legacy Park Benches and Arbors Renovation')
            if 'Legacy Park Paver Repair Project' in text:
                park_projects_2022.append('Legacy Park Paver Repair Project')

# Remove duplicates
unique_projects = list(set(park_projects_2022))
print('\nIdentified projects:', unique_projects)

# Calculate total funding
total_funding = 0
for proj in unique_projects:
    if proj in funding_map:
        total_funding += funding_map[proj]
        print(f'{proj}: ${funding_map[proj]}')

print(f'\nTotal funding: ${total_funding}')

result = f'${total_funding}'
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:44': [{'total_funding': '1033000'}], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
