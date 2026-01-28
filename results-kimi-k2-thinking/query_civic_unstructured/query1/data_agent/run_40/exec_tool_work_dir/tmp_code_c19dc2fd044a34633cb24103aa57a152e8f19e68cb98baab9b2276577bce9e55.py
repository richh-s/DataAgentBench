code = """import json
import re

# Read the civic documents JSON file
civic_docs_file = var_functions.query_db:10
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read the funding JSON file
funding_file = var_functions.query_db:6
with open(funding_file, 'r') as f:
    funding = json.load(f)

# Define a function to extract projects from the text
def extract_design_capital_projects(text):
    projects = []
    
    # Look for "Capital Improvement Projects (Design)" section
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY PROJECTS|$)'
    design_match = re.search(design_section_pattern, text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        design_section = design_match.group(1)
        
        # Extract project names (lines that are project titles, typically just the name)
        # Project names usually appear as standalone lines or as bolded text
        lines = design_section.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip empty lines, update/schedule bullets, and common keywords
            if (line and 
                not line.startswith('(') and 
                not line.startswith('•') and 
                not line.startswith('■') and 
                not line.startswith('□') and 
                not line.startswith('Updates:') and
                not line.startswith('Project Schedule:') and
                not line.startswith('Estimated Schedule:') and
                not line.startswith('Complete') and
                not line.startswith('Advertise') and
                not line.startswith('Begin') and
                'Updates:' not in line and
                'Schedule:' not in line and
                len(line) > 5 and  # Not too short
                not any(keyword in line.lower() for keyword in ['page', 'of', 'agenda item']) and
                not line.isupper()):  # Not all caps (like section headers)
                
                # This looks like a project name
                projects.append(line)
    
    return projects

# Extract design capital projects from all documents
all_design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_design_capital_projects(text)
    all_design_projects.update(projects)

# For debugging: print the extracted projects
print("DEBUG: Extracted design capital projects:")
for p in sorted(all_design_projects):
    print(f"  - {p}")

# Get funding > $50,000
high_funding = [f for f in funding if int(f['Amount']) > 50000]

# For debugging: print high funding projects
print(f"\nDEBUG: Funding records > $50,000: {len(high_funding)}")

# Match projects (case-insensitive and handle slight variations)
matched_count = 0
matched_projects = []

for fund in high_funding:
    fund_name = fund['Project_Name'].lower().strip()
    
    # Check against all design projects
    for design_proj in all_design_projects:
        design_proj_lower = design_proj.lower().strip()
        
        # Direct match or design project is a substring of fund name
        # or fund name is a substring of design project
        if (fund_name == design_proj_lower or
            design_proj_lower in fund_name or
            fund_name in design_proj_lower):
            matched_count += 1
            matched_projects.append({
                'project_name': fund['Project_Name'],
                'amount': int(fund['Amount']),
                'funding_source': fund['Funding_Source']
            })
            break

# Remove duplicates (same project name might appear twice)
unique_projects = {}
for proj in matched_projects:
    unique_projects[proj['project_name']] = proj

final_count = len(unique_projects)

# Prepare result
result = {
    'count': final_count,
    'projects': list(unique_projects.values())
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
