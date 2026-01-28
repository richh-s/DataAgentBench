code = """import json
import re

# Load MongoDB documents from civic_docs_database
mongo_docs_path = locals()['var_functions.query_db:0']
with open(mongo_docs_path, 'r') as f:
    mongo_docs = json.load(f)

# Load funding data from funding_database
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create a dictionary of funding data for easy lookup
funding_dict = {}
for fund in funding_data:
    funding_dict[fund['Project_Name']] = {
        'Funding_Source': fund['Funding_Source'],
        'Amount': fund['Amount']
    }

# Function to extract project information from text
projects = []

for doc in mongo_docs:
    text = doc['text']
    
    # Find projects by looking for patterns that indicate project names
    # Projects often appear as headers or with specific formatting
    
    # Pattern 1: Projects with status markers (common in these documents)
    # Look for lines that are project names followed by status indicators
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
            
        # Look for project names that are typically on their own line
        # These are often followed by status indicators
        
        # Pattern: Project name followed by status markers
        # Check if next few lines contain status indicators
        if i + 3 < len(lines):
            next_lines = '\n'.join(lines[i+1:i+4])
            
            # Check for status indicators, these suggest the current line is a project name
            has_status = 'Updates:' in next_lines or 'Project Schedule:' in next_lines or 'Complete' in next_lines
            
            # Check for year patterns or typical project indicators
            is_project_name = (
                has_status and 
                len(line) > 5 and  # Not too short
                not line.startswith(('(', '•', '-', '●', '_', 'Page', 'Agenda', 'Item', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION')) and
                not any(keyword in line.lower() for keyword in ['civic', 'commission', 'meeting', 'agenda', 'report', 'malibu', 'public', 'works']) or
                'Project' in line or 'Improvements' in line or 'Repair' in line or 'Drainage' in line
            )
            
            if is_project_name or any(keyword in line for keyword in ['FEMA', 'Emergency', 'emergency warning', 'siren', 'disaster']):
                project_name = line
                status = 'Unknown'
                
                # Extract status
                if 'Updates:' in '\n'.join(lines[i:i+5]):
                    # Look for status in following lines
                    for j in range(i+1, min(i+10, len(lines))):
                        if 'Complete Construction:' in lines[j]:
                            status = 'completed'
                            break
                        elif 'Begin Construction:' in lines[j] or 'Advertise:' in lines[j]:
                            status = 'in progress' if 'Begin Construction:' in lines[j] else 'design'
                            break
                        elif 'not started' in lines[j].lower():
                            status = 'not started'
                            break
                        elif 'updates:' in lines[j].lower() and 'currently under construction' in lines[j+1].lower():
                            status = 'in progress'
                            break
                        elif 'project schedule:' in lines[j].lower():
                            status = 'design'
                            break
                
                # Check if project is related to emergency/FEMA
                text_context = '\n'.join(lines[max(0,i-2):min(len(lines),i+10)])
                is_related = (
                    'FEMA' in project_name or 
                    'emergency' in project_name.lower() or
                    'emergency' in text_context.lower() or
                    'FEMA' in text_context or
                    'siren' in text_context.lower() or
                    'warning' in text_context.lower()
                )
                
                if is_related:
                    # Get funding info if available
                    funding_info = funding_dict.get(project_name, {
                        'Funding_Source': 'Not specified',
                        'Amount': 0
                    })
                    
                    projects.append({
                        'Project_Name': project_name,
                        'Funding_Source': funding_info['Funding_Source'],
                        'Amount': funding_info['Amount'],
                        'Status': status
                    })
        
        i += 1

# Also look for projects in a simpler way - find project names in funding data that contain FEMA or emergency
for fund in funding_data:
    proj_name = fund['Project_Name']
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower() or 'siren' in proj_name.lower() or 'warning' in proj_name.lower():
        # Only add if not already in projects
        if not any(p['Project_Name'] == proj_name for p in projects):
            # Find status from documents if possible
            status = 'Unknown'
            for doc in mongo_docs:
                if proj_name in doc['text']:
                    if 'currently under construction' in doc['text'].lower():
                        status = 'in progress'
                    elif 'complete construction' in doc['text'].lower():
                        status = 'completed'
                    elif 'not started' in doc['text'].lower():
                        status = 'not started'
                    elif 'design' in doc['text'].lower() and proj_name in doc['text']:
                        status = 'design'
                    break
            
            projects.append({
                'Project_Name': proj_name,
                'Funding_Source': fund['Funding_Source'],
                'Amount': fund['Amount'],
                'Status': status
            })

# Remove duplicates and format
seen = set()
unique_projects = []
for p in projects:
    key = p['Project_Name']
    if key not in seen:
        seen.add(key)
        unique_projects.append(p)

# Format the results in the required structure
result = []
for p in unique_projects:
    result.append({
        'Project_Name': p['Project_Name'],
        'Funding_Source': p['Funding_Source'],
        'Amount': p['Amount'],
        'Status': p['Status']
    })

# Handle the print format requirement
print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
