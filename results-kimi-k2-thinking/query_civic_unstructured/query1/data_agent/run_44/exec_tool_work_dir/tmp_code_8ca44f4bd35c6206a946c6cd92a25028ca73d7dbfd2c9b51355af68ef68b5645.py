code = """import json
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:2']

with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic = json.load(f)

design_projects = []
for doc in civic:
    txt = doc.get('text','')
    if 'Capital Improvement Projects (Design)' in txt:
        # Extract text between Design and Construction sections
        design_start = txt.find('Capital Improvement Projects (Design)')
        construction_start = txt.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start == -1: construction_start = design_start + 2000
        section = txt[design_start:construction_start]
        # Extract likely project names (lines that aren't too long, contain key terms)
        for line in section.split('\n'):
            line = line.strip()
            if 15 < len(line) < 200 and 'Project Schedule' not in line and 'Updates:' not in line:
                if any(term in line.lower() for term in ['road','beach','park','storm','drain','project','repair','improvement','bridge']):
                    design_projects.append(line)

# Remove duplicates
design_unique = []
for p in design_projects:
    if p not in design_unique:
        design_unique.append(p)

# Get high funding project names
high_funding_names = [r['Project_Name'] for r in funding if int(r['Amount']) > 50000]

# Find matches (case-insensitive partial matching)
matched = []
for design in design_unique:
    d_norm = ' '.join(design.lower().split())
    for fund in high_funding_names:
        f_norm = ' '.join(fund.lower().split())
        if d_norm in f_norm or f_norm in d_norm:
            if fund not in matched:
                matched.append(fund)
                break

print('__RESULT__:')
print(json.dumps({'design_count': len(design_unique), 'matched_count': len(matched)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
