code = """import json
import re

# Access stored data paths
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:2']

# Load data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project names from Design section
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    design_pos = text.find('Capital Improvement Projects (Design)')
    
    if design_pos > -1:
        section = text[design_pos:design_pos+3000]
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            if line and len(line) < 120:
                clean = re.sub(r'^[A-Z0-9]+[.)]\s*', '', line)
                if 'Project Schedule' not in clean and 'Updates' not in clean and len(clean) > 10:
                    has_keyword = any(k in clean.lower() for k in ['road','beach','park','storm','project','repair'])
                    if has_keyword and clean not in design_projects:
                        design_projects.append(clean)

# Get high funding projects
high_funding = [f for f in funding_data if int(f['Amount']) > 50000]

print('__RESULT__:')
result = {
    'design_projects': design_projects,
    'high_funding': [{'name': f['Project_Name'], 'amount': int(f['Amount'])} for f in high_funding]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
