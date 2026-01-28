code = """import json

funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:2']

with open(funding_path) as f:
    funding_records = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Extract design capital projects
design_projects_text = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Find design section
    if 'Capital Improvement Projects (Design)' in text:
        lines = text.split('\n')
        capture = False
        for line in lines:
            if 'Capital Improvement Projects (Design)' in line:
                capture = True
                continue
            if 'Capital Improvement Projects (Construction)' in line:
                capture = False
                break
            if capture and line.strip():
                clean = line.strip().replace('•','').replace('■','').replace('●','')
                if len(clean) > 10 and 'Project Schedule' not in clean and 'Updates:' not in clean:
                    if clean not in design_projects_text:
                        design_projects_text.append(clean)

# Get funded projects > 50k
funded_names = [r['Project_Name'] for r in funding_records if int(r['Amount']) > 50000]

# Match function
def simple_match(name1, name2):
    n1 = ' '.join(name1.lower().split())
    n2 = ' '.join(name2.lower().split())
    return n1 in n2 or n2 in n1

# Find matches
matched = set()
for funded in funded_names:
    for design in design_projects_text:
        if simple_match(funded, design):
            matched.add(funded)

result = len(matched)
print('__RESULT__:')
print(json.dumps({'count': result}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
