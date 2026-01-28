code = """import json

# Load data
f_file = globals()['var_functions.query_db:4']
c_file = globals()['var_functions.query_db:5']

with open(f_file) as f:
    funding = json.load(f)
with open(c_file) as f:
    civic = json.load(f)

# Build funded projects dict (amount > 50000)
funded = {}
for rec in funding:
    if int(rec['Amount']) > 50000:
        funded[rec['Project_Name']] = int(rec['Amount'])

# Parse for capital design projects
count = 0
names = []
keywords = ['design capital', 'capital design', 'complete design', 'design phase capital']

for doc in civic:
    txt = doc.get('text', '').lower()
    if 'capital improvement' in txt and 'design' in txt:
        for line in doc.get('text', '').split(chr(10)):
            line_cleaned = line.strip()
            if line_cleaned and line_cleaned[0].isupper() and line_cleaned in funded:
                count = count + 1
                names.append(line_cleaned)

print('__RESULT__:')
print(json.dumps({'count': count, 'sample': names[:5]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5'], 'var_functions.execute_python:20': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding_name': 'Birdview Avenue Improvements'}, 'var_functions.execute_python:22': {'projects_with_funding': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:24': {'funding_projects': 276, 'message': 'Loaded funding data'}, 'var_functions.execute_python:26': {'total_funding_projects': 276, 'funding_dict_size': 276}}

exec(code, env_args)
