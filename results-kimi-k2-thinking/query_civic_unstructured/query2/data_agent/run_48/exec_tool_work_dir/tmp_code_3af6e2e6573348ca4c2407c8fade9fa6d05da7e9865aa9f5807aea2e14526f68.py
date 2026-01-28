code = """import json
import re

# Read the full result from the file
file_path = var_functions.query_db:6
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")

# Function to extract project information from document text
def extract_projects_from_text(text, filename):
    projects = []
    
    # Look for project sections - they often appear after bullet points or specific patterns
    # Pattern to find project names and their subsequent updates
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project name patterns (often title case, followed by update sections)
        if line and not line.startswith('(') and not line.startswith('cid:') and \
           len(line) < 150 and not any(keyword in line.lower() for keyword in 
           ['capital improvement', 'disaster recovery', 'page', 'agenda item', 'to:', 'prepared by', 'subject:', 
            'recommended action:', 'discussion:', 'updates:', 'project schedule:', 'complete design:', 
            'advertise:', 'begin construction:', 'begin design:', 'estimated schedule:', 'project description:',
            'staff has also', 'this flier', 'public works commission', 'agenda report']) and \
           not line.isupper() and line[0].isupper():
            
            # Check if this is likely a project name (not a heading)
            if not any(heading in line for heading in ['Capital Improvement Projects', 'Disaster Recovery Projects',
                                                      'Design)', 'Construction)', 'Not Started)']):
                
                # Check if next few lines contain project-related keywords
                next_text = ' '.join(lines[i+1:i+5]).lower()
                if any(keyword in next_text for keyword in ['updates:', 'project schedule:', 'complete design:', 
                                                           'construction', 'project is', 'staff is']):
                    # Save previous project if exists
                    if current_project and project_info:
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
                    
                    # Extract topic from project name
                    project_name_lower = line.lower()
                    if 'park' in project_name_lower:
                        project_info['topic'] = 'park'
                    elif any(word in project_name_lower for word in ['road', 'street', 'highway']):
                        project_info['topic'] = 'road'
                    elif any(word in project_name_lower for word in ['drain', 'storm']):
                        project_info['topic'] = 'drainage'
                    elif any(word in project_name_lower for word in ['water', 'sewer']):
                        project_info['topic'] = 'water'
                    elif 'walkway' in project_name_lower or 'path' in project_name_lower:
                        project_info['topic'] = 'park'
        
        # Look for status and date information
        if current_project:
            line_lower = line.lower()
            
            # Check for completion status
            if 'completed' in line_lower:
                project_info['status'] = 'completed'
                # Look for date patterns
                if '2022' in line:
                    project_info['date_info'] = '2022'
                elif '2023' in line:
                    project_info['date_info'] = '2023'
            # Check for design/under construction status
            elif any(phrase in line_lower for phrase in ['design', 'under construction', 'construction was completed', 'construction completed']):
                if 'design' in line_lower and 'complete' not in line_lower:
                    project_info['status'] = 'design'
                elif 'under construction' in line_lower:
                    project_info['status'] = 'construction'
                elif 'complete' in line_lower and '2022' in line:
                    project_info['status'] = 'completed'
                    project_info['date_info'] = '2022'
    
    # Add the last project if exists
    if current_project and project_info:
        projects.append({
            'Project_Name': current_project,
            'topic': project_info.get('topic', ''),
            'status': project_info.get('status', ''),
            'date_info': project_info.get('date_info', ''),
            'source_file': filename
        })
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    if 'text' in doc and 'filename' in doc:
        projects = extract_projects_from_text(doc['text'], doc['filename'])
        all_projects.extend(projects)

# Filter for park-related projects completed in 2022
park_projects_2022 = [
    p for p in all_projects 
    if p['topic'] == 'park' and p['status'] == 'completed' and p['date_info'] == '2022'
]

print(f"Total projects extracted: {len(all_projects)}")
print(f"Park projects completed in 2022: {len(park_projects_2022)}")

# Show the park projects for verification
for proj in park_projects_2022:
    print(f"- {proj['Project_Name']}")

# Save results to a variable
result_data = {
    'all_extracted_projects': all_projects,
    'park_projects_2022': park_projects_2022,
    'total_park_projects_2022': len(park_projects_2022)
}

print('\n__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
