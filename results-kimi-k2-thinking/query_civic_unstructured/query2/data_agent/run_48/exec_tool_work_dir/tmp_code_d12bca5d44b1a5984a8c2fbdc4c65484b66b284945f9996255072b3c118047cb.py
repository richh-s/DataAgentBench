code = """import json
import re

# Read the full result from the file
file_path = var_functions.query_db:6
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

# Get funding data
funding_data = var_functions.query_db:0

# Function to extract project information from document text
def extract_projects_from_text(text, filename):
    projects = []
    
    lines = text.split('\n')
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if line looks like a project name (not too long, starts capitalized, not common heading)
        if line and len(line) < 150 and line[0].isupper() and not line.startswith('('):
            low_line = line.lower()
            if not any(heading in low_line for heading in ['capital improvement', 'disaster recovery', 
                                                        'page', 'agenda item', 'to:', 
                                                        'prepared by', 'subject:', 'recommended action',
                                                        'discussion:', 'updates:', 'project schedule:',
                                                        'complete', 'design:', 'advertise:', 'begin construction',
                                                        'estimated schedule:', 'project description', 'staff has also']):
                
                # Look ahead to see if this is followed by project details
                next_lines = ' '.join(lines[i+1:i+4]).lower()
                if 'updates:' in next_lines or 'construction' in next_lines or 'project is' in next_lines:
                    
                    # Save previous project
                    if current_project:
                        projects.append({
                            'Project_Name': current_project,
                            'topic': project_info.get('topic', ''),
                            'status': project_info.get('status', ''),
                            'date_info': project_info.get('date_info', ''),
                            'source_file': filename
                        })
                    
                    # Start new project
                    current_project = line
                    project_info = {'topic': '', 'status': '', 'date_info': ''}
                    
                    # Determine topic from name
                    name_low = line.lower()
                    if 'park' in name_low or 'playground' in name_low or 'walkway' in name_low:
                        project_info['topic'] = 'park'
                    elif any(w in name_low for w in ['road', 'street', 'highway', 'bridge']):
                        project_info['topic'] = 'road'
                    elif any(w in name_low for w in ['drain', 'storm', 'sewer']):
                        project_info['topic'] = 'drainage'
                    elif any(w in name_low for w in ['water', 'treatment']):
                        project_info['topic'] = 'water'
        
        # Look for status and completion info
        if current_project:
            low_line = line.lower()
            if 'completed' in low_line or 'construction was completed' in low_line:
                project_info['status'] = 'completed'
                if '2022' in line:
                    project_info['date_info'] = '2022'
                elif '2023' in line:
                    project_info['date_info'] = '2023'
            elif 'design' in low_line and 'complete' not in low_line:
                project_info['status'] = 'design'
            elif 'under construction' in low_line:
                project_info['status'] = 'construction'
            elif 'not started' in low_line:
                project_info['status'] = 'not started'
    
    # Don't forget the last project
    if current_project:
        projects.append({
            'Project_Name': current_project,
            'topic': project_info.get('topic', ''),
            'status': project_info.get('status', ''),
            'date_info': project_info.get('date_info', ''),
            'source_file': filename
        })
    
    return projects

# Extract all projects
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc.get('text', ''), doc.get('filename', ''))
    all_projects.extend(projects)

# Filter park projects completed in 2022
park_projects_2022 = []
for p in all_projects:
    if p['topic'] == 'park' and p['status'] == 'completed' and p['date_info'] == '2022':
        park_projects_2022.append(p)

print('Extracted projects count:', len(all_projects))
print('Park projects completed in 2022:', len(park_projects_2022))

for proj in park_projects_2022:
    print('Found project:', proj['Project_Name'])

# Get funding amounts for these park projects
funding_amounts = []
funding_list = funding_data if isinstance(funding_data, list) else []

for park_proj in park_projects_2022:
    proj_name = park_proj['Project_Name']
    for fund in funding_list:
        if fund['Project_Name'] == proj_name:
            funding_amounts.append({
                'Project_Name': proj_name,
                'Amount': int(fund['Amount'])
            })
            print(f"Found funding: {proj_name} - ${fund['Amount']}")
            break

# Calculate total funding
total_funding = sum(f['Amount'] for f in funding_amounts)

result = {
    'total_funding': total_funding,
    'project_count': len(funding_amounts),
    'funding_details': funding_amounts,
    'park_projects_2022': park_projects_2022
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
