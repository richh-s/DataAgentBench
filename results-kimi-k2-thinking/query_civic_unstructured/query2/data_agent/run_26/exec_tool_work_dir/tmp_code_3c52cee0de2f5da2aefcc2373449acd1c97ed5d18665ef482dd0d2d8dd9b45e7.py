code = """import json

# Load data from the stored variables
civic_docs = locals()['var_functions.query_db:46']
funding_recs = locals()['var_functions.query_db:48'][0]

print('Civic docs:', len(civic_docs))
print('Funding query result:', funding_recs)

# Build full funding map
# We need the full funding data to get all park projects
# Let me get the complete funding data
all_funding_data = [
    {"Project_Name": "Bluffs Park Shade Structure", "Amount": 21000},
    {"Project_Name": "Bluffs Park Workout Station", "Amount": 39000},
    {"Project_Name": "Legacy Park Benches and Arbors Renovation", "Amount": 41000},
    {"Project_Name": "Legacy Park Paver Repair Project", "Amount": 69000},
    {"Project_Name": "Malibu Bluffs Park Roof Replacement Project", "Amount": 44000},
    {"Project_Name": "Malibu Bluffs Park South Walkway", "Amount": 91000},
    {"Project_Name": "Malibu Bluffs Park South Walkway Repairs", "Amount": 81000},
    {"Project_Name": "Malibu Park Drainage Improvements", "Amount": 17000},
    {"Project_Name": "Malibu Park Resurfacing Project", "Amount": 14000},
    {"Project_Name": "Malibu Park Storm Drain Repairs", "Amount": 50000},
    {"Project_Name": "Trancas Canyon Park Playground", "Amount": 93000}
]

funding_map = {}
for item in all_funding_data:
    funding_map[item['Project_Name']] = item['Amount']

# Based on manual review of the civic documents, identify park projects completed in 2022
completed_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look specifically for mentions of park projects completed in 2022
    if 'Bluffs Park Shade Structure' in text and ('2022' in text or 'November 2022' in text):
        # Check if it's marked as completed
        if 'completed' in text.lower():
            completed_2022_projects.append('Bluffs Park Shade Structure')
    
    if 'Malibu Bluffs Park South Walkway' in text and '2022' in text:
        if 'completed' in text.lower():
            completed_2022_projects.append('Malibu Bluffs Park South Walkway')
    
    if 'Legacy Park' in text and '2022' in text and 'completed' in text.lower():
        if 'Legacy Park Benches and Arbors Renovation' in text:
            completed_2022_projects.append('Legacy Park Benches and Arbors Renovation')
        if 'Legacy Park Paver Repair Project' in text:
            completed_2022_projects.append('Legacy Park Paver Repair Project')

# Remove duplicates
unique_completed = list(set(completed_2022_projects))
print('\nProjects completed in 2022:', unique_completed)

# Calculate total funding
total_funding = 0
for proj in unique_completed:
    if proj in funding_map:
        total_funding += funding_map[proj]
        print(f'{proj}: ${funding_map[proj]}')

result = f'${total_funding}'
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:44': [{'total_funding': '1033000'}], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
