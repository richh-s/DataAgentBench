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

# Process funding data
funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Helper function to extract project information from text
def extract_project_info(text):
    projects = []
    
    # Patterns for different project statuses
    status_patterns = {
        'completed': [
            r'(?:Construction\s+was\s+completed[.,]?\s+)([A-Z][^\n.]*?)(?=\n|\Z)',
            r'(?:Complete[d]?[\s:]{1,3})([A-Z][^\n.]*)(?=\n|\Z)',
            r'([A-Z][^\n.]*?)\s+-\s*Construction was completed',
            r'([A-Z][^\n.]*?(?:\([^)]*\)|(?:Project|Phase|Improvements|Repairs)*)?)\s*[\n]?\(?cid:\d+\)?\s*Updates:\s*Construction was completed',
        ],
    }
    
    # Project name patterns that indicate park-related projects
    park_keywords = ['park', 'playground', 'bluffs', 'legacy park', 'trancas', 'zuma', 'malibu bluffs', 'skate park']
    
    # Look for mentions of 2022 completion
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Check if this line or nearby lines contain 2022 completion
        if '2022' in line and any(word in line.lower() for word in ['complete', 'construction was completed', 'notice of completion']):
            # Look for project name (usually before the status)
            # Search backwards for project name (usually uppercase or title case)
            for j in range(i-1, max(i-10, -1), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('cid:'):
                    # Check if this is a park-related project
                    if any(keyword in prev_line.lower() for keyword in park_keywords):
                        project_name = prev_line.strip()
                        # Clean up the name
                        project_name = re.sub(r'^\d+\.\s*', '', project_name)
                        project_name = re.sub(r'\s*(\(cid:\d+\)|\(cid:\d+\))$', '', project_name)
                        project_name = re.sub(r'\s*Project Schedule:.*$', '', project_name)
                        project_name = project_name.strip()
                        
                        if project_name and len(project_name) < 200:
                            # Check for exact match or partial match in funding data
                            for funded_name in funding_dict.keys():
                                if (project_name.lower() in funded_name.lower() or 
                                    funded_name.lower() in project_name.lower()):
                                    projects.append({
                                        'project_name': funded_name,
                                        'status': 'completed',
                                        'year': '2022',
                                        'topic': 'park'
                                    })
                                    break
                            else:
                                # If no funding match found, still add the extracted name
                                projects.append({
                                    'project_name': project_name,
                                    'status': 'completed',
                                    'year': '2022',
                                    'topic': 'park'
                                })
                            break
                    # If we hit another status section, stop searching
                    if any(marker in prev_line.lower() for marker in ['updates:', 'project schedule:', 'discussion:', 'capital improvement', 'disaster recovery']):
                        break
    
    return projects

# Extract park projects completed in 2022 from all documents
park_projects_2022 = []
for doc in civic_docs:
    projects = extract_project_info(doc['text'])
    park_projects_2022.extend(projects)

# Remove duplicates
unique_projects = {}
for proj in park_projects_2022:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = proj

park_projects_2022 = list(unique_projects.values())

# Now match with funding data and calculate total
matched_projects = []
total_funding = 0

for proj in park_projects_2022:
    proj_name = proj['project_name']
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        matched_projects.append({
            'project_name': proj_name,
            'amount': amount
        })
        total_funding += amount
    else:
        # Check for partial matches
        for funded_name, amount in funding_dict.items():
            if (proj_name.lower() in funded_name.lower() or 
                funded_name.lower() in proj_name.lower()):
                matched_projects.append({
                    'project_name': funded_name,
                    'amount': amount
                })
                total_funding += amount
                break

# Print results
print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'all_park_projects': [p['project_name'] for p in park_projects_2022]
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
