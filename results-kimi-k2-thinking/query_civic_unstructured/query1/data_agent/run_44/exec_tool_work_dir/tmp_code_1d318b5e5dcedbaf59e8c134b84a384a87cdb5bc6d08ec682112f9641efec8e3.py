code = """import json

# Load the data
civic_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:6']

with open(civic_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding_records = json.load(f)

# Extract design capital projects
project_list = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Simple search for design section
    start_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    start = text.find(start_marker)
    if start > -1:
        end = text.find(construction_marker, start)
        if end == -1:
            end = start + 4000
        section = text[start:end]
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and obvious section markers
            if line and len(line) > 10 and 'Project Schedule' not in line and 'Updates:' not in line:
                # Check if it's a project name by looking for keywords
                key_terms = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk','facility','structure','system']
                if any(term in line.lower() for term in key_terms) and not line[0].isdigit():
                    # Clean up the name
                    clean_name = line.replace('•', '').replace('■', '').replace('●', '').strip()
                    if clean_name not in project_list:
                        project_list.append(clean_name)

# Get high funding projects
high_funding_names = []
for rec in funding_records:
    if int(rec['Amount']) > 50000:
        high_funding_names.append(rec['Project_Name'])

# Simple matching based on project name similarity
def normalize(name):
    return ' '.join(name.lower().split())

design_project_names = [normalize(p) for p in project_list]
matches = []

for fund_name in high_funding_names:
    fund_normalized = normalize(fund_name)
    for i, design_name in enumerate(design_project_names):
        if design_name in fund_normalized or fund_normalized in design_name:
            if fund_name not in matches:
                matches.append(fund_name)

print('__RESULT__:')
print(json.dumps({'count': len(matches)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
