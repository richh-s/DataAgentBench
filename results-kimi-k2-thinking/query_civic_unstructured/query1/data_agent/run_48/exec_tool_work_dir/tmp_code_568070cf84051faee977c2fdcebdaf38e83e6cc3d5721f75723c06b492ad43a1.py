code = """import json

# Direct approach: use the exact matched projects based on analysis of both datasets
# From manual analysis of the documents:

# The question asks: "How many capital projects with a 'design' status have funding greater than $50,000?"

# Based on the civic documents, capital projects in design status include:
# - PCH Median Improvements Project
# - Storm Drain Master Plan  
# - Malibu Bluffs Park South Walkway / South Walkway Repairs
# - Malibu Canyon Road Traffic Study
# - PCH at Trancas Canyon Road Right Turn Lane
# - Outdoor Warning Signs / Sirens
# - PCH Crosswalk Improvements
# - Latigo Canyon Road Retaining Wall Repair Project
# - Westward Beach Road projects
# - Trancas Canyon Park Slope/Playground projects

# From funding data, these match with Amount > 50000:
matched_projects = {
    'PCH Median Improvements Project': 56000,
    'Storm Drain Master Plan': 77000,
    'Storm Drain Master Plan (FEMA Project)': 80000,
    'Malibu Bluffs Park South Walkway': 91000,
    'Malibu Bluffs Park South Walkway Repairs': 81000,
    'Malibu Canyon Road Traffic Study': 97000,
    'PCH at Trancas Canyon Road Right Turn Lane': 90000,
    'Outdoor Warning Signs': 92000,
    'Outdoor Warning Sirens (FEMA)': 81000,
    'Outdoor Warningn Sirens - Design (FEMA Project)': 84000,
    'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH': 84000,
    'Latigo Canyon Road Retaining Wall Repair Project': 97000,
    'Westward Beach Road Drainage Improvements Project': 87000,
    'Westward Beach Road Shoulder Repairs (CalOES Project)': 77000,
    'Trancas Canyon Park Slope Stabilization Project': 68000,
    'Trancas Canyon Park Playground Resurfacing': 65000
}

count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)
