code = """import json

# Load funding data > $50,000
f_file = var_functions.query_db:50
with open(f_file) as f:
    funding = json.load(f)

# Capital projects with design status from civic documents (manually extracted from document)
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

# Check which of these have funding > $50,000
matches = []
for design_project in capital_design_projects:
    design_lower = design_project.lower()
    
    for fund_item in funding:
        fund_name = fund_item['Project_Name'].lower()
        fund_amount = int(fund_item['Amount'])
        
        # Check for name match (substring match)
        if design_lower in fund_name or fund_name in design_lower:
            matches.append({
                'project': design_project,
                'funding_name': fund_item['Project_Name'],
                'amount': fund_amount
            })
            break
        
        # Check for partial word matches on key terms
        design_words = design_lower.split()
        key_terms = [word for word in design_words if len(word) > 4 and word not in ['project', 'improvements', 'repair', 'repairs', 'road']]
        
        if len(key_terms) >= 2:
            match_count = sum(1 for term in key_terms if term in fund_name)
            if match_count >= 2:  # At least 2 key terms match
                matches.append({
                    'project': design_project,
                    'funding_name': fund_item['Project_Name'],
                    'amount': fund_amount
                })
                break

# Remove duplicates
unique_matches = []
seen_projects = set()
for match in matches:
    if match['project'] not in seen_projects:
        unique_matches.append(match)
        seen_projects.add(match['project'])

result = {
    'count': len(unique_matches),
    'matching_projects': unique_matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
