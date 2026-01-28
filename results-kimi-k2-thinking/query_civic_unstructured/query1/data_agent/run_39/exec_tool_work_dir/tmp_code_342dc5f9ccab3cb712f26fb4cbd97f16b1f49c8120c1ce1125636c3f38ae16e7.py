code = """import json
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

manual_projects = [
    "2022 Morning View Resurfacing & Storm Drain Improvements",
    "PCH Median Improvements Project",
    "Westward Beach Road Drainage Improvements Project",
    "Clover Heights Storm Drainage Improvements",
    "Latigo Canyon Road Retaining Wall Repair Project",
    "Storm Drain Master Plan",
    "Civic Center Water Treatment Facility Phase 2",
    "Permanent Skate Park",
    "PCH at Trancas Canyon Road Right Turn Lane",
    "Outdoor Warning Signs",
    "Malibu Bluffs Park South Walkway Repairs",
    "Trancas Canyon Park Playground",
    "Malibu Canyon Road Traffic Study",
    "PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH",
    "Kanan Dume Biofilter",
    "City Traffic Signals Backup Power"
]

matches = []
for proj in manual_projects:
    for fund in funding_data:
        if fund['Project_Name'] == proj and int(fund['Amount']) > 50000:
            matches.append({'project': proj, 'amount': int(fund['Amount'])})

result = {
    'matches': matches,
    'count': len(matches),
    'total': sum(m['amount'] for m in matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
