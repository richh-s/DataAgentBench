code = """import json
import os

# Check what we have in storage
funding_path = str(var_functions.query_db:0)
civic_path = str(var_functions.query_db:2)

# Try to load the data
if os.path.exists(funding_path):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    # It's probably already loaded JSON data
    funding_data = var_functions.query_db:0

if os.path.exists(civic_path):
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

# Create funding lookup (handle both cases)
funded = {}
if isinstance(funding_data, list):
    for rec in funding_data:
        funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# Known design projects from the document
known_projects = [
    'PCH Median Improvements Project',
    'Westward Beach Road Drainage Improvements Project',
    'Clover Heights Storm Drainage Improvements',
    'Latigo Canyon Road Retaining Wall Repair Project',
    'Storm Drain Master Plan',
    'Trancas Canyon Park Playground',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Outdoor Warning Signs',
    'Malibu Bluffs Park South Walkway Repairs',
    'Malibu Canyon Road Traffic Study'
]

# Simple count based on the funding data we saw in the preview
# These explicitly match names from the design section:
matching_names = [
    'PCH Median Improvements Project',
    'Westward Beach Road Drainage Improvements Project',
    'Storm Drain Master Plan',
    'Storm Drain Master Plan (FEMA Project)',
    'Outdoor Warning Signs',
    'Outdoor Warning Sirens (FEMA)',
    'Outdoor Warningn Sirens - Design (FEMA Project)'
]

# Count projects with > $50k funding
count = 0
for name in matching_names:
    name_lower = name.lower()
    if name_lower in funded and funded[name_lower] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0, 'var_functions.execute_python:72': {'funding': 'var_functions.query_db:0', 'civic': 'var_functions.query_db:2'}, 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
