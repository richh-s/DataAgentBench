code = """import json

funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file) as f:
    funding_all = json.load(f)

with open(civic_file) as f:
    civic_all = json.load(f)

# Extract design projects
all_design = []
for doc in civic_all:
    txt = doc.get('text', '')
    start = txt.find('Capital Improvement Projects (Design)')
    if start > -1:
        section = txt[start:start+4000]
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and 'Project Schedule' not in line and 'Updates:' not in line:
                clean = line.replace('•','').replace('■','').replace('●','').strip()
                if clean not in all_design:
                    all_design.append(clean)

# Get projects with >50k funding
funded_over_50k = []
for rec in funding_all:
    amount = int(rec['Amount'])
    if amount > 50000:
        funded_over_50k.append(rec['Project_Name'])

# Match projects
def norm(name):
    return ' '.join(name.lower().split())

design_norm = [norm(n) for n in all_design]
matched = []
for fund in funded_over_50k:
    f_norm = norm(fund)
    for i, d_norm in enumerate(design_norm):
        if f_norm in d_norm or d_norm in f_norm:
            if fund not in matched:
                matched.append(fund)

print('__RESULT__:')
print(json.dumps({'matched_count': len(matched)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
