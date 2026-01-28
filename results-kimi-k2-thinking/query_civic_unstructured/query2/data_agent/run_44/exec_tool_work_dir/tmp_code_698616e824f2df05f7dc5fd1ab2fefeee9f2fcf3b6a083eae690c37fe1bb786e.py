code = """import json

# Load the data
civic_docs_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)
    
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert amounts to integers
for fund in funding_data:
    fund['Amount'] = int(fund['Amount'])

# Based on the document preview, I can see explicit mentions of:
# 1. Bluffs Park Shade Structure - completed November 2022
# 2. Point Dume Walkway Repairs - completed November 2022  
# 3. Broad Beach Road Water Quality Repair - completed November 2022 (but road project)

# Let me search for these specifically
park_projects_2022 = [
    'Bluffs Park Shade Structure',
    'Point Dume Walkway Repairs'
]

# Find funding for these projects
total_funding = 0
matched_records = []

for project in park_projects_2022:
    proj_lower = project.lower()
    
    for fund in funding_data:
        fund_name_lower = fund['Project_Name'].lower()
        
        # Check for exact matches or partial matches
        if (proj_lower == fund_name_lower or 
            fund_name_lower in proj_lower or 
            proj_lower in fund_name_lower):
            total_funding += fund['Amount']
            matched_records.append({
                'project': project,
                'funding_record': fund['Project_Name'],
                'amount': fund['Amount'],
                'source': fund['Funding_Source']
            })

# Also check for any other park projects that might be in the data
print('__RESULT__:')
print(json.dumps({
    'specific_park_projects': park_projects_2022,
    'funding_matches': matched_records,
    'total_funding': total_funding,
    'record_count': len(matched_records)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:24': {'civic_docs': 5, 'funding': 500}}

exec(code, env_args)
