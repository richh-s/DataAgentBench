code = """import json

# Manually created list from the documents of capital projects with design status
known_design_projects = [
    '2022 Morning View Resurfacing & Storm Drain Improvements',
    'PCH Median Improvements Project',
    'Westward Beach Road Repair Project',
    'Westward Beach Road Drainage Improvements Project',
    'Clover Heights Storm Drainage Improvements',
    'Latigo Canyon Road Retaining Wall Repair Project',
    'Storm Drain Master Plan',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Civic Center Water Treatment Facility Phase 2',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Outdoor Warning Signs',
    'Malibu Bluffs Park South Walkway Repairs',
    'Trancas Canyon Park Playground',
    'Malibu Canyon Road Traffic Study'
]

# Load funding data by directly accessing the stored file path
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup
funded_amounts = {}
for rec in funding_data:
    project_name = rec['Project_Name'].strip().lower()
    funded_amounts[project_name] = int(rec['Amount'])

# Count matches with funding > $50,000
count_over_50000 = 0
matched_projects = []

for project in known_design_projects:
    proj_lower = project.lower()
    
    # Direct match
    if proj_lower in funded_amounts and funded_amounts[proj_lower] > 50000:
        count_over_50000 += 1
        matched_projects.append({
            'project': project,
            'funding': funded_amounts[proj_lower]
        })
    else:
        # Check for partial/fuzzy matches
        for funded_name, amount in funded_amounts.items():
            if amount > 50000:
                # Check if project name is contained in funded name or vice versa
                if (proj_lower in funded_name or funded_name in proj_lower) and len(funded_name) > 10:
                    if abs(len(proj_lower) - len(funded_name)) < 30:  # Similar length to avoid false matches
                        count_over_50000 += 1
                        matched_projects.append({
                            'project': project,
                            'matched_as': funded_name,
                            'funding': amount
                        })
                        break

print('__RESULT__:')
print(json.dumps({
    'count_over_50000': count_over_50000,
    'matched': matched_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0, 'var_functions.execute_python:72': {'funding': 'var_functions.query_db:0', 'civic': 'var_functions.query_db:2'}, 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
