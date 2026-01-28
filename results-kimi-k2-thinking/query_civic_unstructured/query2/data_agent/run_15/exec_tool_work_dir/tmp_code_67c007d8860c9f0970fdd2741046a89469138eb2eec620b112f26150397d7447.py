code = """import json
import re

# Load data
funding_file = var_functions.query_db:6
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:4
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding dictionary
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Extract projects completed in 2022 from documents
projects_2022 = []
for doc in civic_docs:
    text = doc['text']
    # Split into sections or lines to find completion mentions
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Look for 2022 completion mentions
        if '2022' in line and ('construction was completed' in line.lower() or 'completed' in line.lower() and '2022' in line):
            # Find project name (usually a few lines above)
            for j in range(i-1, max(i-3, -1), -1):
                potential_name = lines[j].strip()
                # Simple heuristic: project names are typically capitalized/title case and not too short
                if potential_name and len(potential_name) > 5 and not potential_name.startswith('('):
                    if not any(marker in potential_name.lower() for marker in ['updates:', 'project schedule:', 'complete']):
                        # Clean up
                        clean_name = re.sub(r'^\d+\.\s*', '', potential_name)
                        clean_name = re.sub(r'\s*Project Schedule.*', '', clean_name)
                        clean_name = clean_name.strip()
                        if clean_name:
                            projects_2022.append(clean_name)
                            break

# Filter for park-related projects
park_keywords = ['park', 'playground', 'bluffs', 'trancas', 'point dume', 'skate', 'shade', 'walkway', 'legacy', 'arbors', 'benches']
park_projects = []
for proj_name in projects_2022:
    if any(keyword in proj_name.lower() for keyword in park_keywords):
        park_projects.append(proj_name)

# Remove duplicates
park_projects = list(dict.fromkeys(park_projects))

# Match with funding data
matched_projects = []
total_funding = 0

for proj_name in park_projects:
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        matched_projects.append({'project_name': proj_name, 'amount': amount})
        total_funding += amount
    else:
        # Try partial matching
        for funded_name, amount in funding_dict.items():
            if proj_name.lower() in funded_name.lower() or funded_name.lower() in proj_name.lower():
                matched_projects.append({'project_name': funded_name, 'amount': amount})
                total_funding += amount
                break

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'extracted_park_projects': park_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
