code = """import json

# Load the data from the query results
with open(locals()['var_functions.query_db:6']) as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    civic_data = json.load(f)

# Create sets for tracking
high_funding_projects = {rec['Project_Name'] for rec in funding_data if int(rec['Amount']) > 50000}

# Extract design projects from civic documents
import re

design_capital_names = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Look for the design section
    design_marker = 'Capital Improvement Projects (Design)'
    if design_marker in text:
        # Get the section
        start = text.index(design_marker)
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1:
            end = start + 4000
        section = text[start:end]
        
        # Extract lines that could be project names
        for line in section.split('\n'):
            line = line.strip().replace('•','').replace('■','').strip()
            if line and len(line) > 10 and 'Project Schedule' not in line and 'Updates:' not in line:
                # Check for project keywords
                keywords = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk','facility']
                if any(k in line.lower() for k in keywords):
                    design_capital_names.add(line)

# Normalize names for matching
norm_high_funding = [' '.join(name.lower().split()) for name in high_funding_projects]
norm_design = [' '.join(name.lower().split()) for name in design_capital_names]

# Find matches
matched = []
for hf in high_funding_projects:
    hf_norm = ' '.join(hf.lower().split())
    for d_norm in norm_design:
        if hf_norm in d_norm or d_norm in hf_norm:
            matched.append(hf)
            break

answer = len(matched)
print('__RESULT__:')
print(json.dumps({'capital_design_projects_over_50k': answer}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}, 'var_functions.list_db:58': ['Funding']}

exec(code, env_args)
