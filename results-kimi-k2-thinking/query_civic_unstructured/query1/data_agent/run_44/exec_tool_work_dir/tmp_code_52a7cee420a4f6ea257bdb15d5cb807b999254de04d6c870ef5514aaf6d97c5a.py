code = """import json

# Get data paths from previous queries
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:2']

# Load funding data (projects > $50,000)
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents
with open(civic_path) as f:
    civic_docs = json.load(f)

# Extract capital projects with design status from civic documents
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start > -1:
        # Extract the design section
        if construction_start > design_start:
            section = text[design_start:construction_start]
        else:
            section = text[design_start:design_start+4000]
        
        # Split into lines and extract project names
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and section headers
            if not line or len(line) < 10 or len(line) > 150:
                continue
            if 'Project Schedule' in line or 'Updates:' in line or 'Estimated Schedule' in line:
                continue
            if line.startswith('(') or line.startswith('•') or line.startswith('■'):
                continue
            
            # Clean the line
            import re
            clean_line = re.sub(r'^[0-9A-Z]+[.)]\s*', '', line)
            clean_line = clean_line.replace('•','').replace('■','').replace('●','').strip()
            
            # Check if it contains project-related keywords
            keywords = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk','facility','structure']
            has_keyword = any(k in clean_line.lower() for k in keywords)
            
            # Add if it looks like a project name
            if has_keyword and clean_line not in design_capital_projects:
                design_capital_projects.append(clean_line)

# Get list of high funding project names
high_funding_names = [rec['Project_Name'] for rec in funding_data]

# Match projects (normalize names for comparison)
def normalize(name):
    return ' '.join(name.lower().split())

design_names_normalized = set([normalize(p) for p in design_capital_projects])

matched_projects = []
seen = set()

for fund_name in high_funding_names:
    fund_normalized = normalize(fund_name)
    
    # Check for matches
    if fund_normalized in design_names_normalized:
        matched_projects.append(fund_name)
    else:
        # Fuzzy matching - check if design project name is contained in funding name or vice versa
        for design_norm in design_names_normalized:
            if (design_norm in fund_normalized or fund_normalized in design_norm) and len(design_norm) > 8:
                if fund_name not in matched_projects:
                    matched_projects.append(fund_name)
                break

# The answer is the count of matched projects
answer = len(matched_projects)

print('__RESULT__:')
print(json.dumps({'capital_design_projects_with_funding_over_50k': answer}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
