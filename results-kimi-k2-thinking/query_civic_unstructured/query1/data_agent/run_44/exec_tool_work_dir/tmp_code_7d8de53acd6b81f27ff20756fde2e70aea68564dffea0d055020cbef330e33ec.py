code = """import json
import re

# Load funding data (> $50,000)
funding_file = locals()['var_functions.query_db:6']
with open(funding_file) as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_documents = json.load(f)

# Extract capital projects with design status from civic documents
design_capital_projects = []

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find the Design section
    design_start = text.lower().find('capital improvement projects (design)')
    construction_start = text.lower().find('capital improvement projects (construction)')
    
    if design_start > -1:
        # Extract design section
        if construction_start > design_start:
            section = text[design_start:construction_start]
        else:
            section = text[design_start:design_start+4000]
        
        # Parse project names from this section
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if line and 10 < len(line) < 200:
                # Skip headers and markers
                if any(skip in line for skip in ['Project Schedule', 'Updates:', 'Estimated Schedule', 'RECOMMENDED ACTION']):
                    continue
                if line.startswith('(') or line.startswith('•'):
                    continue
                
                # Clean line
                clean = re.sub(r'^[A-Z0-9]+[.)]\s*', '', line)
                clean = clean.strip()
                
                # Check for project keywords
                if any(k in clean.lower() for k in ['road','beach','park','storm','drain','project','repair','improvement']):
                    if clean not in design_capital_projects:
                        design_capital_projects.append(clean)

# Create normalized versions for matching
def normalize(name):
    return ' '.join(name.lower().split())

design_names = set(normalize(p) for p in design_capital_projects)

# Find matches with funding > $50,000
matches = []
for rec in funding_records:
    amount = int(rec['Amount'])
    if amount > 50000:
        fund_name = rec['Project_Name']
        fund_norm = normalize(fund_name)
        
        # Direct or partial match
        if fund_norm in design_names or any(d in fund_norm for d in design_names):
            matches.append(fund_name)

# Remove duplicates and count
unique_matches = list(set(matches))
result = len(unique_matches)

print('__RESULT__:')
print(json.dumps({'count': result, 'sample_projects': unique_matches[:5]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}, 'var_functions.list_db:58': ['Funding']}

exec(code, env_args)
