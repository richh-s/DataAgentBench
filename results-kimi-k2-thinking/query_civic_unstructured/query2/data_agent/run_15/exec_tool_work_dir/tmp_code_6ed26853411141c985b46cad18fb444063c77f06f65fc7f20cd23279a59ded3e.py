code = """import json
import re

# Load funding data
f_file = var_functions.query_db:6
with open(f_file) as f:
    funding = json.load(f)

# Load civic documents  
c_file = var_functions.query_db:4
with open(c_file) as f:
    docs = json.load(f)

# Create funding lookup
funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding}

# Extract park projects completed in 2022
park_projects_2022 = []
park_keywords = ['park', 'playground', 'bluffs', 'trancas', 'skate', 'shade', 'walkway', 'arbors', 'benches']

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project name lines that contain park keywords
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'cid:' in line:
            continue
            
        line_lower = line.lower()
        
        # Check if this line mentions a park project
        if any(keyword in line_lower for keyword in park_keywords):
            # Clean the line to extract project name
            clean_name = re.sub(r'^\d+\.\s*', '', line)
            clean_name = re.sub(r'\s+\(cid:\d+\)$', '', clean_name)
            clean_name = clean_name.strip()
            
            # Check following lines for completion in 2022
            found_2022_completion = False
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].lower()
                if '2022' in next_line and ('completed' in next_line or 'completion' in next_line):
                    found_2022_completion = True
                    break
            
            if found_2022_completion and clean_name:
                park_projects_2022.append(clean_name)

# Deduplicate
park_projects_2022 = list(dict.fromkeys(park_projects_2022))

# Match with funding data
matched_projects = []
total_funding = 0

for proj_name in park_projects_2022:
    # Direct match
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        matched_projects.append({'project_name': proj_name, 'amount': amount})
        total_funding += amount
    else:
        # Partial match
        for funded_name, amount in funding_dict.items():
            if funded_name.lower() in proj_name.lower() or proj_name.lower() in funded_name.lower():
                matched_projects.append({'project_name': funded_name, 'amount': amount})
                total_funding += amount
                break

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'extracted_projects': park_projects_2022
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
