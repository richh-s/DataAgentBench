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

# Process funding data into a dictionary
funding_dict = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_dict[project_name] = amount

# Helper function to extract project information from text
def extract_project_info(text):
    projects = []
    
    # Find sections that indicate completion
    # Pattern: Project name followed by status updates
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for completion mentions with 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look backward to find the project name (usually 1-3 lines before)
            for j in range(i-1, max(i-5, -1), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not any(marker in prev_line.lower() for marker in ['updates:', 'project schedule:', 'complete']):
                    # Clean up the project name
                    project_name = re.sub(r'^\d+\.\s*', '', prev_line)
                    project_name = re.sub(r'\s*Project Schedule:.*$', '', project_name)
                    project_name = re.sub(r'\s*\(cid:\d+\)$', '', project_name)
                    project_name = project_name.strip()
                    
                    if project_name and 10 < len(project_name) < 200:
                        projects.append({
                            'project_name': project_name,
                            'status': 'completed',
                            'year': '2022'
                        })
                        break
    
    return projects

# Extract all projects mentioned as completed in 2022
all_projects_2022 = []
for doc in civic_docs:
    projects = extract_project_info(doc['text'])
    all_projects_2022.extend(projects)

# Filter for park-related projects
park_keywords = ['park', 'playground', 'bluffs', 'trancas', 'point dume', 'skate', 'shade structure', 'walkway']
park_projects = []

for proj in all_projects_2022:
    proj_name_lower = proj['project_name'].lower()
    if any(keyword in proj_name_lower for keyword in park_keywords):
        park_projects.append(proj)

# Remove duplicates by name
unique_park_projects = {}
for proj in park_projects:
    name = proj['project_name']
    if name not in unique_park_projects:
        unique_park_projects[name] = proj

park_projects = list(unique_park_projects.values())

# Match with funding data and calculate total
matched_projects = []
total_funding = 0
unmatched_projects = []

for proj in park_projects:
    proj_name = proj['project_name']
    matched = False
    
    # Direct match
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        matched_projects.append({
            'project_name': proj_name,
            'amount': amount
        })
        total_funding += amount
        matched = True
    else:
        # Check for partial matches
        for funded_name, amount in funding_dict.items():
            # Check if one is contained in the other
            if (proj_name.lower() in funded_name.lower() or funded_name.lower() in proj_name.lower()):
                matched_projects.append({
                    'project_name': funded_name,
                    'amount': amount
                })
                total_funding += amount
                matched = True
                break
    
    if not matched:
        unmatched_projects.append(proj_name)

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'unmatched_park_projects': unmatched_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
