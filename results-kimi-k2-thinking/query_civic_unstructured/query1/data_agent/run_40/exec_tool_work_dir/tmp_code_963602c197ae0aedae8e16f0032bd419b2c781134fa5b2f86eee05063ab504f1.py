code = """import json
import re

# Load funding data
funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    all_funding = json.load(f)

# Get projects with funding > $50,000
high_funding_projects = {}
for record in all_funding:
    amount = int(record['Amount'])
    if amount > 50000:
        name = record['Project_Name'].lower().strip()
        high_funding_projects[name] = amount

# Load civic documents
civic_path = var_functions.query_db:10
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract design capital projects from documents
all_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find Capital Improvement Projects (Design) section
    # Pattern to capture the design section
    pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY|$)'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if match:
        design_section = match.group(1)
        lines = design_section.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and various markers
            if (line and 
                not line.startswith('(') and 
                not line.startswith('■') and 
                not line.startswith('□') and 
                not line.startswith('•') and
                'Updates:' not in line and
                'Schedule:' not in line and
                'Complete Design:' not in line and
                'Advertise:' not in line and
                'Begin Construction:' not in line and
                len(line) > 10 and
                not line.isupper()):
                
                # Clean up common artifacts
                clean_line = line.strip()
                if clean_line:
                    all_design_projects.add(clean_line)

# Match projects with funding
matched_projects = set()

for design_proj in all_design_projects:
    design_lower = design_proj.lower()
    
    # Try to match with funding projects
    for fund_name in high_funding_projects:
        # Direct match or substring in either direction
        if (design_lower in fund_name or 
            fund_name in design_lower or
            design_lower.replace('improvements', 'improvement') in fund_name or
            fund_name.replace('improvements', 'improvement') in design_lower):
            matched_projects.add(design_proj)
            break

# Count the matches
count = len(matched_projects)

result = {
    'count': count,
    'matched_projects': list(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
