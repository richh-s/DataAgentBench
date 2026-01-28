code = """import json
import re

# Load funding data
funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    all_funding = json.load(f)

# Filter funding > $50,000
high_funding = {f['Project_Name'].lower().strip(): int(f['Amount']) 
                for f in all_funding if int(f['Amount']) > 50000}

# Load civic documents
civic_path = var_functions.query_db:10
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract design capital projects
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY|$)', 
                             text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        design_section = design_match.group(1)
        lines = design_section.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and bullet points
            if line and not line.startswith('(') and not line.startswith('■') and \
               not line.startswith('□') and not line.startswith('•') and \
               'Updates:' not in line and 'Schedule:' not in line and \
               'Complete Design:' not in line and 'Advertise:' not in line and \
               'Begin Construction:' not in line and \
               len(line) > 10 and 'Page' not in line:
                
                # Clean up the project name
                proj_name = line.strip()
                if proj_name and not proj_name.isupper():
                    design_projects.add(proj_name)

# Match with funding data
matched = []
for proj in design_projects:
    proj_lower = proj.lower()
    
    # Check for direct match or substring match
    for fund_name, amount in high_funding.items():
        if (proj_lower in fund_name or fund_name in proj_lower or 
            proj_lower.replace('project', '').strip() in fund_name or
            fund_name.replace('project', '').strip() in proj_lower):
            
            matched.append({
                'project': proj,
                'amount': amount,
                'funding_key': fund_name
            })
            break

# Deduplicate by project name
unique_matched = {}
for item in matched:
    unique_matched[item['project']] = item

result = {
    'count': len(unique_matched),
    'projects': list(unique_matched.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
