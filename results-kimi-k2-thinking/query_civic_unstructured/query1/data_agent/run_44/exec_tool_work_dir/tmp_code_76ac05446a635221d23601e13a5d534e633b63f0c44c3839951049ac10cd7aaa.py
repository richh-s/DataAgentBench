code = """import json

f_path = locals()['var_functions.query_db:6']
c_path = locals()['var_functions.query_db:2']

with open(f_path) as f:
    all_funding = json.load(f)

with open(c_path) as f:
    all_civic = json.load(f)

# Find design capital projects
design_names = []
for doc in all_civic:
    text = doc.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start > -1:
        snippet = text[start:start+3000]
        for line in snippet.split('\n'):
            line = line.strip()
            # Basic project name detection
            if line and 10 < len(line) < 150 and not line.startswith('('):
                if 'Project Schedule' not in line and 'Updates:' not in line and 'Estimated Schedule' not in line:
                    design_names.append(line)

# Funding > 50k
funded_over_50k = [f for f in all_funding if int(f['Amount']) > 50000]

# Normalize function
def norm(name):
    return ' '.join(name.lower().split())

design_norm = [norm(n) for n in design_names]
matched = []

for fund in funded_over_50k:
    f_name = fund['Project_Name']
    f_norm = norm(f_name)
    for d_norm in design_norm:
        # Check if names overlap
        if (f_norm in d_norm or d_norm in f_norm) and f_name not in matched:
            matched.append(f_name)
            break

# Simple output
print('__RESULT__:')
print('{"count":', len(matched), '}')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
