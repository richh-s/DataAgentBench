code = """import json

# Load data
with open('var_functions.query_db:0') as f:
    funding_d = json.load(f)

with open('var_functions.query_db:2') as f:
    civic_d = json.load(f)

funded = {}
for rec in funding_d:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# Find design projects simply - look for patterns
keywords = ['PCH Median Improvements Project', 'Westward Beach Road', 'Clover Heights Storm Drainage Improvements', 
            'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan',
            'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2',
            'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane',
            'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs',
            'Trancas Canyon Park Playground', 'Malibu Canyon Road Traffic Study']

# These are actual project names found in the documents above
actual_projects = ['2022 Morning View Resurfacing & Storm Drain Improvements',
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
                   'Malibu Canyon Road Traffic Study']

count = 0
for proj in actual_projects:
    proj_key = proj.lower()
    for funded_name in funded:
        if proj_key in funded_name or funded_name in proj_key:
            if funded[funded_name] > 50000:
                count += 1
                break

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0}

exec(code, env_args)
