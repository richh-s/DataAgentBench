code = """import json
import re

funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:2']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

capital_design = []

for doc in civic_docs:
    text = doc.get('text', '')
    match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Not Started)', text, re.DOTALL | re.IGNORECASE)
    if match:
        section = match.group(1)
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) < 120 and 'Project Schedule' not in line and 'Updates' not in line and len(line) > 10:
                clean = re.sub(r'^[A-Z0-9]+[.)]\s*', '', line)
                keys = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk']
                if any(k in clean.lower() for k in keys):
                    capital_design.append({'name': clean, 'status': 'design', 'type': 'capital'})

design_names = set([' '.join(p['name'].lower().split()) for p in capital_design])

matches = []
seen = set()

for f in funding_data:
    fund_name = ' '.join(f['Project_Name'].lower().split())
    if int(f['Amount']) > 50000:
        if fund_name in design_names:
            key = fund_name
            if key not in seen:
                seen.add(key)
                matches.append({'Project_Name': f['Project_Name'], 'Amount': int(f['Amount'])})
        else:
            for design in design_names:
                if design in fund_name or fund_name in design:
                    key = ' '.join(f['Project_Name'].lower().split())
                    if key not in seen:
                        seen.add(key)
                        matches.append({'Project_Name': f['Project_Name'], 'Amount': int(f['Amount'])})

print('__RESULT__:')
print(json.dumps({'count': len(matches)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
