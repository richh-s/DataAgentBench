code = """import json
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:2']

with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic = json.load(f)

# Extract design projects
design = []
for doc in civic:
    txt = doc.get('text', '')
    start = txt.find('Capital Improvement Projects (Design)')
    if start > -1:
        part = txt[start:start+5000]
        for line in part.split('\n'):
            line = line.strip()
            if line and 10 < len(line) < 120 and 'Project Schedule' not in line and 'Updates:' not in line:
                design.append(line)

# Get funded > 50k
high = [r for r in funding if int(r['Amount']) > 50000]

# Match
matched = set()
for h in high:
    hname = ' '.join(h['Project_Name'].lower().split())
    for d in design:
        dname = ' '.join(d.lower().split())
        if hname in dname or dname in hname:
            matched.add(h['Project_Name'])
            break

result = len(matched)
print('__RESULT__:')
print(str(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
