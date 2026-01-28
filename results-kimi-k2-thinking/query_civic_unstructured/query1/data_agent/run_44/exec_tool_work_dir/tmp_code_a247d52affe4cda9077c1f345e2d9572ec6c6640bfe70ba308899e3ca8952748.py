code = """import json

# Load data from stored query results
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file) as f:
    funding_records = json.load(f)

with open(civic_file) as f:
    civic_documents = json.load(f)

# Extract capital design projects from civic documents
design_projects = []
for doc in civic_documents:
    text = doc.get('text', '').lower()
    if 'capital improvement projects (design)' in text:
        # Get a window of text after the design section
        start = text.index('capital improvement projects (design)')
        section = text[start:start+3000]
        lines = section.split('\n')
        for line in lines:
            clean = line.strip()
            if clean and len(clean) < 150:
                kws = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median']
                if any(k in clean for k in kws) and 'project schedule' not in clean:
                    design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Get high funding projects
high_funding = [r for r in funding_records if int(r['Amount']) > 50000]

# Match projects
matched = []
for fund in high_funding:
    fund_name = ' '.join(fund['Project_Name'].lower().split())
    for design in design_projects:
        design_name = ' '.join(design.lower().split())
        if fund_name in design_name or design_name in fund_name:
            if fund['Project_Name'] not in matched:
                matched.append(fund['Project_Name'])
                break

answer = len(matched)
print('__RESULT__:')
print(json.dumps({'count': answer}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}, 'var_functions.list_db:58': ['Funding']}

exec(code, env_args)
