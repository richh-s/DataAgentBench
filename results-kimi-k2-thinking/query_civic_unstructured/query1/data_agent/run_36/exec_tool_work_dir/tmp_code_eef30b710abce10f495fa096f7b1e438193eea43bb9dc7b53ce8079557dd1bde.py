code = """import json

# Load data
funding_file = var_functions.query_db:4
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Filter for funding > $50,000
high_funding_projects = []
for record in funding_data:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            high_funding_projects.append({
                'name': record['Project_Name'],
                'amount': amount,
                'id': record['Funding_ID']
            })
    except:
        pass

print(f"Total funding records > $50,000: {len(high_funding_projects)}")

# Based on the civic document preview, these are capital projects with design status:
design_projects_from_docs = [
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

print(f"Capital design projects from documents: {len(design_projects_from_docs)}")

# Match design projects with funding > $50,000
matches = []
for design in design_projects_from_docs:
    design_lower = design.lower()
    for fund in high_funding_projects:
        fund_lower = fund['name'].lower()
        
        # Exact or near-exact match
        if (fund_lower == design_lower or 
            fund_lower in design_lower or 
            design_lower in fund_lower):
            matches.append({
                'design_project': design,
                'funding_project': fund['name'],
                'amount': fund['amount']
            })
            break

result = {
    'capital_design_projects_with_funding_over_50k': len(matches),
    'matched_projects': matches
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
