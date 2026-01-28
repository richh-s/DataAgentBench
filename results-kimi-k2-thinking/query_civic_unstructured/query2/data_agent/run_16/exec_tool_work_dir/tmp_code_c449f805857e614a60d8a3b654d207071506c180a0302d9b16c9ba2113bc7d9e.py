code = """import json

# Access the stored results directly
funding_data = var_functions.query_db_8
civic_docs = var_functions.query_db_10

# Check what type of data we have
print('Type of funding_data: ' + str(type(funding_data)))
print('Type of civic_docs: ' + str(type(civic_docs)))

# If they're file paths (strings), read them
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print('Number of funding records: ' + str(len(funding_data)))
print('Number of civic documents: ' + str(len(civic_docs)))

# Let's examine the structure of the documents
if civic_docs:
    print('\nFirst document keys: ' + str(list(civic_docs[0].keys())))
    print('First document excerpt: ' + civic_docs[0]['text'][:300])

# Let's also look at some park-related project names from funding data
park_projects = [item for item in funding_data if 'park' in item['Project_Name'].lower()]
print('\nFound ' + str(len(park_projects)) + ' park-related projects in funding data')

# Now let's search for projects that are park-related AND completed in 2022
# We need to parse the text from civic_docs to find completed park projects in 2022

# First, let's find all park-related projects in funding data
park_project_names = [item['Project_Name'] for item in funding_data if 'park' in item['Project_Name'].lower()]
print('\nPark project names found in funding data:')
for name in park_project_names[:15]:
    print('  - ' + name)

# Let's search the civic documents for completed park projects in 2022
completed_park_projects = []

for doc in civic_docs:
    text = doc['text'].lower()
    
    # Check if this document mentions park projects completed in 2022
    if 'park' in text and 'completed' in text and '2022' in text:
        # Extract lines or sections that mention park projects
        lines = doc['text'].split('\n')
        for line in lines:
            lower_line = line.lower()
            if 'park' in lower_line and 'completed' in lower_line and '2022' in lower_line:
                completed_park_projects.append(line.strip())

print('\nFound ' + str(len(completed_park_projects)) + ' references to completed park projects in 2022')
for ref in completed_park_projects[:10]:
    print('  - ' + ref)

# Let's be more specific - look for project names in the documents
print('\nSearching for specific project names...')

# Some known park projects from our funding data
known_park_projects = [
    'Bluffs Park Shade Structure',
    'Bluffs Park Workout Station',
    'Legacy Park Benches and Arbors Renovation',
    'Legacy Park Paver Repair Project',
    'Malibu Bluffs Park Roof Replacement Project',
    'Malibu Bluffs Park South Walkway',
    'Malibu Bluffs Park South Walkway Repairs',
    'Trancas Canyon Park Upper and Lower Slopes Repair'
]

# Check if any of these appear as completed in 2022
for project_name in known_park_projects:
    for doc in civic_docs:
        if project_name.lower() in doc['text'].lower() and 'completed' in doc['text'].lower() and '2022' in doc['text'].lower():
            print('Found: ' + project_name + ' mentioned with completion in 2022')

# Let's try a different approach - extract project status information using regex patterns
import re

park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for patterns like "Project Name: updates... completed... 2022"
    # This is a simplified pattern
    park_matches = re.findall(r'([^\n]*park[^\n]*completed[^\n]*2022[^\n]*)', text, re.IGNORECASE)
    if park_matches:
        for match in park_matches:
            park_projects_2022.append(match.strip())

print('\nFound ' + str(len(park_projects_2022)) + ' park projects with completion in 2022 (regex):')
for proj in park_projects_2022[:10]:
    print('  - ' + proj)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
