code = """import json
import re

funding_file = str(locals()['var_functions.query_db:6'])
civic_file = str(locals()['var_functions.query_db:2'])

with open(funding_file) as f:
    funding_recs = json.load(f)
with open(civic_file) as f:
    civic_docs = json.load(f)

design_projects = []
for doc in civic_docs:
    txt = doc.get('text', '')
    # Find design section
    design_pos = txt.find('Capital Improvement Projects (Design)')
    if design_pos >= 0:
        construction_pos = txt.find('Capital Improvement Projects (Construction)', design_pos)
        if construction_pos < 0:
            construction_pos = design_pos + 4000
        section = txt[design_pos:construction_pos]
        # Parse lines
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 10:
                if 'Project Schedule' not in line and 'Updates:' not in line and 'Estimated Schedule' not in line:
                    clean = re.sub(r'^[A-Z0-9]+[.)]\s*', '', line)
                    clean = clean.replace('•','').replace('■','').replace('●','').strip()
                    keywords = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk','facility']
                    if any(k in clean.lower() for k in keywords) and clean not in design_projects:
                        design_projects.append(clean)

high_funding = [r for r in funding_recs if int(r['Amount']) > 50000]

def normalize(name):
    return ' '.join(name.lower().split())

design_names = set([normalize(p) for p in design_projects])
matches = set()

for fund in high_funding:
    fund_name = fund['Project_Name']
    fund_norm = normalize(fund_name)
    # Direct match
    if fund_norm in design_names:
        matches.add(fund_name)
    else:
        # Partial match
        for d in design_names:
            if (fund_norm in d or d in fund_norm) and len(d) > 8:
                matches.add(fund_name)
                break

result = len(matches)
print('__RESULT__:')
print(json.dumps({'count': result}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
