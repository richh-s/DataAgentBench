code = """import json, re

# Load data
with open(locals()['var_functions.query_db:6']) as f:
    funding = json.load(f)
with open(locals()['var_functions.query_db:2']) as f:
    civic = json.load(f)

# Extract design projects
design = []
for doc in civic:
    txt = doc.get('text','')
    if 'Capital Improvement Projects (Design)' in txt:
        start = txt.index('Capital Improvement Projects (Design)')
        end = start + 4000
        for line in txt[start:end].split('\n'):
            line = line.strip()
            if line and len(line) > 10 and 'Project Schedule' not in line and 'Updates:' not in line:
                design.append(line)

# Deduplicate
design_unique = list(set(design))

# Get high funding projects
high_funding = [r for r in funding if int(r['Amount']) > 50000]

# Match
matches = set()
for fund in high_funding:
    f_norm = ' '.join(fund['Project_Name'].lower().split())
    for d in design_unique:
        d_norm = ' '.join(d.lower().split())
        if f_norm in d_norm or d_norm in f_norm:
            matches.add(fund['Project_Name'])
            break

print('__RESULT__:')
print(json.dumps({'count': len(matches)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}, 'var_functions.list_db:58': ['Funding']}

exec(code, env_args)
