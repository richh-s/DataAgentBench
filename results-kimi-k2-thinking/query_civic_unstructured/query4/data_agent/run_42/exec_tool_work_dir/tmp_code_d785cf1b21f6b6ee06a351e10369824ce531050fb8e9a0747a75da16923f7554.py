code = """import json

# Load the MongoDB results
mongo_result = var_functions.query_db:42
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_result

# Load the funding data
funding_result = var_functions.query_db:4
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_recs = json.load(f)
else:
    funding_recs = funding_result

# Build funding lookup
d = {rec['Project_Name']: int(rec['Amount']) for rec in funding_recs}

# Based on the MongoDB results, extract projects with Spring 2022 construction starts
# From the preview, these projects have "Begin Construction: Spring 2022":
spring_2022_projects = [
    'Marie Canyon Green Streets',
    'PCH Median Improvements Project', 
    'PCH Signal Synchronization System Improvements Project',
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'
]

# Count projects with funding data and sum amounts
count = 0
total_funding = 0
for project in spring_2022_projects:
    if project in d:
        count += 1
        total_funding += d[project]

result = f"Projects starting Spring 2022: {count}, Total funding: ${total_funding:,}"
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:92': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '61', 'Project_Name': 'Marie Canyon Green Streets', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '50000'}, {'Funding_ID': '71', 'Project_Name': 'PCH Median Improvements Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '56000'}, {'Funding_ID': '74', 'Project_Name': 'PCH Signal Synchronization System Improvements Project', 'Funding_Source': 'International Aid', 'Amount': '16000'}]}

exec(code, env_args)
