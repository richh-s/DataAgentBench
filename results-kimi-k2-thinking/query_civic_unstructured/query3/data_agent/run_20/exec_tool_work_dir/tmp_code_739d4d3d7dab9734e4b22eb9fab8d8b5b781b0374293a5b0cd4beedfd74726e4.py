code = """import json
import os

# Get the storage keys from the local scope
# The storage keys are stored as variables in locals(), but their names contain colons
# So we need to access them via the locals() dictionary

# Load civic documents
if isinstance(locals()['var_functions.query_db:4'], str):
    # It's a file path
    with open(locals()['var_functions.query_db:4']) as f:
        civic_docs = json.load(f)
else:
    # It's direct data
    civic_docs = locals()['var_functions.query_db:4']

# Load funding data  
if isinstance(locals()['var_functions.query_db:6'], str):
    with open(locals()['var_functions.query_db:6']) as f:
        funding_data = json.load(f)
else:
    funding_data = locals()['var_functions.query_db:6']

print('__RESULT__:')
print(json.dumps({
    "civic_docs_count": len(civic_docs),
    "funding_count": len(funding_data),
    "civic_doc_keys": list(civic_docs[0].keys()) if civic_docs else [],
    "sample_funding": funding_data[0] if funding_data else None
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
