code = """import json

# Get file paths
f_path = locals()['var_functions.query_db:6']
c_path = locals()['var_functions.query_db:2']

# Load data
with open(f_path) as f:
    funding = json.load(f)
with open(c_path) as f:
    civic = json.load(f)

# Simple extraction and matching
design_names = []
for doc in civic:
    txt = doc.get('text','')
    start = txt.find('Capital Improvement Projects (Design)')
    if start > -1:
        end = start + 4000
        section = txt[start:end]
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 10:
                design_names.append(line)

# Get high funding projects
high_funding = []
for rec in funding:
    if int(rec['Amount']) > 50000:
        high_funding.append(rec['Project_Name'])

# Match with strict criteria
matched = []
for fund in high_funding:
    f_lower = ' '.join(fund.lower().split())
    for d in design_names:
        d_lower = ' '.join(d.lower().split())
        if f_lower in d_lower or d_lower in f_lower:
            if fund not in matched:
                matched.append(fund)
                break

# Create result
result = json.dumps({'count': len(matched)})

# Print in required format
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}, 'var_functions.list_db:58': ['Funding']}

exec(code, env_args)
