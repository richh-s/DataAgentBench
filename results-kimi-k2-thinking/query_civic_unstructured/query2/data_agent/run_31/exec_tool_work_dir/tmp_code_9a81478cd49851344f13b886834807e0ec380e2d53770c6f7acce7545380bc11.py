code = """import json

# Look for available variables and load data systematically
funding_path = None
civic_path = None

# Check all local variables for the file paths
for key, value in locals().items():
    if 'query_db' in str(key):
        if 'funding' in str(key).lower() and isinstance(value, str):
            funding_path = value
        elif 'civic' in str(key).lower() and isinstance(value, str):
            civic_path = value

# Load funding data
funding_data = []
if funding_path:
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)

# Load civic documents
civic_docs = []
if civic_path:
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)

# From civic docs, find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for completion mentions in 2022
    if 'completed' in text.lower() and '2022' in text:
        # Check for specific park projects
        if 'Bluffs Park Shade Structure' in text:
            if 'completed' in text and '2022' in text:
                # Verify it's actually completed in 2022
                lines = text.split('\n')
                for line in lines:
                    if 'Bluffs Park Shade Structure' in line:
                        if 'completed' in line.lower() and '2022' in line:
                            park_projects.append('Bluffs Park Shade Structure')

# Remove duplicates
park_projects = list(set(park_projects))

# Find funding amounts
project_funding = {}
for proj in park_projects:
    for funding in funding_data:
        if proj == funding.get('Project_Name', ''):
            project_funding[proj] = int(funding.get('Amount', 0))

# Calculate total
total_funding = sum(project_funding.values())

result = {
    'projects_completed_2022': list(project_funding.keys()),
    'total_funding': total_funding,
    'details': project_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.execute_python:0': {'collection': 'civic_docs', 'filter': {'text': {'$regex': 'park', '$options': 'i'}}, 'projection': {'filename': 1, 'text': 1}}, 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
