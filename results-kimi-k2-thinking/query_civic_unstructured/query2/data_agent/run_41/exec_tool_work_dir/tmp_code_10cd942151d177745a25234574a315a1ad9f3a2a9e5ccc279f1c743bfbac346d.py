code = """import json

# Load funding data
funding_key = 'var_functions.query_db:5'
funding_val = locals()[funding_key]

if isinstance(funding_val, str) and funding_val.endswith('.json'):
    with open(funding_val, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_val

# Identify park-related projects completed in 2022 based on document analysis
# From the document preview:
# 1. Bluffs Park Shade Structure - completed November 2022
# 2. Point Dume Walkway Repairs - completed November 2022

park_projects_2022 = [
    'Bluffs Park Shade Structure',
    'Point Dume Walkway Repairs'
]

# Find matching funding and calculate total
total_funding = 0
matched_records = []

for target_project in park_projects_2022:
    for fund in funding_records:
        fund_name = fund['Project_Name']
        amount = int(fund['Amount'])
        
        # Check for matches (exact or partial)
        if target_project == fund_name or target_project in fund_name:
            total_funding += amount
            matched_records.append({
                'project': target_project,
                'funding_record': fund_name,
                'amount': amount
            })
            break

# Also check for similar variations
variations = [
    'Malibu Bluffs Park South Walkway',  # Similar to Point Dume
    'Malibu Bluffs Park South Walkway Repairs'  # Similar
]

# Create result
result_dict = {
    'total_funding': total_funding,
    'matched_projects': matched_records
}

output = json.dumps(result_dict)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
