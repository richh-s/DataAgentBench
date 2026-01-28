code = """import json

# Load funding data
f_file = var_functions.query_db:44
with open(f_file) as f:
    funding = json.load(f)

# Capital projects with design status from civic documents
capital_design_projects = [
    "2022 Morning View Resurfacing & Storm Drain Improvements",
    "PCH Median Improvements Project", 
    "Westward Beach Road Repair Project",
    "Westward Beach Road Drainage Improvements Project",
    "Clover Heights Storm Drainage Improvements",
    "Latigo Canyon Road Retaining Wall Repair Project",
    "Storm Drain Master Plan",
    "Trancas Canyon Park Upper and Lower Slopes Repair",
    "Civic Center Water Treatment Facility Phase 2",
    "Permanent Skate Park",
    "PCH at Trancas Canyon Road Right Turn Lane",
    "Outdoor Warning Signs",
    "Malibu Bluffs Park South Walkway Repairs",
    "Trancas Canyon Park Playground",
    "Malibu Canyon Road Traffic Study"
]

# Filter funding > $50,000
high_funding = []
for item in funding:
    if item.get('Amount'):
        try:
            amount = int(item['Amount'])
            if amount > 50000:
                high_funding.append(item)
        except:
            pass

# Match projects
matches = set()
for design in capital_design_projects:
    design_lower = design.lower()
    for fund in high_funding:
        fund_lower = fund['Project_Name'].lower()
        if design_lower in fund_lower or fund_lower in design_lower:
            matches.add(design)
            break

result = {'count': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
