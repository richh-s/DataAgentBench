code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:6
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
civic_file = var_functions.query_db:4
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding dictionary
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Find park projects completed in 2022
park_projects = []
park_terms = ['park', 'playground', 'bluffs', 'trancas', 'skate', 'shade', 'walkway', 'arbors', 'benches']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for completion patterns
    for i in range(len(lines)):
        line = lines[i]
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look backward for project name
            for j in range(i-1, max(i-4, -1), -1):
                proj_line = lines[j].strip()
                if not proj_line or proj_line.startswith('('):
                    continue
                
                # Skip status markers
                lower_line = proj_line.lower()
                if any(marker in lower_line for marker in ['updates:', 'schedule', 'advertise', 'begin construction']):
                    continue
                
                # Check if park-related
                if any(term in lower_line for term in park_terms):
                    # Clean up the name
                    clean_name = re.sub(r'^\d+\.\s*', '', proj_line)
                    clean_name = re.sub(r'\s*Project Schedule.*', '', clean_name)
                    clean_name = clean_name.strip()
                    
                    if clean_name and len(clean_name) > 5:
                        park_projects.append(clean_name)
                        break

# Remove duplicates
park_projects = list(dict.fromkeys(park_projects))

# Match with funding data
matched_projects = []
total_funding = 0

for proj_name in park_projects:
    # Direct match
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        matched_projects.append({'project_name': proj_name, 'amount': amount})
        total_funding += amount
    else:
        # Partial match
        for funded_name, amount in funding_dict.items():
            # Check if either name contains the other
            if funded_name.lower() in proj_name.lower() or proj_name.lower() in funded_name.lower():
                matched_projects.append({'project_name': funded_name, 'amount': amount})
                total_funding += amount
                break

# Get result as JSON
result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'extracted_count': len(park_projects),
    'extracted_projects': park_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
