code = """import json
import re

funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:2']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract structured project data
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section for Capital Improvement Projects
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Not Started|$)', 
                             text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        section = design_match.group(1)
        lines = section.split('\n')
        
        current_project = None
        for line in lines:
            line = line.strip()
            # Skip empty lines and obvious non-project lines
            if not line or 'Project Schedule' in line or 'Updates' in line or 'RECOMMENDED' in line:
                continue
                
            # Clean the line
            clean_line = re.sub(r'^[A-Z0-9]+[.)]\s*', '', line)
            clean_line = clean_line.strip()
            
            # Check if this is a project name (has relevant keywords, reasonable length)
            if (10 < len(clean_line) < 120 and 
                any(k in clean_line.lower() for k in ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk']):
                
                # Check if it's not all uppercase heading
                if not (clean_line.isupper() and len(clean_line.split()) <= 3):
                    current_project = clean_line
                    capital_design_projects.append({
                        'Project_Name': current_project,
                        'type': 'capital',
                        'status': 'design'
                    })

# Remove duplicates based on project name
unique_design_projects = {}
for proj in capital_design_projects:
    name = proj['Project_Name']
    # Normalize name for matching (lowercase, remove extra spaces)
    key = ' '.join(name.lower().split())
    if key not in unique_design_projects:
        unique_design_projects[key] = proj

# Create a set of design project names for fast lookup
design_project_names = set(unique_design_projects.keys())

# Find funding matches (projects > $50k that match design projects)
matches = []
for fund in funding_data:
    fund_name = ' '.join(fund['Project_Name'].lower().split())
    amount = int(fund['Amount'])
    if amount > 50000:
        # Check for exact match or partial match
        if fund_name in design_project_names:
            matches.append({
                'Project_Name': fund['Project_Name'],
                'Amount': amount,
                'Status': 'design',
                'Type': 'capital'
            })
        else:
            # Check if any design project name is contained in the funding name
            for design_name in design_project_names:
                if design_name in fund_name or fund_name in design_name:
                    matches.append({
                        'Project_Name': fund['Project_Name'],
                        'Amount': amount,
                        'Status': 'design',
                        'Type': 'capital'
                    })
                    break

# Remove duplicate matches based on project name
unique_matches = {}
for match in matches:
    key = ' '.join(match['Project_Name'].lower().split())
    unique_matches[key] = match

result_count = len(unique_matches)

print('__RESULT__:')
print(json.dumps({
    'count': result_count,
    'projects': list(unique_matches.values())[:10]  # Sample of matching projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
