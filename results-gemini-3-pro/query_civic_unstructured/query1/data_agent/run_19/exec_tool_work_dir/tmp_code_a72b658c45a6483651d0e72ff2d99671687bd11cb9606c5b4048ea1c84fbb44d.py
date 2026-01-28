code = """import json

with open(locals()['var_function-call-10318342191074584213'], 'r') as f:
    funding_data = json.load(f)
high_funding_db = {item['Project_Name']: float(item['Amount']) for item in funding_data if float(item['Amount']) > 50000}

# Check specific names
checks = [
    "Civic Center Water Treatment Facility",
    "Morning View",
    "Malibu Road",
    "Slope",
    "Trancas"
]

results = {}
for name in high_funding_db:
    for check in checks:
        if check.lower() in name.lower():
            results[name] = high_funding_db[name]

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-10318342191074584213': 'file_storage/function-call-10318342191074584213.json', 'var_function-call-9654609134184919281': 'file_storage/function-call-9654609134184919281.json', 'var_function-call-4559528786802393198': {'count': 12, 'matches': ['Outdoor Warning Signs', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Bluffs Park South Walkway', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Storm Drain Master Plan', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Canyon Road Traffic Study', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane']}, 'var_function-call-8228371129491145108': {'count': 13, 'matches': ['PCH at Trancas Canyon Road Right Turn Lane', 'Westward Beach Road Drainage Improvements Project', 'Outdoor Warning Signs', 'Civic Center Stormwater Diversion Structure', 'Storm Drain Master Plan (FEMA Project)', 'project_471', 'Trancas Canyon Park Playground Resurfacing', 'Clover Heights Storm Drain', 'Malibu Bluffs Park South Walkway Repairs', 'PCH Median Improvements Project', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'Permanent Skate Park']}, 'var_function-call-1696498921780090662': ["Line 'Trancas Canyon Park Upper and Lower Slopes Repair' mentions Trancas", "Line 'project' matched project_471", "Line 'PCH at Trancas Canyon Road Right Turn Lane' mentions Trancas", "Line 'Trancas Canyon Park Playground' mentions Trancas", "Line 'PCH at Trancas Canyon Road Right Turn Lane' mentions Trancas", "Line 'turn lane at the intersection of PCH and Trancas Canyon Road.' mentions Trancas", "Line 'PCH at Trancas Canyon Road Right Turn Lane' mentions Trancas", "Line 'turn lane at the intersection of PCH and Trancas Canyon Road.' mentions Trancas"]}

exec(code, env_args)
