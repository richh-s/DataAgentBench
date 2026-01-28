code = """import json, re, os
f_path = locals()['var_functions.query_db:6']
c_path = locals()['var_functions.query_db:2']

with open(f_path) as f:
    funding = json.load(f)

with open(c_path) as f:
    civic = json.load(f)

design_projects = []
for doc in civic:
    txt = doc.get('text','')
    if 'Capital Improvement Projects (Design)' in txt:
        start = txt.find('Capital Improvement Projects (Design)')
        end = start + 4000
        section = txt[start:end]
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and 'Project Schedule' not in line and 'Updates:' not in line:
                clean = re.sub(r'^[A-Z0-9]+[.)]\s*', '', line)
                clean = clean.replace('•','').replace('■','').replace('●','').strip()
                kws = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk','facility']
                if any(k in clean.lower() for k in kws):
                    design_projects.append(clean)

high_funding = [r for r in funding if int(r['Amount']) > 50000]

norm = lambda x: ' '.join(x.lower().split())

design_norm = [norm(p) for p in design_projects]
matches = set()

for fund in high_funding:
    f_norm = norm(fund['Project_Name'])
    for d_norm in design_norm:
        if f_norm in d_norm or d_norm in f_norm:
            matches.add(fund['Project_Name'])
            break

print('__RESULT__:' + str(len(matches)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}, 'var_functions.list_db:58': ['Funding'], 'var_functions.list_db:76': ['civic_docs'], 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)
