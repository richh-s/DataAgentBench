code = """import json
import re
from collections import defaultdict

# Read the full funding data
funding_file_path = locals()['var_functions.query_db:5']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Read the MongoDB documents
mongo_docs = locals()['var_functions.query_db:6']

# Extract project information from MongoDB documents
project_info = defaultdict(dict)

for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into sections
    sections = re.split(r'\n\n[A-Z][a-zA-Z\s\-]+\n', text)
    
    # Look for project descriptions that contain emergency or FEMA keywords
    # These projects typically have status indicators
    
    # Pattern 1: Projects with status updates (e.g., "Project Schedule:", "Updates:")
    # Pattern 2: Projects with FEMA/CalOES suffixes
    
    # Find all project names and their contexts
    lines = text.split('\n')
    current_project = None
    in_project_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically start without bullet points)
        # Skip if line is too short or contains common headers
        if (len(line) > 10 and 
            not line.startswith('Agenda Item') and
            not line.startswith('Page') and
            not line.startswith('To:') and
            not line.startswith('Prepared by') and
            not line.startswith('Approved by') and
            not line.startswith('Date prepared') and
            not line.startswith('Meeting date') and
            not line.startswith('RECOMMENDED ACTION') and
            not line.startswith('DISCUSSION') and
            not line.startswith('Capital Improvement Projects') and
            not line.startswith('Disaster Recovery Projects') and
            not line.startswith('(') and  # Skip bullet points
            not any(keyword in line for keyword in ['Updates:', 'Project Schedule:', 'Project Description:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Complete Construction:'])):
            
            # Check if this looks like a project name
            if any(keyword in line.lower() for keyword in ['project', 'improvements', 'repairs', 'replacement', 'maintenance', 'structure']):
                current_project = line
                in_project_section = True
                
                # Extract status from surrounding context
                status = None
                project_type = None
                
                # Look for status indicators in next few lines
                for j in range(i+1, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    
                    if 'Complete Design:' in next_line or 'Advertise:' in next_line or 'Begin Construction:' in next_line:
                        status = 'design'
                        project_type = 'capital'
                        break
                    elif 'under construction' in next_line.lower() or 'construction was completed' in next_line.lower():
                        status = 'completed'
                        project_type = 'capital'
                        break
                    elif 'not started' in next_line.lower() or 'preliminary design' in next_line.lower():
                        status = 'not started'
                        project_type = 'capital'
                        break
                
                # Store project info
                if current_project:
                    project_info[current_project] = {
                        'status': status,
                        'type': project_type,
                        'topic': 'emergency,FEMA' if 'FEMA' in current_project or 'emergency' in current_project.lower() else None,
                        'source_file': filename
                    }

# Also extract projects with explicit FEMA or emergency references
for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for patterns like "Project_Name (FEMA Project)"
    # These are mentioned in the funding data
    
    # Search for any line that contains FEMA or emergency
    lines = text.split('\n')
    
    for line in lines:
        if ('FEMA' in line or 'emergency' in line.lower()) and len(line.strip()) > 5:
            line = line.strip()
            # Avoid capturing bullet points and headers
            if not line.startswith('(') and not any(header in line for header in ['Agenda Item', 'Page ', 'RECOMMENDED', 'DISCUSSION']):
                # This might be a project name or description
                if len(line) < 200:  # Reasonable length for a project name
                    # Try to extract a clean project name
                    if 'Updates:' not in line and 'Project Schedule:' not in line:
                        # Clean up the line
                        clean_line = re.sub(r'^[^a-zA-Z]*', '', line)  # Remove leading non-letters
                        clean_line = re.sub(r'[^a-zA-Z0-9\s\-\(\)]*$', '', clean_line)  # Remove trailing symbols
                        
                        if clean_line and len(clean_line) > 10:
                            project_info[clean_line] = {
                                'status': None,  # Will try to find from context
                                'type': 'disaster' if 'FEMA' in clean_line else None,
                                'topic': 'emergency,FEMA',
                                'source_file': doc.get('filename', '')
                            }

print("__RESULT__:")
print(json.dumps({
    "projects_found": len(project_info),
    "sample_projects": dict(list(project_info.items())[:10])
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:11': {'funding_count': 500, 'mongo_docs_count': 38}}

exec(code, env_args)
