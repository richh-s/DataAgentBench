code = """import json, sys

# Load the funding data
fpath = locals()['var_functions.query_db:74']
try:
    with open(fpath, 'r') as f:
        funding = json.load(f)
except Exception as e:
    print(f'Error loading funding: {e}', file=sys.stderr)
    funding = []

# Load civic documents  
cpath = locals()['var_functions.query_db:30']
try:
    with open(cpath, 'r') as f:
        docs = json.load(f)
except Exception as e:
    print(f'Error loading docs: {e}', file=sys.stderr)
    docs = []

print('Funding records:', len(funding))
print('Civic docs:', len(docs))

# Sample of disaster projects from funding
print('\nSample disaster projects from funding:')
for item in funding[:100]:
    name = item.get('Project_Name', '').lower()
    if any(x in name for x in ['fema', 'caloes', 'caljpia', 'fire']):
        print(f"  {item['Project_Name']} - ${item['Amount']}")

# Sample 2022 projects from funding
print('\nSample 2022 projects from funding:')
for item in funding[:100]:
    if '2022' in item.get('Project_Name', ''):
        print(f"  {item['Project_Name']} - ${item['Amount']}")

# Load more funding data to check for disaster + 2022 combinations
print('\nLooking for disaster projects with 2022 in name...')
for item in funding:
    name = item.get('Project_Name', '')
    low = name.lower()
    if ('2022' in name and 
        any(x in low for x in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'recovery'])):
        print(f"  {name} - ${item['Amount']}")

# Check civic docs for project mentions
if docs:
    print(f'\nFirst doc text sample:')
    print(docs[0]['text'][:500])

result = {'funding_count': len(funding), 'docs_count': len(docs)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:22': {'total_funding_records': 500, 'total_funding_amount': 28094000, 'disaster_projects_count': 27, 'disaster_projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000]]}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
