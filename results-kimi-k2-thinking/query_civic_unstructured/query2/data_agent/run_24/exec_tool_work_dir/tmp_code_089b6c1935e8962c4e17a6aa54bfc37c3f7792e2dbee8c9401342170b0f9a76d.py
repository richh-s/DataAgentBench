code = """import json
import re

# Load civic documents from the temp file
civic_docs_path = '/tmp/tmpw8a01a0z.json'
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding records
funding_path = '/tmp/tmptjtu3_1d.json'
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded %d civic documents and %d funding records' % (len(civic_docs), len(funding_records)))

# Based on the sample, look for these specific 2022 completed park projects:
target_projects = {
    'Bluffs Park Shade Structure': False,
    'Marie Canyon Green Streets': False,
    'Broad Beach Road Water Quality Repair': False,
    'Point Dume Walkway Repairs': False
}

# Search civic documents for completion information
docs_text = ' '.join([doc.get('text', '') for doc in civic_docs])

for proj_name in target_projects.keys():
    proj_lower = proj_name.lower()
    # Check if project is mentioned with 2022 completion
    if proj_lower in docs_text.lower() and '2022' in docs_text:
        # Look for the specific project in context
        for doc in civic_docs:
            text = doc.get('text', '')
            if proj_lower in text.lower() and '2022' in text:
                if 'completed' in text.lower():
                    target_projects[proj_name] = True
                    print('Found %s completed in 2022' % proj_name)

# Calculate funding for projects confirmed completed in 2022
funding_dict = {}
for f in funding_records:
    funding_dict[f['Project_Name'].lower()] = int(f['Amount'])

total_funding = 0
confirmed_projects = []

for proj_name, confirmed in target_projects.items():
    if confirmed and proj_name.lower() in funding_dict:
        amount = funding_dict[proj_name.lower()]
        total_funding += amount
        confirmed_projects.append({'name': proj_name, 'amount': amount})
        print('Confirmed funding: %s - $%d' % (proj_name, amount))

print('Total confirmed funding: $%d' % total_funding)

result = {
    'total_funding': total_funding,
    'projects': confirmed_projects,
    'doc_projects_matched': len(confirmed_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
