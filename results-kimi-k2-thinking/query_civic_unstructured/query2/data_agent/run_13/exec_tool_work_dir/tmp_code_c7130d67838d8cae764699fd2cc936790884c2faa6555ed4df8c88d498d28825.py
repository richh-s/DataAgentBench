code = """import json
import re

# Read the civic documents from the file
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Parse each document to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into sections to find project information
    # Look for patterns that indicate project listings
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        
        # Look for project name patterns (typically bolded or listed items)
        # Common patterns: project names are often followed by updates or schedule
        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('■'):
            # Check if this looks like a project name (not a header, not empty, reasonable length)
            if 10 < len(line) < 200 and not any(header in line.lower() for header in [
                'public works', 'commission', 'agenda', 'item', 'subject:', 'recommended action:',
                'discussion:', 'to:', 'chair', 'prepared by:', 'approved by:', 'date prepared:',
                'meeting date:', 'page', 'capital improvement projects', 'disaster recovery projects',
                'capital improvement projects (design)', 'capital improvement projects (construction)',
                'capital improvement projects (not started)', 'staff has also prepared'
            ]):
                # This might be a project name - check if followed by project details
                if current_project:
                    # Save previous project
                    if 'Project_Name' in project_info:
                        projects.append(project_info)
                
                current_project = line
                project_info = {'Project_Name': current_project, 'filename': filename}
        
        # Extract project details
        if current_project:
            # Look for status indicators
            if 'status:' in line.lower():
                status_match = re.search(r'status:\s*(\w+)', line, re.IGNORECASE)
                if status_match:
                    project_info['status'] = status_match.group(1).lower()
            elif 'updates:' in line.lower():
                # Look for status in updates
                if 'construction was completed' in line.lower() or 'completed' in line.lower():
                    project_info['status'] = 'completed'
            
            # Look for dates
            if 'et:' in line.lower() or 'complete:' in line.lower() or 'date:' in line.lower():
                # Extract year patterns
                year_match = re.search(r'(202[0-9])', line)
                if year_match:
                    project_info['et'] = year_match.group(1)
            elif 'construction was completed' in line.lower():
                year_match = re.search(r'(202[0-9])', line)
                if year_match:
                    project_info['et'] = year_match.group(1)
            
            # Look for topic indicators (park, road, etc.)
            if 'park' in line.lower():
                project_info['topic'] = 'park'
    
    # Don't forget the last project
    if current_project and 'Project_Name' in project_info:
        projects.append(project_info)

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for proj in projects:
    is_park = 'park' in proj.get('Project_Name', '').lower()
    is_completed = proj.get('status') == 'completed'
    is_2022 = proj.get('et') == '2022'
    
    if is_park and is_completed and is_2022:
        park_projects_2022.append(proj)

print('__RESULT__:')
print(json.dumps(park_projects_2022))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
