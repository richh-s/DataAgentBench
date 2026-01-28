code = """import json
import re

# Load data from files
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file) as f:
    funding_records = json.load(f)

with open(civic_file) as f:
    civic_documents = json.load(f)

# Step 1: Extract capital projects with 'design' status from civic documents
design_capital_projects = []

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start > -1:
        # Extract design section
        if construction_start > design_start:
            section = text[design_start:construction_start]
        else:
            section = text[design_start:design_start+4000]
        
        # Split into lines and extract project names
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and markers
            if not line or len(line) < 10:
                continue
            # Skip section headers and descriptions
            if 'Project Schedule' in line or 'Updates:' in line or 'Estimated Schedule' in line:
                continue
            # Skip bullet points and special characters
            if line.startswith('(') or line.startswith('•') or line.startswith('■'):
                continue
            
            # Clean the line
            clean_line = re.sub(r'^[0-9A-Z]+[.)]\s*', '', line)
            clean_line = clean_line.strip()
            
            # Check if it looks like a project name (contains keywords, not all caps heading)
            keywords = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk','facility']
            has_keyword = any(k in clean_line.lower() for k in keywords)
            not_heading = not (clean_line.isupper() and len(clean_line.split()) <= 3)
            
            if has_keyword and not_heading and clean_line not in design_capital_projects:
                design_capital_projects.append(clean_line)

# Step 2: Get high funding projects (> $50,000)
high_funding_projects = []
for rec in funding_records:
    amount = int(rec['Amount'])
    if amount > 50000:
        high_funding_projects.append(rec['Project_Name'])

# Step 3: Match projects between the two lists
# Normalize names for better matching
def normalize_name(name):
    return ' '.join(name.lower().split())

# Build set of normalized design project names
design_names_normalized = set()
for proj in design_capital_projects:
    normalized = normalize_name(proj)
    if normalized:
        design_names_normalized.add(normalized)

# Find matches
matched_projects = []
seen_matches = set()

for fund_name in high_funding_projects:
    fund_normalized = normalize_name(fund_name)
    
    # Direct match check
    if fund_normalized in design_names_normalized:
        if fund_name not in seen_matches:
            seen_matches.add(fund_name)
            matched_projects.append(fund_name)
    else:
        # Partial fuzzy matching
        for design_norm in design_names_normalized:
            # Check if one name contains the other (more lenient matching)
            if (design_norm in fund_normalized or fund_normalized in design_norm) and len(design_norm) > 10:
                if fund_name not in seen_matches:
                    seen_matches.add(fund_name)
                    matched_projects.append(fund_name)
                break

# Result is the count
final_count = len(matched_projects)

# Return result in required format
print('__RESULT__:')
print(json.dumps({'capital_design_projects_with_high_funding': final_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
